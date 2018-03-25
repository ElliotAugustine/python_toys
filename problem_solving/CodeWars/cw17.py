# 피보나치 수열인데 음수에도 적용되고 백만번째 수도 정확하고 효율적으로 계산가능한 알고리즘
## http://mitpress.mit.edu/sicp/chapter1/node15.html 이거 참조(이 책 구해서 읽기!!)
### 위 페이지 내용은 exponentiation이라고 해서 단순 반복 계산을 지수적으로 줄이는 방법임. 예를 들어 a**n을 a**(n-1)*a로 하는 게 아니라 홀수/짝수로 나누어서 a**(n/2)*2이런 식으로.

# 1: 단순히 점화식 풀어서 계산 -> 정확도 문제로 실패(fractions모듈의 Fraction 함수도 이용했지만 무리수를 유리수로 근사하는 게 더 큰 오차를 낳는 듯)
from math import sqrt
def fib(n):
    ans = (1/sqrt(5))*(((1+sqrt(5))/2)**n - ((1-sqrt(5)) / 2)**n)
    return ans

# 2: 그냥 재귀식 -> 당연히 계산 폭발
fibdic = {0:0, 1:1}
def fib(n):
    if n > max(fibdic.keys()):
        fibdic[n] = fib(n - 1) + fib(n - 2)
    elif n < min(fibdic.keys()):
        fibdic[n] = fib(n + 2) - fib(n + 1)
    return fibdic[n]

# 3: 점화식 풀이에 exponentiation 적용 -> 정확성 문제 미해결
from math import sqrt
def fib(n):
    def g(k):
        gr = (1 + sqrt(5))/2
        if k == 0:
            return 1/sqrt(5)
        elif k%2 == 0:
            semi = g(k/2)**2*sqrt(5)
        else:
            semi = g((k-1)/2)**2*gr*sqrt(5)
        if k >= 25:
            semi = round(semi)
        return semi
    k = abs(n)
    ans = int(round(g(k)))
    if n < 0:
        ans *= (-1)**(k%2+1)
    return ans

# 최종 답안 ~ 행렬을 곱하는 방식에 exponentiation 적용
dic = {0: 0, 1: 1}
def fib(n):
    k = abs(n)
    if k not in dic.keys():
        if k%2 == 0:
            f, g = fib(k/2), fib(k/2-1)
            dic[k] = f**2 + 2*f*g
        elif k%2 == 1:
            h, i = fib((k+1)/2), fib((k-1)/2)
            dic[k] = h**2 + i**2
    ans = dic[k]
    if n < 0:
        ans *= (-1)**(k%2+1)
    return ans