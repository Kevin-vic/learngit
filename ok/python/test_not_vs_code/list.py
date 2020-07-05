l = [100,1024,"How are u?","everyday"]
def bijiao(num1,num2):
    if num1>num2:
        print(num1)
        print("is bigger than")
        print(num2)
    elif num1<num2 :
        print(num1)
        print("is smaller than")
        print(num2)
    else:
        print("the same!")
bijiao(l[0],l[1])
print(l)
print("0,1 de bi jiao")
input()