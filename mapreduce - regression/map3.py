#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# mapper 3 Regression

import sys

 
sum_yest_ybar=0.0
sum_y_ybar=0.0

for line in sys.stdin:

    try:

        key,val = line.strip().split('\t')

        li=val.strip().split(',')

        a=float(li[0])
        b=float(li[1])
        yest_ybar2=float(li[2])
        y_ybar2=float(li[3])

        sum_yest_ybar+=yest_ybar2
        sum_y_ybar+=y_ybar2

    except:
        continue

print("AA" + '\t' + \
    str(a) + "," + \
    str(b) + "," + \
    str(sum_yest_ybar) + "," + \
    str(sum_y_ybar))
