#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 2 score_d

import sys

previous_doc=0
temp_score=0.0

for line in sys.stdin:
# remove leading and trailing whitespace

	key,val = line.strip().split('\t')

	if key==previous_doc:
		temp_score=temp_score + float(val.split(',')[1])
	else:
		temp_sent = val.split(',')[0]

		if temp_score>0 and temp_sent=='p':
			print(key + '\t' + 'pp')
			previous_doc=key
			temp_score=0

		elif temp_score>0 and temp_sent=='n':
			print(key + '\t' 'pn')
			previous_doc=key
			temp_score=0

		elif temp_score<=0 and temp_sent=='p':
			print(key + '\t' 'np')
			previous_doc=key
			temp_score=0

		else:
			print(key + '\t' 'nn')
			previous_doc=key
			temp_score=0



