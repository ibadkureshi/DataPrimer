# starting number
number=2

#while loop to go from number till 100 looking for primes
while number <= 100:
	#figure out if the number is a prime
	is_prime = True
	trial=2
	while trial < number:
		#test
		if (number % trial) == 0:
			is_prime = False
		trial +=1

	if is_prime:
		print number
	number += 1