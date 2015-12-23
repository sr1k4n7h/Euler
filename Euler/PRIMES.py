__author__ = 'srikanth'

import math

lim = input("LIMIT :")
sqrtlim = math.sqrt(float(lim))
pp = 2
ss = [pp]
ep = [pp]
pp += 1
rss = [ss[0]]
tp = [pp]
i=0
rss.append(rss[i] * tp[0])
xp = []
pp += ss[0]
npp = pp
tp.append(npp)
while npp < int(lim):
    i += 1
    while npp < rss[i] + 1:
        for n in ss:
            npp = pp + n
            if npp > int(lim): break
            if npp <= rss[i] + 1: pp = npp
            sqrtnpp = math.sqrt(npp)
            test = True
            for q in tp:
                if sqrtnpp < q:
                    break
                elif npp % q == 0:
                    test = False
                    break
            if test:
                if npp <= sqrtlim:
                    tp.append(npp)
                else:
                    xp.append(npp)
        if npp > int(lim): break
    if npp > int(lim): break
    lrpp = pp
    nss = []
    while pp < (rss[i] + 1) * 2 - 1:
        for n in ss:
            npp = pp + n
            if npp > int(lim): break
            sqrtnpp = math.sqrt(npp)
            test = True
            for q in tp:
                if sqrtnpp < q:
                    break
                elif npp % q == 0:
                    test = False
                    break
            if test:
                if npp <= sqrtlim:
                    tp.append(npp)
                else:
                    xp.append(npp)
            if npp % tp[0] != 0:
                nss.append(npp - lrpp)
                lrpp = npp
            pp = npp
        if npp > int(lim): break
    if npp > int(lim): break
    ss = nss
    ep.append(tp[0])
    del tp[0]
    rss.append(rss[i] * tp[0])
    npp = lrpp
ep.reverse()
[tp.insert(0, a) for a in ep]
tp.reverse()
[xp.insert(0, a) for a in tp]

#
# def trunn(n):
#     l = len(n)
#     flag = True
#     for i in range(1, l):
#         n1 = n[:-i]
#         n2 = n[i:]
#         # print(n1,n2)
#         if int(n1) not in xp:
#             flag = False
#             return flag
#         if int(n2) not in xp:
#             flag = False
#             return flag
#     return flag
#
#
# TR = []
#
# for j in xp[4:]:
#     if trunn(str(j)):
#         TR.append(j)
#
# print(TR)

def rot(n):
    l = len(n)
    flag = True
    # A = []
    for step in range(l):
        n = n[l - 1] + n[0:l - 1]
        if int(n) not in xp:
            flag = False
            break
        # A.append(n)
    return flag
CP = []
for i in xp:
    if rot(str(i)):
        CP.append(i)

print(CP)