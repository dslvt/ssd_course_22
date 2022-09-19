import random
from cmath import sqrt


def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)


def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


def funh(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


quadratic_equation_solver = lambda a, b, c: (
    (-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

# took from https://stackoverflow.com/questions/65431561/pascal-tringle-using-lambda-without-variables-or-recursion
pascal_triangle_printer = lambda x: [
    (lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(x)]
