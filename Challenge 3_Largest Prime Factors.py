#Challenge 3: Largest prime factor
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math

num = 13195
primes = [2]
prime_factors = []

'''Version 1 - Doesn't work'''
def max_prime(number):
	maxpf = number
	if (number % 2) != 0 and all(number % i != 0 for i in range(2, int(math.sqrt(number))+1)):
		print "%d is a prime number!" % (number)
	else:
		for n in range(3, number + 1, 2):
		'''
		This looks in a range starting with 3, going to half of the number provided, and incrementing by step 2.
		Doing this means that only odd numbers are considered, and that will speed 
		the operation up considerably. To get this to work simply, just initialize 
		the primes list with 2, rather than including 2 within the range here.
		This works because 2 is the only even prime number.
		
		https://www.quora.com/Is-there-a-relation-between-a-number-and-its-largest-prime-factor'''
		
		
			if all(n % i != 0 for i in range(2, int(math.sqrt(n))+1)):
			#FIX - make expression below check if number / n is prime
				new_number = number / n
				if all(new_number % i != 0 for i in range(2, int(math.sqrt(new_number))+1)):
					return " The maximum prime number factor of %d is %d" % (number, new_number)
					
				#else:
					#maxpf = (number / (2*n)) 
					
		'''
		This looks at a number divided by all previous numbers in a sequence
		(up to the square root of the number). This is a key point for finding 
		factors, and also saves a lot of time.
		
		The reason given for checking if a number is prime up until its square root is 
		as follows (from: http://stackoverflow.com/questions/5811151/why-do-we-check-upto-the-square-root-of-a-prime-number-to-determine-if-it-is-pri):
		
		"Let's say m = sqrt(n) then m × m = n. Now if n is not a prime then n can be written as n = a × b, so m × m = a × b. 
		Notice that m is a real number whereas n, a and b are natural numbers.

		Now there can be 3 cases:

		a > m ⇒ b < m
		a = m ⇒ b = m
		a < m ⇒ b > m

		In all 3 cases, min(a, b) ≤ m. Hence if we search till m, we are bound to find at least one factor of n, 
		which is enough to show that n is not prime."

		
		If each of them leave remainders, the number is prime
		doing this a different way, with nested for loops creates HUGE lists because
		each time a single division operation leaves a remainder the number gets added
		to the prime list, meaning that numbers are in there many times. That duplication 
		is not useful and takes a huge amount of time to deal with for larger numbers.
		'''
				primes.append(n)

'''Version 2 - Doesn't work 
The problem here is that it	doesn't see if the new_number is an integer...and if it's not an integer, then
it will pass the test as prime, even though it isn't actually prime
'''

def max_prime(number):
	for n in range(3, number + 1, 2):
		if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)):
			new_number = number / n
			if all(new_number % i != 0 for i in range(2, int(math.sqrt(new_number))+1)):
				return "The maximum prime number factor of %d is %d" % (number, new_number)


'''Version 3 - Doesn't work
What I wanted here was to use the knowledge provided on the site below that allows you to ID the largest
prime factor based on knowing small prime factors and the source number. 

https://www.quora.com/Is-there-a-relation-between-a-number-and-its-largest-prime-factor 
(see answer by Michael Northington)

I wanted to avoid the function iterating through all 600 billion numbers to make it fast.

The problem here is that the range isn't actually being modified beyond initialization.
Another format is required for that.
'''
def max_prime(number):
	pot_max_prime = 0
	max_prime_factor = 0
	for n in range(3, number + 1, 2):
		if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)):
		#checks if n is a prime number. If true, then n is prime.
			#print (n)
			if (number % n) ==0:
			#checks if n is a factor of the input number. If true, n is a prime factor.
				pot_max_prime = (number / n)
				#defines new variable that might be the max prime factor
				if all(pot_max_prime % i != 0 for i in range(2, int(math.sqrt(pot_max_prime))+1)):
				#checks if that potential max prime factor is a prime number. If true, pot_max_prime is answer.
					max_prime_factor = pot_max_prime
				return "The maximum prime number factor of %d is %d" % (number, max_prime_factor)


'''Version 4: Works (on small numbers within memory capacity)
This version works, and the range is dynamically changed using the reference below. 
(see: http://stackoverflow.com/questions/11905606/changing-the-number-of-iterations-in-a-for-loop)

Though a while loop is probably better

But it runs out of memory on the large number and can't complete the task.
'''

import math
primes = [2]
nonprimes = []
numtrack = []

def max_prime(number):
	num = number
	pot_max_prime = 0
	max_prime_factor = 0
	r = [x for x in range(3, num + 1, 2)]
	for n in r:
		if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)) and (number % n) ==0 and not all((number / n) % i !=0 for i in range(2, int(math.sqrt((number / n)))+1)):
			num = int((number / (2 * n)))
			if num % 2 != 0:
				num += 2
			else:
				num += 1
			a = r.index(num)
			del r[a:]
			primes.append(n)
			numtrack.append(num)

		elif all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)) and (number % n) ==0 and all((number / n) % i !=0 for i in range(2, int(math.sqrt((number / n)))+1)):
			max_prime_factor = (number / n)
			primes.append(n)
			return "The maximum prime number factor of %d is %d" % (number, max_prime_factor)

		else:
			nonprimes.append(n)
	

max(primes)


'''Version 5: Works (also on small numbers within memory capacity)
Transforms version 4 into a version with a while lool
'''

def max_prime(number):
	n = 3
	num = number
	pot_max_prime = 0
	max_prime_factor = 0
	while n <= num:
		if all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)) and (number % n) ==0 and not all((number / n) % i !=0 for i in range(2, int(math.sqrt((number / n)))+1)):
		#checks if n is prime, a factor of the input number, and if the ratio of the number to n is *not* prime
			num = int((number / (2 * n)))
			if num % 2 != 0:
				num += 2
			else:
				num += 1
			#Necessary in order to ensure only odd numbers are looked at
			primes.append(n)
			numtrack.append(num)

		elif all(n % i !=0 for i in range(2, int(math.sqrt(n))+1)) and (number % n) ==0 and all((number / n) % i !=0 for i in range(2, int(math.sqrt((number / n)))+1)):
		#checks if n is prime, a factor of the input number, and if the ratio of the number to n is prime
			max_prime_factor = (number / n)
			primes.append(n)
			return "The maximum prime number factor of %d is %d" % (number, max_prime_factor)
		else:
			other.append(n)
		n += 2


'''Version 6: 
Copied from Triptych here: http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number/412942#412942
Works instantly. 
Answer is 6857 from list of [71, 839, 1471, 6857.0]
'''

num = 600851475143

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0: #this loops through a number for as many times that 2 is a prime factor before incrementing d and checking the next number
            factors.append(d)
            n /= d
        d = d + 1 #it works to increment by 1 because even numbers that would be factors are already taken care of by dividing by smaller prime numbers.
        if d*d > n: #this must relate to the relationship between a prime number and its square root
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(num)
largest_prime_factor = max(pfs)

'''Version 7: 
Copied from Triptych here: http://stackoverflow.com/questions/23287/largest-prime-factor-of-a-number/412942#412942
Works instantly. Tried to adjust this based on the suggestion to iterate separately for 2 and then only for odd numbers since
2 is the only even prime number....but for some reason this doesn't seem to work. 
Answer is 6857 (from list of prime factors: [71, 839, 1471, 6857.0])

'''

num = 600851475143

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    while n > 1:
        while n % 2	== 0:
            factors.append(2)
            n /= 2
		d = 3
        while n % d == 0:
		    factors.append(d)
            n /= d
        d = d + 2
		if d*d > n:
		#Don't totally understand this, but it has to do with the relationship between prime numbers, factors, and their square root
		#possibly explained above
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(num)
largest_prime_factor = max(pfs)

				
'''For reference: a function to quickly check if a number is prime'''
def is_prime(x):
	if x == 2:
		return True
	elif x > 2:
		for n in range(2, x):
		    if x % n == 0:
			    return False
		else:
			return True
	elif x < 2:
		return False