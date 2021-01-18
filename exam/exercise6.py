input = ["jonathan", "rady"]

countGoodNames = 0
for name in input:
    nameSize = len(name)

    if nameSize >= 4 and nameSize <= 6:
        countGoodNames += 1

if countGoodNames == len(input):
    print("GOOD")
else:
    print("BAD")