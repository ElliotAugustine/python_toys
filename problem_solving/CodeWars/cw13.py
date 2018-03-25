def solution(n):
    dic = [('I','V'),('X','L'),('C','D'),('M','d'),'d']
    ans = []
    y = [int(z) for z in str(n)]
    y.reverse()
    for i, x in enumerate(y):
        m = dic[i][0]*(x%5//4) + dic[i+1][0]*(x//9) + dic[i][1]*((x%9+1)//5) + dic[i][0]*(x%5%4)
        ans.append(m)
    ans.reverse()
    return ''.join(ans)


def solution2(n):
    roman_numerals = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string