# This is where Exercise 5.4 goes
# Name: Lei Wang

def is_triangle(t1, t2, t3):
	if (t1+t2 >= t3) and (t1+t3 >= t2) and (t2+t3 >= t1) :
		print "yes"
	else:
		print "no"

def test_triangle():
	t1 = raw_input("give me an integer\n")
	t2 = raw_input("give me another integer\n")
	t3 = raw_input("give me a third integer\n")

	print "let me find out if it's a triangle ... "
	is_triangle(int(t1), int(t2), int(t3))

test_triangle()