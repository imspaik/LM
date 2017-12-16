#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime
f = open ("auth.log", "r")
inicioip= 129
finip= 143

li = []
ip = []
dic= {}

for linea in f.readlines():
	if "authentication failure" in linea:
		a=linea[inicioip: finip]
		ip.append(a)
		#print ip
		cats = (linea[:15])
		ts = datetime.strptime(cats, '%b %d %H:%M:%S')
		li.append(ts)
		dic= {"ip":ip}
#tambien puedo li.append(datetime.strptime(linea[:15], "%b %d %H:%S"))
#f.close()
#for dat in li:
#	print datetime.strftime(dat, "%b %d %H:%M:%S") 
#for ele in dic:
print dic

	

