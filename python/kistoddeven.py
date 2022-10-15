def fltr_o_e(l):
    odds = []
    evens = []
    for i in l:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    otpt = [odds, evens]
    return otpt

nums = [1,2,3,4,5,6,7,8,9,33,55,2,43,65,78,99]
print(fltr_o_e(nums))
