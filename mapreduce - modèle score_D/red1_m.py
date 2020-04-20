#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 1 modele score_d

import sys


previous_word=None
flag_first_line=1


for line in sys.stdin:

    key,val = line.strip().split('\t')

    try:
        temp_sent=val.strip().split(',')[1]
        temp_doc=val.strip().split(',')[0]
        print(temp_doc +  '\t' + temp_sent + ',' + str(dist))

    except:
        dist=float(val)

