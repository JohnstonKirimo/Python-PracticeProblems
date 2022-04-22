"""
next and prev for references to nodes that are both next and what precedes it
"dummy" nodes are known as the header sentinel and trailer sentinel for both the beginning and end of a list respectively
Each insertion happens between a pair of existing nodes - eg. Add between header and what is after to add to the front

"""

#sample solution
class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None
		self.prevNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.prevNode = a
b.nextNode = c
c.prevNode = b
