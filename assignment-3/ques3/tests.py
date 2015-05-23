########## TESTS for Part-a  ##########

rect1=Rectangle(Rectangle.Point(0,0),10,10)
rect2=Rectangle(Rectangle.Point(11,0),2,3)
rect3=Rectangle(Rectangle.Point(2,0),5,15)

assert(rect1.intersect(rect2) is False)
assert(rect1.intersect(rect3) is True)


########## TESTS FOR PART-B #################

strng=WordIterator('A quick brown fox jumps over')
it=iter(strng)
one=it.next()
two=it.next()
three=it.next()
four=it.next()
five=it.next()
six=it.next()

assert (one=='A' and six == 'over')




#################### TESTS FOR PART-C ################################
a=pointIterator((2,2),(5,2),2)
print a.next()
print a.next()
print a.next()






