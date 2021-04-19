from os import listdir
from os.path import join, isfile
import time
import datetime
import os

if __name__ != '__main__':
	exit()

roots = ['sub1', 'sub2']

for root in roots:
	files = [f for f in listdir(root) if isfile(join(root, f))]
	
	for file in files:
		f = join(root, file)
		
		try:
			dt = time.strptime(file, '%Y%m%d%H%M%S')
		
			mod = datetime.datetime(dt.tm_year, dt.tm_mon, dt.tm_mday, dt.tm_hour, dt.tm_min, dt.tm_sec)
			modTime = time.mktime(mod.timetuple())

			os.utime(f, (modTime, modTime))
		
		except ValueError as e:
			pass
		
