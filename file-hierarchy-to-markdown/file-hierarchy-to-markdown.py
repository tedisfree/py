import os
import sys


def main():
    if len(sys.argv) < 3:
        print('usage:)')
        print('> python file-hierarchy-to-markdown.py <target-path> <output-markdown>')
        sys.exit(-1)

    print('dir=', sys.argv[1])
    print('output=', sys.argv[2])

    with open(sys.argv[2], 'w') as f:
        f.write('|Directory|File Name|Y/N|Description|\n')
        f.write('|---|---|---|---|\n')
        for _root, _dir, _files in os.walk(sys.argv[1]):
            if len(_files) > 0:
                __root = os.path.basename(_root)
                for _file in _files:
                    f.write('|%s|%s|N||\n' % (__root, _file))
                    __root = ''
        else:
            print('no data to write down')

    print('okay')


if __name__ == '__main__':
    main()
