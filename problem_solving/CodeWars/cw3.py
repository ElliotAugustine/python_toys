# 문자열에서 A를 T, T를 A로, C를 G, G를 C로 바꾸는 함수
def dna_strand1(dna):
    dnadic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(dnadic[x] for x in dna)


def dna_strand2(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))
