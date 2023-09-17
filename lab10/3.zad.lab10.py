#Задача 3. Да се напише програма, която да реализира генератор на прости числа.

def is_prime(x):
	is_prime_fl = True

	for el in range(2,x):
		if x%el==0:
			is_prime_fl = False
			break
	return is_prime_fl
	
primes = [x for x in range(10) if is_prime(x)]
print(primes)