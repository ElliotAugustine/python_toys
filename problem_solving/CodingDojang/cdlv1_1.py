# 100이하 3과 5의 배수 합
set1 = set(range(3, 1000, 3))
set2 = set(range(5, 1000, 5))
print(sum(set1|set2))