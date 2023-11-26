#list functions

languages=["python","c++","c#",".net",100]
print(languages)
numbers = [2,13,4,15,6]
#numbers.sort()
numbers.reverse()
#print(numbers[2])
#print(numbers[:5])
print(numbers[0:5])
#numbers.append(333)
#numbers.insert(2, 55)
numbers.insert(1,99)
numbers.remove(99)
numbers.pop()
print(numbers)
numbers[1]=98
print(numbers)
#tupples
#tupples is immutable we will not change it value
tp=(1,2,3,4)
print(tp)
a=1
b=2
a,b = b,a
print(a,b)