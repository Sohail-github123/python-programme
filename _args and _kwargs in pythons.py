#def function_name_print (a, b , c , d) :
 #   print(a , b , c , d)
def funargs(normal,*args,**kwargs):  #(args) as tuple , normal args first rakhenge
    #print(args[0])
    print(normal)
    for item in args :
        print(item)
    print("Now i would like to introduce some of heroes")
    for key, value in kwargs.items():
        print(f"{key}, {value} )
#function_name_print("Sohail","Akola","pycharm","skillf")
akola = ("Sohail","Akola","pycharm","skillf")
normal ="this is a normal"
kw = {"Sohail":"Akola","Harry":"Mumbai","The programmer":"Pune"}
funargs(normal,*akola, **kw)