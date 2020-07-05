from random import randint
num = randint(0,101)
a = "it's a number"
print(a)
print("do u know")
print("u must guess a number!")
print("it's from 1 to 100")
b = False
while b == False:
    answer = int(input())
    if answer < num:
        print("too small")
    elif answer > num:
        print("too big")
    else:
        print("yes,right")
        b = True
input()
print("byebye!")