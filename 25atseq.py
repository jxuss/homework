# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""




import random
import math

print('python3 25atseq.py')
nt = 30 
dna = ''
at = 0
for i in range(nt):
	r = random.randint(1,10)
	print (r)
	if r == 1 or r == 2 or r == 3:
		dna = 'A' + dna
		at +=1
	elif r == 4 or r == 5 or r == 6:
		dna = 'T' + dna
		at +=1
	elif r == 7 or r == 8:
		dna = 'C' + dna
	else :
		dna = 'G' + dna
AT = at / nt

print(nt, AT, dna)











