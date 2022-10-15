strnum = input("Enter more than 2 digit number: ")
tot = 0
i = 0
while i < len(strnum):
    tot += int(strnum[i])
    i += 1
print(tot)
