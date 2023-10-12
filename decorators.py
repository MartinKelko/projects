"""def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

# print_name = start_end_decorator(print_name)

result = add5(10)
print(result)"""

def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World!")

# Call the decorated function
say_hello()
