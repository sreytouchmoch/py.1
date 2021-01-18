found72=False

number=0
while not found72 and number!=3:
    list=int(input())
    number=number+1
    if list!=72:
        print("again")
    if list==72:
        print("win")
        found72=True
    elif number==3:
        print("lost")
