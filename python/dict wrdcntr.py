def wrdcntr(strng):
    count = {}
    for char in strng:
        count[char] = strng.count(char)
    return count
print(wrdcntr('Manish'))
