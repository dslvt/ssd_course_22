import random
from test_functions import func, funx, funh
from test_functions import quadratic_equation_solver
from test_functions import pascal_triangle_printer

from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4

import argparse

arg_parser = argparse.ArgumentParser(description='Assignemnt 1. SSD')

arg_parser.add_argument('-t1', '--run_task_1',
                        action=argparse.BooleanOptionalAction, default=True)
arg_parser.add_argument('-t2', '--run_task_2',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-t3', '--run_task_3',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-t4', '--run_task_4',
                        action=argparse.BooleanOptionalAction, default=False)


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


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


def task1():
    print('Running Task 1')

    func()
    funx()
    func()
    funx()
    func()


def task2():
    print('Running Task 2')

    funh(None, bar2="")


def task3():
    print('Running Task 3')


def task4():
    print('Running Task 4')


if __name__ == '__main__':
    args = arg_parser.parse_args()

    if args.run_task_1:
        task1()

    if args.run_task_2:
        task2()

    if args.run_task_3:
        task3()

    if args.run_task_4:
        task4()
