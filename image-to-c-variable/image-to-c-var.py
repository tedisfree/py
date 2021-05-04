import os, sys
from PIL import Image

img = "input-image.bmp"
im = Image.open(img)
f = open(img+"txt", "w")

pix = im.load()
width, height = im.size

print(im.size)

prefix = "template_str[][]={\n"
f.write(prefix)

for y in range(height):
	prefix = "  {"
	f.write(prefix)
	
	for x in range(width):
		# print(pix[x,y], end="")
		if pix[x,y]==0:
			f.write("1,")
		else:
			f.write("0,")
			
	f.write("},\n")
	
f.write("};\n")
f.close()
