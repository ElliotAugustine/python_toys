# 알파벳 배열 중 없는 것 찾기
def find_missing_letter(chars):
    return [chr(x) for x in range(ord(chars[0]),ord(chars[-1])+1) if chr(x) not in chars][0]


def find_missing_letter2(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1])-1:
        n += 1
    return chr(ord(chars[n])+1)
    