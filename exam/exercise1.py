input=[7,5,7]
result=0
found=False
for index in range(len(input)):
    value=input[index]
    if value==7 and not found:
        result=index
        found=True
if found:
    print(result)
else:
     print("not found ")
