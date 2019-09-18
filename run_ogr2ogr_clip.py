from __future__ import print_function
import os
from subprocess import call
call(["ls", "-l"])

boundary = "D:/Avi/ogr2ogr/model_boundary.shp"
datapath = "D:/Avi/ogr2ogr"
saveloc = datapath
filetype = "ESRI Shapefile"

for file in os.listdir(datapath):
	if file.startswith("1") and file.endswith(".shp"):
		print('Currently clipping {0}'.format(file))
		inp = datapath+"/"+file
		outp = saveloc+"/clip_"+file
		print(inp)
		print(outp)
		clip = 'ogr2ogr -clipsrc %s %s %s' % (boundary, outp, inp)
		call(clip)