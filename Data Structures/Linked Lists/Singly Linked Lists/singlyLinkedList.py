"""
Singly Linked List is a collection of nodes that form a linear sequence
Each node stores a reference to the next node
The first and last node of the list are known as the "head" and the "tail" of the list
Process of moving through the list is "traversing"
Each node stores a reference to the element and the next node (except the tail)
How do we add a new element?
Example to append to the Head (inverse can be done for appending to the Tail) - We create a new node - Set its element to the new element - Set the next link to refer to the current head - Set the list's head to point to the new node
Removing an element from the Head is essentially the reverse operation to adding the item
We cannot easily remove the last node - to do so efficiently requires a doubly linked list
O(k) time to access elements
Constant time insertions and deletions in any position, arrays require O(n) time
Linked Lists can expand without having to specify their size ahead of time!

"""
#sample implementation

class Node(object):
	def __init__(self, value):
		self.value = value
		self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

# how to link the nodes?
a.nextNode = b
b.nextNode = c
 