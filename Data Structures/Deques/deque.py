"""
A deque is a double-ended queue, with a front and an end and the items are positioned within the collection
It has an nonrestrictive nature for adding items - can add to front OR rear and the same applies for for removal
Does not require LIFO/FIFO enforced data structure design

"""
#sample implementation
# Deque() create a deque
# addFront(item)
# addRear(item)
# removeFront()
# removeRear()
# isEmpty()
# size()

class Deque(object):
	def __init__:
		self.items = []

	def isEmpty(self):
		return self.items == []

	# rear is the first index
	def addRear(self, item):
		self.items.insert(0, item)

	# front is the len(self.items) index
	def addFront(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.popleft()

	def size(self):
		return len(self.items)

d = Deque()
d.addFront('hello')
d.addRear('world')
d.size() 										# 2
print d.removeFront() + ' ' + d.removeRear() 	# 'hello world'
d.size() 										# 0
