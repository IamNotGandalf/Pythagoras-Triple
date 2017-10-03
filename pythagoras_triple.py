#********************************************************************
#
#  Frank playing around with Python ...
#  29.Sep.2017
#
#  Quest from Project Euler: Problem #9 - Special Pythagorean Triplet
#
#  Find the product of  a * b * c
#
#  Conditions:
#
# 	a < b < c
#	a^2 + b^2 = c^2
#	a + b + c = 1000
#
#********************************************************************



#
# Check wehther a given triplet is valid within the given range
#

def valid_pythagoras_tripple(inp_a, inp_b, inp_c, inp_range):
	if ((inp_a+inp_b+inp_c) == inp_range):
		if (inp_a < inp_b < inp_c):
			if ((inp_a*inp_a + inp_b*inp_b) == inp_c*inp_c):
				return True
			else:
				return False
		else:
			return False
	else:
		return False
	pass

#
# Generate the required triples with a bit of optimization, otherwise e.g. range=1000
# would produce one Billion operations in brute force nested for loops. Idae: calculate 
# cc = x^2 + y^2 instead of looping with for. This should save some 10 Millonen Operations.
#

import time
from math import sqrt

start_time = time.time()
test_range = 1000
counter = 0

for a in xrange(1, test_range):
	for b in xrange(a + 1, test_range):
		
		# ... flow control and info

		# counter += 1
		# print 'Loop: ' + str(counter)

		c_sqr = a**2 + b**2
		c = int (sqrt (c_sqr))

		# Attention, int truncates the sqrt. So it will produce alot invalide results for cc as long as
		# we do not check whether it is realy an Integer. We could do so by subtracting cc from
		# sqrt(cc_sqr) and check against 0.
		
		if (c - sqrt(c_sqr) == 0):
			if valid_pythagoras_tripple(a, b, c, test_range):
				print('The winner is: ')
				print(a, b, c)
				print('The product is: ' + str(a * b * c))
				break

print('Done with the slightly optimized brute force ...')
print("It took %10.8f seconds ..." % (time.time() - start_time))


#****************************************************************
#
#  Now there is this f* cool random approach ...
#  Some experience on execution on my MAC Book ... 
#  		0.3 to 12.2 sec execution time
#		200.000 to > 4 Mio shots
#
#****************************************************************

import random

# reset time measurement

start_time = time.time()

# clean up from first run and setup for brute random ;-) ...

test_range = 1000
counter = 0

a = random.randint(1, test_range)
b = random.randint(a, test_range)
c_sqr = a**2 + b**2
c = int(sqrt(c_sqr))

while not valid_pythagoras_tripple (a, b, c, test_range):
	a = random.randint(1, test_range)
	b = random.randint(a, test_range)
	c_sqr = a**2 + b**2
	c = int(sqrt(c_sqr))
	counter += 1
	#
	# for further use: here should be an emergency exit for the loop in case random sucks ...
	# e.g. maximum shots or maximum runtime
 	#
	pass

print(a, b, c)

print('Done with the brute random ...')
print('It took %10.8f seconds ...' % (time.time() - start_time))
print('and %i shots ...' % counter)

