import math
#- coding UTF-8 -#
print('计算任意的一元二次方程')
def eryuan(sum1,sum2,sum3):
    if sum2*sum2-4*sum1*sum3>=0:
        sq = math.sqrt(sum2*sum2-4*sum1*sum3)
        jieguo1 = (-sum2+sq)/(2*sum1)
        jieguo2 = (-sum2-sq)/(2*sum1)
        print("第一个解是",jieguo1,"第二个解是",jieguo2)
        return(jieguo1,jieguo2)
    else:
        print("无实数根")
        pass
    

print("请填写ax平方+bx+c的系数，依次填写a、b、c")
a = float(input())
b = float(input())
c = float(input())
print("a是",a)
print("b是",b)
print("c是",c)
eryuan(a,b,c)
print("输入任意字符，在按enter退出")
input()
