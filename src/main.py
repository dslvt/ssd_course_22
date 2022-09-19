import argparse

from task1 import run_task_1
from task2 import run_task_2
from task3 import run_task_3
from task4 import run_task_4

arg_parser = argparse.ArgumentParser(description='SSD Assignemnt 1')
arg_parser.add_argument('-t1', '--run_task_1',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-t2', '--run_task_2',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-t3', '--run_task_3',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-t4', '--run_task_4',
                        action=argparse.BooleanOptionalAction, default=False)
arg_parser.add_argument('-a', '--run_all',
                        action=argparse.BooleanOptionalAction, default=False)


quadratic_equation_solver = lambda x: print(x)
pascal_triangle_printer = lambda x: print(x)

if __name__ == '__main__':
    args = arg_parser.parse_args()

    if args.run_task_1 or args.run_all:
        run_task_1()

    if args.run_task_2 or args.run_all:
        run_task_2()

    if args.run_task_3 or args.run_all:
        run_task_3()

    if args.run_task_4 or args.run_all:
        run_task_4()
