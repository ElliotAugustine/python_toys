#피보나치 수열로 이루어진 사각형들의 변들의 합

def perimeter(n):
    s0, s1 = 1, 1
    for i in range(n):
        s1, s0 = s1 + s0, s1
    return 4 * (s1 + s0 - 1)



# cf : 일반적 피보나치
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#하지만 이 방법은 왼쪽 오른쪽이 엄청나게 반복되면서 연산낭비 심각 -> memoization!(검색)