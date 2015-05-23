from ques1 import *
from ques2 import *
  
def runReverseIteatorTests():
    def testEmptyListIterator():
	    l = IterableDoublyLinkedList()
	    rev_it = l.getReverseIterator()
	    try:
		    rev_it.prev()
		    assert(False)
	    except StopIteration:
		    assert(True)
    def testReverseElementListIterator():
        l = IterableDoublyLinkedList()
        l.insert("name", "steve")
        l.insert("nam", "seve")
        l.insert("na", "teve")
        rev_it = l.getReverseIterator()
        rev_it.prev()
        rev_it.prev()
        rev_it.prev()
        try:
            rev_it.prev()
            assert(False)
        except StopIteration:
            assert(True)

    def testFwdElementListIterator():
        l = IterableDoublyLinkedList()
        l.insert("name", "steve")
        l.insert("nam", "seve")
        l.insert("na", "teve")
        rev_it = l.getForwardIterator()
        rev_it.next()
        rev_it.next()
        rev_it.next()
        try:
            rev_it.next()
            assert(False)
        except StopIteration:
            assert(True)

    testEmptyListIterator()
    testReverseElementListIterator()
    testFwdElementListIterator()
runReverseIteatorTests()
			
