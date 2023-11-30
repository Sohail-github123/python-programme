def factorial_iterative(n) :
     fac = 1
     for i in range (n):
         fac = fac * (i+1)
     return fac
"""
program n: Integer
return : n * n-1 * n-2 * n-3 ..........1
"""
def factorial_recursive (n):
   if  n ==1:
        return 1

   else:
        return n * factorial_recursive(n-1)
   # 5 * factorial_recursive(4)
   # 5 * 4 /* factorial_recursive(1)
   # 5 * 4 * 3 * factorial_recursive(1)
   # 5 * 4 * 3 * 2 * factorial_recursive(1)
   # 5 * 4 * 3 * 2 * 1 factorial_recursive(1)
   # 5 * 4 * 3 * 2 * 1 = 120

number = int(input("Enter the number"))
print("Factorial Using Iterative Method ", factorial_iterative(number))
print("Factorial Using Recursive Method ", factorial_recursive(number))

# n! = n * n-1 * n-2 * n-3 .........1
# n! = n * (n-1)!

# 0 1 1 2 3 5 8 13 21
def fabonacci (n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)
number = int(input("Enter the number"))
print(fabonacci(number))