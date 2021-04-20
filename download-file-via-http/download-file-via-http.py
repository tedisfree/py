import os
import requests
import re

def main():
    print('start download test')
    with requests.get('http://tedisfree.github.io/abcdef', stream=True) as r:
        if r.status_code!=200:
            print('failed to download file (code=%d)' % r.status_code)

        if 'Content-Disposition' not in r.headers:
            print('cannot find content headers from response')
            return
        filename = re.findall('filename=(.+)', r.headers['Content-Disposition'])[0]
        if len(filename) == 0:
            print('cannot find file name from response')
            return

        filename = filename.replace('"', '')
        print('dest name = '+filename)

        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

    print('download complete. file name='+filename)


if __name__=='__main__':
    main()
