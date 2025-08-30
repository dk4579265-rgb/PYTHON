#########  USER KP GREET 


def greet(name):
    return "Hello,"+ name +"!"

print(greet("chai"))                        # hello chai

 
        OR

def greet(name="user"):
    return "hello,"+name+"!"


print(greet())                          ## hello user !