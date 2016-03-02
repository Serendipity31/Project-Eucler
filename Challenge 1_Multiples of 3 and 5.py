#Challenge 1: Multiples of 3 and 5
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

lst = [x for x in range(1,1001)]
nat_numbers = []

def sum(numbers):
	total = 0
	for number in numbers:
		if number % 3 == 0 or number % 5 == 0:
			nat_numbers.append(number)
			total += number
	return total

print (sum(lst))
