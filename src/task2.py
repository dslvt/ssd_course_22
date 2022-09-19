import time
import inspect
from contextlib import redirect_stdout
import io


def format_output(text):
    return text.replace('\n', '\n\t')


def decorator_2(func):
    count_data = {'count': 0}

    def wrapper(*args, **kwargs):
        count_data['count'] += 1
        data = {'Name': f'\t{func.__name__}',
                'Type': f'\t{type(func)}',
                'Sign': f'\t{inspect.signature(func)}',
                'Args': f'\tpositional {args}\n\tkeyworded {kwargs}',
                'Doc': f'\t{func.__doc__}',
                'Source': inspect.getsource(func)}

        with redirect_stdout(io.StringIO()) as f:

            start_time = time.perf_counter()
            func(*args, **kwargs)
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
