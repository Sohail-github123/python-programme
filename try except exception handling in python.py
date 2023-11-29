"""print("Enter num 1")
num1 = int(input())
print("Enter num 2")
num2 = int(input())
try:
    print("The sum of these two numbers is ", int (num1)+int(num2))

except Exception as e:
    print(e)

print("This line is very important") """

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error")