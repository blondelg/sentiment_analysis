#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# mapper 1 Regression
import sys


 
nb=0
sumx=0.0
sumy=0.0

for line in sys.stdin:

    try:

        li=line.strip().split(',')
        x=float(li[0])
        y=float(li[1])
        sumx+=x
        sumy+=y
        nb+=1

        print("ZZ" + '\t' + str(nb) + "," + str(sumx) + "," + str(sumy) + "," + str(x) + "," + str(y))

    except:
        continue

print("AA" + '\t' + str(nb) + "," + str(sumx) + "," + str(sumy) + "," + str(x) + "," + str(y))