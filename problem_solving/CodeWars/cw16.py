# 리스트 들로 구성된 구조가 같은 리스트인지 여부 찾기

def same_structure_as(original,other):
    a = ''.join(x for x in str(original) if x in '[,]"\'').split('"')
    a = ''.join(a[i] for i in range(len(a)) if i%2 == 0).split("'")
    a = ''.join(a[i] for i in range(len(a)) if i%2 == 0)
    b = ''.join(x for x in str(other) if x in '[,]"\'').split('"')
    b = ''.join(b[i] for i in range(len(b)) if i%2 == 0).split("'")
    b = ''.join(b[i] for i in range(len(b)) if i%2 == 0)
    return a == b

def same_structure_as2(original,other):
    if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
        for o1, o2 in zip(original, other):
            if not same_structure_as2(o1, o2): return False
            else: return True
    else: return not isinstance(original, list) and not isinstance(other, list)