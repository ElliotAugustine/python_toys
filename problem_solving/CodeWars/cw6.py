# 알파벳이 중복되는 두 리스트를 넣어서 두 리스트에 있는 모든 글자들이 중복되지 않도록 순서대로 나열된 리스트 반환
def longest(s1, s2):
	return ''.join(sorted(set(s1)|set(s2)))