# -*- coding: utf-8 -*-


def frequencyTable(S):
	table = {}
	for c in S:
		if c in table:
			table[c] += 1
		else:
			table[c] = 1
	return table

print("Input String: ")
S = input()
T = frequencyTable(S)

unique = True
for key in T:
	if T[key] != 1:
		unique = False
		
if unique: 
	print("Is unique!")
else:
	print("Not unique!")
		


			 
  