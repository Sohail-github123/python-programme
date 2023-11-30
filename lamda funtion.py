# # Lambda funtion or Anonymus function
#
# def add(a,b):
#     return a+b
# #minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9,4))

def a_first(a):
    return a[1]
a = [[1,14],[5,6],[8,23]]
a.sort(key=a_first)
print(a)

# if we take 1 it will sort 1 th position of all list we use sort func
# if we take a[0] it will sort o th position of all list we use sort funtion in this
# eg a[0]=1 a[1]=14
# eg a[0] ------[[1,-], [5,-], [8, -]
# eg a[1] ------[-, 6],[-, 14],[-, 23]
