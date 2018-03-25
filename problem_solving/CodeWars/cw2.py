# a, b 사이 모든 정수의 합(a,b 포함)
def get_sum1(a, b):
    return sum(range(min(a,b), max(a,b)+1))


def get_sum2(a, b):
    return (a+b)*(abs(a-b)+1)/2
