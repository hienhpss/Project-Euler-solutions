# 
# Solution to Project Euler problem 15
# by Project Nayuki
# 
# http://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 


def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result


def binomial(n, k):
	return factorial(n) // (factorial(k) * factorial(n - k))


print(binomial(40, 20))