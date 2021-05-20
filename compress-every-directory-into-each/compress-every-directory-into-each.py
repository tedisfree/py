import sys
import os
import shutil


def main():
    if len(sys.argv) < 3:
        print('argument error')
        exit(1)

    root = sys.argv[-2]
    hierarchy = sys.argv[-1].split(',')

    if os.path.exists('tmp'):
        shutil.rmtree('tmp')
    os.mkdir('tmp')

    cur = os.path.join('tmp')
    for h in hierarchy:
        cur = os.path.join(cur, h)
        os.mkdir(cur)

    if not os.path.exists('out'):
        os.mkdir('out')

    for d in [_ for _ in os.listdir(root) if os.path.isdir(os.path.join(root, _))]:
        shutil.copytree(os.path.join(root, d), os.path.join(cur, d))
        shutil.make_archive(os.path.join('out', d), 'zip', 'tmp')
        shutil.rmtree(os.path.join(cur, d))

    shutil.rmtree('tmp')


if __name__ == '__main__':
    main()
