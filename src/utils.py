import time


def format_output(text, tab_count=1):
    tabs = "\t" * tab_count
    return text.replace('\n', f'\n{tabs}')


def print_header(task_num):
    print('')
    print(f'Running task {task_num}...')


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        output = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        return output, total_time
    return wrapper
