#!/usr/bin/python

# Geoffroy Blondel
# Certificat Data Science 2018

# reducer 3 modele score_d

import sys

sum_pp = 0
sum_pn = 0
sum_np = 0
sum_nn = 0

previous_key = None

for line in sys.stdin:

	key, val = line.strip().split('\t')
	val = val.strip()


	if key!=previous_key:
		previous_key=key
		if val == "pp":
			sum_pp+=1

		elif val == "pn":
			sum_pn+=1

		elif val == "np":
			sum_np+=1

		else:
			sum_nn+=1

nume=sum_pp+sum_nn
deno=sum_pp+sum_pn+sum_np+sum_nn
print("matrice de confusion:")
print('\t'+' '+'pred pos'+'\t'+'pred neg')
print('real pos'+ ' ' + str(sum_pp) + '\t' +'\t'+ str(sum_pn))
print('real neg'+ ' ' + str(sum_np) + '\t' + '\t'+str(sum_nn))
print('accuracy : ' + str(float(nume) / float(deno)))

