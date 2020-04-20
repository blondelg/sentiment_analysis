#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# mapper 2 Regression

import sys

 
nb=0
sumxy=0.0
sumxx=0.0

for line in sys.stdin:

    try:

        key,val = line.strip().split('\t')

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

        print("ZZ" + '\t' + \
            str(nb) + "," + \
            str(sumxy) + "," + \
            str(sumxx) + "," + \
            str(xbar) + "," + \
            str(ybar) + "," + \
            str(x) + "," + \
            str(y))

    except:
        continue

print("AA" + '\t' + \
    str(nb) + "," + \
    str(sumxy) + "," + \
    str(sumxx) + "," + \
    str(xbar) + "," + \
    str(ybar) + "," + \
    str(x) + "," + \
    str(y))