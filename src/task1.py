def decorator_1(func):
    def wrapper():
        print('Task 1')
        func()
    return wrapper