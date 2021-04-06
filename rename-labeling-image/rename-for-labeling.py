import os
import sys

if __name__ != '__main__' :
    print('not-main')
    sys.exit()

RENAME_PREFIX = 'palm2'
IMAGE_PATH = './images/'

index = 0
for filename in os.listdir(IMAGE_PATH) :
    extIndex = filename.rfind('.')
    if extIndex is -1 :
        continue

    name = filename[:extIndex]
    extension = filename[extIndex:]

    src = IMAGE_PATH+filename
    dst = IMAGE_PATH+'{}_{:06}{}'.format(RENAME_PREFIX, index, extension)
    index += 1
    os.rename(src, dst)
    print('{:05}  {}'.format(index, filename))

print('job done')

