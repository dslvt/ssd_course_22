import random
import time
from utils import print_header


def decorator_1(func):
    data = {'count': 0}

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        output = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        data['count'] += 1
        print(f'func call {data["count"]} executed in {total_time} sec')
        return output
    return wrapper


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)


@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


def run_task_1():
    print_header(1)

    func()
    funx(10, 15)
    func()
    funx(20)
    func()
