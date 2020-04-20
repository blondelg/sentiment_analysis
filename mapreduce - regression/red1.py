#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 1 Regression

import sys


sumx=0.0
sumy=0.0
moy_x=0.0
moy_y=0.0
flag_moy=0
nb=0

for line in sys.stdin:

    try:

        key,val = line.strip().split('\t')

        if key=="AA":
            li=val.strip().split(',')
            nb+=float(li[0])
            temp_sumx=float(li[1])
            temp_sumy=float(li[2])
            sumx+=temp_sumx
            sumy+=temp_sumy

        if key=="ZZ":
            li=val.strip().split(',')
            x=float(li[3])
            y=float(li[4])
            if flag_moy==0:
                flag_moy=1
                moy_x=sumx/nb
                moy_y=sumy/nb

            print("ZZ" + '\t' + \
                str(nb) + "," + \
                str((x-moy_x)*(y-moy_y)) + "," + \
                str((x-moy_x)**2) + "," + \
                str(moy_x) +   "," + \
                str(moy_y) +  "," + \
                str(x) + "," + \
                str(y))

    except:
        continue

