def cmnlst(l,m):
    olst = []
    for i in l:
        if i in m:
            olst.append(i)
    return olst

l1 = [3,4,5,6,7,2,0]
l2 = [22,5,44,65,8,79,0]
print(cmnlst(l1,l2))
