def factorial(n) :
    fac = 1
    for i in range (n):
        fac = fac * (i +1)
        return fac
"""
program n: Integer
return : n * n-1 * n-2 * n-3 ..........1
"""

number = int(input("Enter then number"))
print(factorial_iterative(number))

# n! = n * n-1 * n-2 * n-3 .........1
# n! = n * (n-1)!