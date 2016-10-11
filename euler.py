import math
import operator
from decimal import *

getcontext().prec = 1000

euler = str(sum(1 / Decimal(math.factorial(i)) for i in range (1,1000))) 
print euler
euler_list = euler[2:len(euler) - 1]

def check_prime(number):
	print "checking "+str(number)
	x = 0
	for i in xrange(2,number):
		if number % i == 0:
			return False
	return number
#or
def is_prime(a):
    return all(a % i for i in xrange(2, a))
	
for i in range(len(str(euler_list))-10):
    x = int(reduce(operator.add,euler_list[i:i+10]))
    if check_prime(x):
        print x
        print i
        break 
#or   
for i in xrange(2,len(euler_list)):
	x = euler_list[i:i+10]
	if check_prime(int(x)):
		print x
		break