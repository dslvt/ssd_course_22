def decorator_2(func):
    def wrapper():
        print('Task 2')
        func()
    return wrapper