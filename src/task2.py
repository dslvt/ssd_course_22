def decorator_2(func):
    def wrapper():
        print('Task 2')
        func()
    return wrapper


def run_task_2():
    pass
