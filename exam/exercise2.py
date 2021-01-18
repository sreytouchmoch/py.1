input = [3, 7, 7]
result = 0
found = False
for index in range(len(input)):
    value = input[index]
    if value == 7:  #find the last
        result = index
        found = True

# Print result
if found:
    print(result)
else:
    print("not found")