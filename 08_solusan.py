########## function acceps any number of keyword argument print formed
########## kwargs #####

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="saktiman",power="leser")
print_kwargs(name="saktiman")
print_kwargs(name="saktiman",power="lazer",enemy="Dr.jackaal")