# -*- coding: UTF-8 -*-
#print 'Hello World!'
import math

f1 = open(r"E:\Github\MyTools\data analysis\blue.txt")
f = open(r"E:\Github\MyTools\data analysis\purple.txt")

lines = f.readlines()+f1.readlines()

rgbls =[]

# get all data
for line in lines:
	if line == "" or line == "\n":
			continue
	if line == None:
			continue

	if "GET" in line:
		continue
	
	line = line.strip("% ")
	rgbl=line.split(",")
	#print rgbl
	rgbl[0].lstrip("0")
	rgbl[1].lstrip("0")
	rgbl[2].lstrip("0")

	
	#print [int(rgbl[0]),int(rgbl[1]),int(rgbl[2])]
	rgbls.append([int(rgbl[0]),int(rgbl[1]),int(rgbl[2])])

print("all data num:")
print(len(rgbls))
				 
# get all different data
dif_rgbs =[]
for data in rgbls:
	add = True
	for d in dif_rgbs:
		if data[0] == d[0] and data[1] == d[1] and data[2] == d[2]:
			add = False
	if add:
		dif_rgbs.append(data)
		#print data
		
print("dif data num:")
print(len(dif_rgbs))
				 

dif_r = 8
dif_g = 8
dif_b = 8
dif_len = 10


version_rgbs = []
for data in dif_rgbs:
	add = True
	for d in version_rgbs:
		#if abs(data[0]-d[0])>dif_r or abs(data[1]-d[1])>dif_g or abs(data[1]-d[1])>dif_b:
		#	add = True
		#	continue
		
		dis = (data[0]-d[0])**2+(data[1]-d[1])**2+(data[2]-d[2])**2
		if dis <= dif_len**2:
			add = False
	if add:
		version_rgbs.append(data)
		print(data)

print("dif version led data num:")
print(len(version_rgbs))
print("base on dif len:")
print(dif_len)	 
				 		 
				 
				 
				 
				 
				 
				 
