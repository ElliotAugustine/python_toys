# 앞 리스트에서 뒤 리스트 요소 제거하는 함수
def array_diff1(a, b):
    return list(filter(lambda x: x not in b, a))


def array_diff2(a, b):
    return [x for x in a if x not in b]