class DoublyLinkedList(object):
    "Internal representation of a node in the doubly-lined list"
    class Node(object):
        def __init__(self, key, val):
            self.key = key						
            self.val = val						
            self.next = None
            self.prev = None				

            "initialize the required fields of a node instance"
            
        
        def __eq__(self, key):
            "compare the content of this node with the key"
            return (self.key == key)
        
        def val(self):
            "return the value stored in this node"
            return self.val

    def __init__(self):
        self.head = None
        self.tail = None
   
    """
    return the number of elements in the list.
    returns a number greater than or equal to zero.
    """
    def length(self):
        temp = self.head
	lens=0
        while (temp!=None):
    		lens += 1
    		temp = temp.next
        return lens
        

    """
    creates a new node initialized with 'key' and 'val', and makes
    'head' point to the new node.
    precondition: neither 'key' nor 'val' may be None. 
    postcondition: self.head will point to the new node.
    """
    def insert(self, key, val):
        if(key!=None and val!=None):
            newnode = DoublyLinkedList.Node(key, val)
            newnode.next=self.head
            if not self.head:
                self.tail = newnode
            else:
                newnode.next=self.head
                self.head.prev=newnode
            self.head = newnode
         
 
        return

    """
    searches from the 'head' of the list, the first occurrence of 'key'. 
    when found, returns 'val' associated with the key.
    returns None when 'key' is not in the list.
    postcondition: self.head is the starting of list 
    """ 
    def find(self, key):
        temp = self.head
        while (temp!=None):
            if (temp.key!=key):
	        temp=temp.next
            else:
                return temp.val
	return None
    """
    removes the node, if there's one, at the 'tail' position.
    postcondition: tail shifts by one if the list is not empty
    """
    def deleteLast(self):
       if (self.tail!=None):
           t=self.tail
           self.tail = t.prev
           if (self.tail!=None):
               self.tail.next =None
           else:
               self.head = None
           t=t.prev
                




            
    """
    removes the node, if there's one, at the 'head' position.
    postcondition: self.head points to the element next to the previous starting of the list.
    """
    def deleteFirst(self):
        if (self.head!=None):
            self.head = self.head.next
        if(self.head!=None):   
            self.head.prev = None
        return
        

    """
    finds the first entry that matches 'key', and deletes it.
    postcondition: If an entry with the key exists it is deleted from the list.
    """
    def delete(self, key):
        temp=self.head
        while(temp!=None):
            if(temp!=key):
                temp=temp.next
            else:
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                del temp







