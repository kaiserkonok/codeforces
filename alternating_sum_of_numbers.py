def solution(numbers):
	plus = True
	sum = 0

	for number in numbers:
		if plus:
			sum += number
			plus = False
		else:
			sum -= number
			plus = True


	return sum



n_tests = int(input())

for _ in range(n_tests):
	n_input = int(input())
	numbers = map(int, input().split(' '))
	print(solution(numbers))