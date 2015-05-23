from ques1 import *
class ForwardListIterator(object):			
	def __init__(self,head):
		self.node=head
	def next(self):
		if (self.node!=None):
			m=self.node.val
			self.node=self.node.next
			return m

		else :
			raise StopIteration()


class ReverseIterator(object):			
	def __init__(self,tail):
		self.node=tail
	def prev(self):
		if (self.node!=None):
			m=self.node.val
			self.node=self.node.prev
			return m

		else :
			raise StopIteration()

class IterableDoublyLinkedList(DoublyLinkedList):				
	def getReverseIterator(self):						
            return ReverseIterator(self.tail)
	def getForwardIterator(self):						
            return ForwardListIterator(self.head)

  
