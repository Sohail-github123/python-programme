# F Strings
import math

me ="sohail"
#a = "this is me %s"%me
a1 = 3
#a = "this is me %s%s"%(me , a1)
#a = "This is {}{}"
#b = a.format(me, a1)
#print(b)
a =f"this is {me} {a1} {3*4}  {math.cos(0)}  {math.sin(0)}"
print(a)