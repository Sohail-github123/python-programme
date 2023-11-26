"""variables,Datatypes,Typecasting"""
var1 = "this is line one"
var2 = '2'
var3 =4.2
print(type(var3))
print(int(var2)+var3)
#only same type values are combined int+int
# typecasting str() int() float()
print(var1 + str(var2))
print(var2 + var1)
# multiply
print(100* var3)
# to print 100 times
print(10* var1)
print(10 * "hello\n")
print(10* int(var2)+var3)
# input function
print("Enter your number")
inpnum = input()
print("you entered",int(inpnum) +10)
# input function input number as a string convert into integer
print('enter first number')
n1 = input()
print('enter second number')
n2 = input()
print("sumof two number is",int(n1)+int(n2))