def rev_el(l):
    el = []
    for i in l:
        el.append(i[::-1])
    return el

words = ['manish', 'kumar']
print(rev_el(words))
