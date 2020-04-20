#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 2 Regression

import sys

 
nb=0
sumxy=0.0
sumxx=0.0
flag_coef=0

for line in sys.stdin:

    try:

        key,val = line.strip().split('\t')

        if key=="AA":

        	li=val.strip().split(',')

        	nb=float(li[0])
        	xy=float(li[1])
        	xx=float(li[2])
        	xbar=float(li[3])
        	ybar=float(li[4])
        	x=float(li[5])
        	y=float(li[6])

        	sumxy+=xy
        	sumxx+=xx

        if key=="ZZ":
        	li=val.strip().split(',')

        	nb=float(li[0])
        	xy=float(li[1])
        	xx=float(li[2])
        	xbar=float(li[3])
        	ybar=float(li[4])
        	x=float(li[5])
        	y=float(li[6])

        	if flag_coef==0:
        		flag_coef=1

        		a=sumxy/sumxx
        		b=ybar-a*xbar

        	yest_ybar2=((a*x+b)-ybar)**2
        	y_ybar2=(y-ybar)**2

        	print("ZZ" + '\t' + \
        		str(a) + "," + \
        		str(b) + "," + \
        		str(yest_ybar2) + "," + \
        		str(y_ybar2))

    except:
        continue