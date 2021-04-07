import os


def main():
    with open('rfile.txt', 'w') as f:
        for root, _dir, _file in os.walk(os.getcwd()):
            for __file in _file:
                f.write('%s\t%s\r\n' % (__file, root))


if __name__ == '__main__':
    main()
