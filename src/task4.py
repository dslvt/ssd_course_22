import inspect
import io
import time
from contextlib import redirect_stdout
from datetime import datetime
import random

import pandas as pd

from utils import format_output, print_header, time_decorator


class decorator_4:
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.name = func.__name__
        self.type = type(func)
        self.sign = inspect.signature(func)
        self.args = None
        self.doc = func.__doc__
        self.source = inspect.getsource(func)
        self.time_output = None

    def __call__(self, *args, **kwds):
        self.count += 1

        try:
            with redirect_stdout(io.StringIO()) as f:
                start_time = time.perf_counter()
                self.func(*args, **kwds)
                total_time = time.perf_counter() - start_time

            self.time_output = f'func call {self.count} executed in {total_time} sec'
            self.output = f.getvalue()
            self.args = (args, kwds)

            self.dump_output()
            return self.output
        except Exception as e:
            file_name = 'output/task4_error_log.txt'
            timestamp = datetime.now()
            with open(file_name, 'a') as f:
                f.write(f'{timestamp} | {str(e)}\n')

    def dump_output(self):
        data = {'Name': f'\t{self.name}',
                'Type': f'\t{self.type}',
                'Sign': f'\t{self.sign}',
                'Args': f'\tpositional {self.args[0]}\n\t\tkeyworded {self.args[1]}',
                'Doc': f'\t{format_output(f"{self.doc.lstrip()}")}',
                'Source': format_output(self.source, 2),
                'Output': format_output(self.output, 2)}

        file_name = f'output/t4 {self.name} {datetime.now()}.txt'
        with open(file_name, 'x') as f:
            f.write(f'{self.time_output}\n')
            for k, v in data.items():
                f.write(f'{k}: {v}\n')


def funt_builder(sec):
    def funt(bar1, bar2=10):
        """
        This function does something useful
        :param bar1: description
        :param bar2: description
        """
        if random.random() > 0.5:
            raise Exception('Some error')
        time.sleep(sec)
        print("some\nmultiline\noutput")

    funt.__name__ = f'funt_{int(sec * 1000)}'
    funt = time_decorator(decorator_4(funt))
    funt.__name__ = f'funt_{int(sec * 1000)}'
    return funt


def run_task_4():
    print_header(4)

    exec_times = []
    functions = [funt_builder(1),
                 funt_builder(0.5),
                 funt_builder(0.1),
                 funt_builder(0.25)]

    for fn in functions:
        _, sec = fn(10)
        exec_times.append((fn.__name__, sec))

    exec_times_df = pd.DataFrame(
        exec_times, columns=['PROGRAM', 'TIME ELAPSED'])
    exec_times_df = exec_times_df.sort_values(
        by=['TIME ELAPSED'], ascending=True)
    exec_times_df['RANK'] = list(range(1, len(functions) + 1))
    columns_titles = ['PROGRAM', 'RANK', 'TIME ELAPSED']
    exec_times_df = exec_times_df.reindex(columns=columns_titles)
    exec_times_df.reset_index(inplace=True)

    print(exec_times_df)
