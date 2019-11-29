# -*- coding: utf-8 -*-

# Python Queue implementation

class Queue():
	
	def __init__(self):
		self.Q = []
		self.size = len(self.Q)
		
	def enqueue(self, x):
		self.Q.append(x)
		self.size = len(self.Q)
		
	def dequeue(self):
		if self.size == 0:
			return "empty queue!"
		else:
			item = self.Q[0]
			self.Q = self.Q[1:]
			self.size = len(self.Q)
			return item
	
if __name__ == '__main__':
	
	import numpy as npy
	
	Q = Queue()
	
	for i in range(0, 10):
		r= npy.random.randint(0, 100)
		print(str(r) + " ", end = " ")
		Q.enqueue(r)
	print("Kurisu")
	Q.enqueue("kurisu")
	
	print("Queue size is " + str(Q.size))
	
	for i in range(0, 11):
		print(Q.dequeue())
	
	print("Queue size is " + str(Q.size))
	
	print(Q.dequeue())