import inspect
import io
import time
from contextlib import redirect_stdout

from utils import format_output


def decorator_2(func):
    count_data = {'count': 0}

    def wrapper(*args, **kwds):
        count_data['count'] += 1
        data = {'Name': f'\t{func.__name__}',
                'Type': f'\t{type(func)}',
                'Sign': f'\t{inspect.signature(func)}',
                'Args': f'\tpositional {args}\n\tkeyworded {kwds}',
                'Doc': f'\t{func.__doc__}',
                'Source': inspect.getsource(func)}

        with redirect_stdout(io.StringIO()) as f:

            start_time = time.perf_counter()
            func(*args, **kwds)
            total_time = time.perf_counter() - start_time

        output = f.getvalue()

        data['Output'] = format_output(output)
        data['Doc'] = format_output(f"{data['Doc'].lstrip()}")
        data['Doc'] = f"\t{data['Doc']}"
        data['Source'] = format_output(data['Source'])

        print(
            f'{data["Name"]} call {count_data["count"]} executed in {total_time} sec'.strip())

        for k, v in data.items():
            print(f'{k}: {v}')

        return data['Output']
    return wrapper


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


def run_task_2():
    funh(None, bar2="")
