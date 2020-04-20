#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 3 Regression

import sys

# Input: x, y
# Output: count(x), sum(x), sum(y), x, y
 
sum_yest_ybar=0.0
sum_y_ybar=0.0

for line in sys.stdin:

    try:

        key,val = line.strip().split('\t')

        if key=="AA":

            li=val.strip().split(',')
            a=float(li[0])
            b=float(li[1])
            yest_ybar2=float(li[2])
            y_ybar2=float(li[3])

            sum_yest_ybar+=yest_ybar2
            sum_y_ybar+=y_ybar2

    except:
        continue

print("a" + '\t' + str(a))
print("b" + '\t' + str(b))
print("r2" + '\t' + str(sum_yest_ybar/sum_y_ybar))