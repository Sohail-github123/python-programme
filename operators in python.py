#operators in python
#********************
#Arithmatic operator
#Assignment operator
#comparison operator
#Logical operator
#Identity operator
#membership operator
#Bitwise operator

#Arithmatic operator
print("5 + 6 is " ,5+6)
print("5 - 6 is " ,5-6)
print("5 * 6 is " ,5*6)
print("5 / 6 is " ,5/6)
print("5 ** 2 is " ,5**2)
print("5 % 5 is " ,5%5)
print("15 // 6 is " ,15//6)  #flor division oprator

#Assignment operator
x = 5
print(x)
x +=5
print(x)
x -=2
print(x)
x /=4
print(x)
x **=2
print(x)

#comparison operator
i = 5
print(i>=5)   #( not equal to != ,  equal to == , >= ,<= ,and,or)

#Logical operator
a= True
b= False
print(a and b)
#print(a and a)
#print(a or b)
#print(b and b)

#Identity operator
a = True
b = False
print(a is b)
#print(5 is  5)
#print(a is not b)
#print(5 is not 5)

#membership operator

list = [1,5,6,88,33,44,11,66]
print(66 in list)
print(88 not in list)

#Bitwise operators
#0 - 00
#1 - 01
#2 - 10
#3 - 11
print(0 & 1) #and
print(0 | 1) #or
