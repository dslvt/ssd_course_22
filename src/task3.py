def decorator_3(func):
    def wrapper():
        print('Task 3')
        func()
    return wrapper


def run_task_3():
    pass
