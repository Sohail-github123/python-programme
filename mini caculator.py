print("<< mini caculator >>")
num1 = float (input("enter first number here: "))
num2 = float (input("enter second number here: "))
print ("press 1 for addition \n press 2 for substraction \n press 3 for multiplication \n press 4 for division")
choice = int (input("enter your choice from 1-4: "))
if choice == 1:
    print ("Addition of two number is", num1 + num2 )
elif choice == 2 :
   print ("subsstraction of two number is", num1 - num2 )
elif choice == 3 :
    print ("subsstraction of two number is", num1 * num2 )
elif choice == 4 :
    print ("subsstraction of two number is", num1 / num2 )
else:
    print ("invalid input" )