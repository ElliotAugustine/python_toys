# 스마일 개수 세기
# 스마일 시작은 반드시 :아니면;
# 코는 없거나 있다면 -아니면~
# 입은 )아니면D
# 얼굴 순서는 항상 일정
def count_smileys(arr):
    return len([x for x in arr if x[0] in ':;' and x[1:] in '-)~)-D~D'])