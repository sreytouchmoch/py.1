listOfnumber = eval(input())
AllIndexof7=[]
for index in range (len(listOfnumber)):
    if listOfnumber[index]==7:
        AllIndexof7.append(index)
print(AllIndexof7)
