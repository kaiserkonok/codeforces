from math import inf


def calculated_formula(a, b, c):
	return (c - a) + (b - c)


def solution(a, b):
	minimum = inf

	for c in range(a, b + 1):
		val = calculated_formula(a, b, c)

		if val < minimum:
			minimum = val

	return minimum


n_tests = int(input())


for _ in range(n_tests):
	a, b = map(int, input().split(' '))
	print(solution(a, b))
