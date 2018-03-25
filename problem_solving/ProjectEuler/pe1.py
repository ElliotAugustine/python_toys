# 100이하 3과 5의 배수 합
def pe1(a, b):
    m = b//a
    return a*m*(m+1)/2


for i in range(2, 11):
    print(pe1(3, 10**i)+pe1(5, 10**i)-pe1(15, 10**i))