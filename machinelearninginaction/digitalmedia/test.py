from numpy import *
from PIL import Image
import pickle as p
from os import listdir

def img2text():
	result = array([])
	fileList = listdir('./image.orig')
	m = len(fileList)
	for i in range(m):
		im = Image.open('./image.orig/%s' % fileList[i])
		imgSize = im.size[0]*im.size[1]
		r,g,b = im.split()
		r_arr = array(r).reshape(imgSize)
	 	g_arr = array(g).reshape(imgSize)
		b_arr = array(b).reshape(imgSize)
		image_arr = concatenate((r_arr, g_arr, b_arr))
		result = concatenate((result, image_arr))
	result = result.reshape((m, imgSize*3))
	#print type(result)
	return result
	# fr = open('myfile.txt','w')
	# for line in result:
	# 	fr.write(str(line))
	# fr.close()
			