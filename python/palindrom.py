def plindrm(str):
    if str == str[::-1]:
        return True
    return False

print(plindrm("manish"))
print(plindrm("ava"))
