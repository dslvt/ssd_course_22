import inspect
from datetime import datetime
import time
from contextlib import redirect_stdout
import io
from utils import format_output


class decorator_3:
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.name = func.__name__
        self.type = type(func)
        self.sign = inspect.signature(func)
        self.args = None
        self.doc = func.__doc__
        self.source = inspect.getsource(func)

    def __call__(self, *args, **kwds):
        self.count += 1
        with redirect_stdout(io.StringIO()) as f:
            start_time = time.perf_counter()
            self.func(*args, **kwds)
            total_time = time.perf_counter() - start_time

        self.output = f.getvalue()
        self.args = (args, kwds)

        print(f'func call {self.count} executed in {total_time} sec')
        self.dump_output()

    def dump_output(self):
        data = {'Name': f'\t{self.name}',
                'Type': f'\t{self.type}',
                'Sign': f'\t{self.sign}',
                'Args': f'\tpositional {self.args[0]}\n\t\tkeyworded {self.args[1]}',
                'Doc': f'\t{format_output(f"{self.doc.lstrip()}")}',
                'Source': format_output(self.source, 2),
                'Output': format_output(self.output, 2)}

        file_name = f'output/{datetime.now()}.txt'
        with open(file_name, 'x') as f:
            for k, v in data.items():
                f.write(f'{k}: {v}\n')


@decorator_3
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


def run_task_3():
    pass