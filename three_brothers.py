def solution(a, b):
    if a != 1 and b != 1:
        return 1
    elif a != 2 and b != 2:
        return 2
    else:
        return 3
    

a, b = map(int, input().split(' '))

print(solution(a, b))
