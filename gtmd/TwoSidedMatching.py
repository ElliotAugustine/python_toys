from random import randint, shuffle


def randex(minlen=20):
    # create two random group with members having preference list on the other goup
    # minlen : minimum length of preference list of one person
    b, g = tuple([chr(x) for x in range(97, 123)]), tuple([chr(y) for y in range(65, 91)])
    boys, girls = {}, {}
    for m in b:
        boys[m] = list(g)
        shuffle(boys[m])
        boys[m] = boys[m][:randint(minlen, 26)]
    for w in g:
        girls[w] = list(b)
        shuffle(girls[w])
        girls[w] = girls[w][:randint(minlen, 26)]
    return boys, girls


def blockcheck(match, boys, girls, r='B'):
    # check if the design is blocked or not
    # r = 'B' if the right part of each pair of the match(value) is boys
    f = match.pop('fail')
    if r != 'B':
        girls, boys = boys, girls
    rmat = {}
    newg = {}
    newb = {}
    for i in f:
        if i in girls.keys():
            newg[i] = girls[i]
        else:
            newb[i] = boys[i]
    for g in match.keys():
        newg[g] = girls[g][:girls[g].index(match[g])]
        rmat[match[g]] = g
    for b in rmat.keys():
        newb[b] = boys[b][:boys[b].index(rmat[b])]
    for w in newg.keys():
        for wm in newg[w]:
            if w in newb[wm]:
                return "Blocked"
    for m in newb.keys():
        for mw in newb[m]:
            if m in newg[mw]:
                return "Blocked"
    return "OK"
