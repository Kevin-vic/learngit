from random import randint
num = randint(1,101)
print("what's your name?")
you = input()
print("Oh,u are a %s" %you)
print("I'm a computer,let's play a game!")
print("guess what I think")
def bijiao(num1,num2):
    if num1 < num2:
        print("small!")
        return False
    if num1 > num2:
        print("big!")
        return False
    if num1 == num2:
        print("that's right")
        return True
yes = False
while yes == False:
    ans = int(input())
    bijiao(ans,num)



