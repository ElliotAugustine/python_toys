# 각 단어 제일 앞 알파벳을 단어 뒤로 보내고 ay를 붙임 구두점은 제외
def pig_it(text):
	return ' '.join(x[1:]+x[0]+'ay' if x.isalpha() else x for x in text.split())