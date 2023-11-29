a = 9
b = 8
#c = sum((a, b))   # Built in function
#print(c)

#def function1():
#    print("Hello you are in function 1")

#function1()

def function1(a,b):
    print("hello you are in funtion 1",a+b)

def function2(a,b):
    '''this is a function for calculate avg THIS IS DOCSTRING'''
    average = (a+b)/2
    return average
v = function2(5,7)
print(v)
print(function2.__doc__ )
