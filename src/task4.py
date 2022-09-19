def decorator_4(func):
    def wrapper():
        print('Task 4')
        func()
    return wrapper