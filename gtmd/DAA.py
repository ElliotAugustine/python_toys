from copy import deepcopy
from pandas import DataFrame


def df_to_listdict(df):
    # change input DataFrame into a dictionary with list values
    dic = {}
    for k in df.columns:
        dic[k] = list(df[k])
    return dic


def daa(boys, girls, f='B'):
    # Deferred Acceptance Algorithm
    # 'boys' and 'girls' should be dictionaries with list values
    # f = 'B' if boys move first, or f should be 'G'
    match = {}
    fa = []
    if f != 'B':
        boys, girls = girls, boys
    first, second = deepcopy(boys), deepcopy(girls)
    for g in second.keys():
        match[g] = None
    movlist = list(first.keys())
    while movlist:
        prelist = []
        for mov in movlist:
            if len(first[mov]) == 0:
                continue
            hom = first[mov][0]
            if mov in second[hom]:
                second[hom] = second[hom][:second[hom].index(mov)+1]
                if match[hom] and match[hom] != mov:
                    prelist.append(match[hom])
                match[hom] = mov
            else:
                prelist.append(mov)
            first[mov].remove(hom)
        movlist = deepcopy(prelist)
    for b in boys.keys():
        if b not in match.values():
            fa.append(b)
    for g in girls.keys():
        if not match[g]:
            match.pop(g)
            fa.append(g)
    match['fail'] = fa
    return match


def matchshow(match, r='B'):
    if r != 'B':
        n = {}
        for v in match.keys():
            n[match[v]] = v
        match = n
    m = DataFrame({'boy': list(match.values()), 'girl': list(match.keys())})
    return m.transpose()


if __name__ == "__main__":
    # test daa with boys starting and girls starting 10 times each and check the stability
    from TwoSidedMatching import randex, blockcheck
    for i in range(10):
        boys, girls = randex()
        bmat = daa(boys, girls)
        bok = blockcheck(bmat, boys, girls)
        bshow = matchshow(bmat)
        gmat = daa(boys, girls, 'G')
        gok = blockcheck(gmat, boys, girls, 'G')
        gshow = matchshow(gmat, 'G')
        print("No.{}\nBOYS START:\n{}\nSTABLE? : {}\n\nGIRLS START:\n{}\nSTABLE? : {}\n\n\n\n".format(
            i+1, bshow, bok, gshow, gok))
