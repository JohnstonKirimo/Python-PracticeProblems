"""
What are Queues?

Ordered collection of items where items addition happens at the end "rear"
Removal happens from the "front"
Item entered and waits in queue to be removed
Longest item at the front - FIFO implementation
"Enqueue" and "Dequeue" to the adding to the rear and removing the front
"Push" and "pop" refers to the queue.

"""

#sampleimplementation
# Queue() to create a queue
# enqueue(item) to add to the rear
# dequeue() removes from the front
# isEmpty() is the bool
# size() returns the size

class Queue(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item) # insert for FIFO

	def dequeue():
		return self.items.pop()

	def size():
		return len(self.items)

q = Queue()
q.size() 		# 0
q.enqueue(1)
q.enqueue(2)
q.dequeue() 	# 1
