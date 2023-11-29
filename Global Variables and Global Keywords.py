# l = 10 # GLOBAL variable
#
# def function1 (n) :
#     #l = 5 #LOCAL VAR
#     m = 9 #LOCAL VAR
#     global l
#     l = 1 + 45
#     print(l,m)
#     print(n,"I have printed")
#
# function1("This is me ")
# print(l)

x=89
def sohail() :
    x = 20
    def akola () :
        global x    #x=89 golbal ko change karke x=88 kardenga
        x = 88
    #print("before calling akola()",x)
    akola()
    print("after calling akola()", x)
sohail()
print(x)