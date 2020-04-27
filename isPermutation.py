# -*- coding: utf-8 -*-


def frequencyTable(S):
	table = {}
	for c in S:
		if c in table:
			table[c] += 1
		else:
			table[c] = 1
	return table

def isPermutation(S1, S2):
	ST = frequencyTable(S1)
	TT = frequencyTable(S2)
	return ST == TT

print("String 1: ")
S1 = input()
print("String 2: ")
S2 = input()

print(isPermutation(S1, S2))
		


			 
  