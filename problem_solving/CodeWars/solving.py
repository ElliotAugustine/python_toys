comdic = {1:[[1]]}
def combos(n):
    if n in comdic.keys():
        ans = comdic[n]
    else:
        ans = []
        for k in range(1, n):
            ans + [[k] + c for c in combos(n-k) if c[0] >= k]
        comdic[n]
    return ans