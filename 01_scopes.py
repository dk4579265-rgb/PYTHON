######### ##########

username ="chaiaurcode" 
def fun():
    #username ="chai"
    print(username)
    
print(username)        ##### ou==chaiurcode    ,  chaiurcode
fun() 
    
#################################

x=99

def fun2(y):   
    z=x+y
    return z
result = fun2(1)
print(fun2(1))                    # 100

#################################

x= 99
def func3():
    global x
    x=88
    
func3()    
print(x)                         # 88 
############################

x=99

def f1():
    x=88
    
    def f2():
        print(x)
    return f2

myResult=f1()
myResult()
 ###################################
 
x=99

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual



f = chaicoder(2)
g = chaicoder(3)

print(f(3))                 #9
print(g(3))                  # 27
     
 
   