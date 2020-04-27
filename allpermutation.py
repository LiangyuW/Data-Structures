# -*- coding: utf-8 -*-


def allpermutation(s, prefix):
	if len(s)==0:
		print(prefix)
		return

	for i in range(0, len(s)):
		rem = s[0: i]+s[i+1:len(s)]
		allpermutation(rem,prefix+s[i])				
			
print(allpermutation("cool!", ""))

