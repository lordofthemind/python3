def listcnt(l):
    lcnt = 0
    for i in l:
        if type(i) == list:
            lcnt += 1

    return lcnt

lst = [1,2,3,[1,2,3,4],[5,6,3,4,5],4,5,[5,6,7,8,9]]
print(listcnt(lst))
