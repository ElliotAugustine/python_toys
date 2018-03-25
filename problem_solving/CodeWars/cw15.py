# cw14에서 알 수 있듯이 원래 피보나치 계산하는 방식은 비효율적, 따라서 메모이제이션을 이용해서 캐시 데이터에 저장하면서 이미 계산한 것은 찾을 수 있도록, 동시에 재귀함수는 계속 이용하도록 설계
fibdic = {1: 1, 2: 1}
def fibonacci(n):
    if n not in fibdic.keys():
        fibdic[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibdic[n]


# 혹은
def fibonacci2(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# 혹은
def fibonacci3(m):
    cache = {1: 1, 2: 1}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1)+fib(n-2)
        return cache[n]
    return fib(m)


# 결국 그냥 다 각자 계산시키는 것보다 하나의 공통된 메모리를 설정해서 중복되는 것 제외하고 하는 게 효율적