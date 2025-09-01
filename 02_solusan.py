def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ','.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)  # Fixed typo here
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="hanji")


"""######## output############
calling: hello with args  and kwargs 
hello
calling: greet with args chai and kwargs greeting=hanji
hanji, chai  """