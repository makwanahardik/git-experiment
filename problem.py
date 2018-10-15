import json
from pprint import pprint
diffrent_shade=[]

with open('palette.json') as data_file:
	data = json.load(data_file)

for color, color_shades in data.items():
	for shade, value in color_shades.items():
		if shade not in diffrent_shade:
			diffrent_shade.append(shade)

for color, color_shades in data.items():
	# print (color + ' : ')
	color_array=[];

	for d_shade in diffrent_shade:

		if not(d_shade in color_shades.keys()):
			color_array.append(d_shade);
	if len(color_array)>0 :
		print (color)
		print("====================================")
		print (color_array)
