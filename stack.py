# -*- coding: utf-8 -*-

# python Stack implementation

class Stack():
	
	
	def __init__(self):
		self.S = []
		self.size = 0
	
	def isEmpty(self):
		if len(self.S) == 0:
			return True
		else:
			return False
	
	def push(self, x):
		self.S.append(x)
		self.size = len(self.S) 
		
	def pop(self):
		if self.isEmpty():
			return 'Stack empty!'
		else:
			item = self.S[-1]
			self.S = self.S[:-1]
			self.size = len(self.S) 
			return item
	
	def peak(self):
		return self.S[-1]
	

if __name__ == '__main__':
	
	import numpy as npy
	
	S = Stack()
	print(S.isEmpty())
	print(S.size)
	
	for i in range(0, 10):
		S.push(npy.random.randint(1,100))
		
	S.push("hello")
	
	print("Stack size: " + str(S.size))
	
	for i in range(0, 11):
		print(S.pop())
	
	print(S.pop())
	print("Stack size: " + str(S.size))
	
	