def format_output(text, tab_count=1):
    tabs = "\t" * tab_count
    return text.replace('\n', f'\n{tabs}')