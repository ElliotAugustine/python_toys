# n팩토리얼의 마지막 0 개수

def zeros(n):
    i = 0
    while n//5:
        i += n//5
        n = n//5
    return i


def zeros2(n):
	return n//5 + zeros2(n//5) if n//5 else 0