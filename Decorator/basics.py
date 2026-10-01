from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")

    return wrapper

@decorator
def greet():
    print("hello World")

greet()

print(greet.__name__)