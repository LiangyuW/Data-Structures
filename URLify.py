# -*- coding: utf-8 -*-

def URLify(s, length):
	l = list(s)
	space = 0
	for i in range(0, length):
		if l[i] == ' ':
			space += 2
	newLength = length+space
	
	for i in reversed(range(length)):
		if l[i] == " ":
			l[newLength-3:newLength] = ['%','2','0']
			newLength = newLength-3
		else:
			l[newLength-1] = l[i]
			newLength = newLength-1
	return "".join(l)

print(URLify("mr john smith    ", 13))

