# 일반 번호키가 있다. 특정하게 추측된 숫자배열을 제시하면 각 숫자들은 번호키 상 상하좌우의 다른 숫자일 가능성이 있다. 그럴 때 가능한 모든 숫자배열의 리스트.
def get_pins(observed):
    cod = ('08', '124', '1235', '236', '1457', '24568', '3569', '478', '05789', '689')
    ans = ['']
    for i in observed:
        ans = [x + k for x in ans for k in cod[int(i)]]
    return ans