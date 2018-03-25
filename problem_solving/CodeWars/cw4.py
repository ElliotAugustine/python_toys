# 문장에서 각 단어의 첫 글자만 대문자로 바꾸기
def toJadenCase(string):
    return " ".join(x.capitalize() for x in string.split())
