# 소수 여부 판단
def is_prime(num):
    if num <= 3:
        return num >= 2
    for i in range(2, int(num**(.5))+1):
        if num%i == 0:
            return False
    return True


def is_prime1(num):
    return num > 1 and not any(num % n == 0 for n in range(2,int(num**(.5))+1))