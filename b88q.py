import math
num1,num2=map(int,input().split())
num3=math.gcd(num1,num2)
print((num1*num2)//num3)
