#!/usr/bin/env python3
"""
Question 4:
Explain the use of `*args` and `**kwargs` in function definitions.
"""

def solve():
    """
    *args and **kwargs allow a function to accept a variable number of arguments.

    - *args collects extra positional arguments as a tuple.
    - **kwargs collects extra keyword arguments as a dictionary.

    They are useful for:
    - Creating flexible functions that can accept any number of arguments.
    - Passing arguments to other functions without knowing them in advance.
    - Decorators, wrappers, and generic functions.

    The names "args" and "kwargs" are conventional but not required.
    The important parts are the single (*) and double (**) asterisks.
    """

    print("=== Example 1: *args ===")
    def sum_all(*args):
        return sum(args)  # args is a tuple of all positional arguments

    print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
    print(f"sum_all(10, 20, 30, 40) = {sum_all(10, 20, 30, 40)}")

    print("\n=== Example 2: **kwargs ===")
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print("print_info(name='Alice', age=30):")
    print_info(name='Alice', age=30)

    print("\n=== Example 3: Combining positional, *args, **kwargs ===")
    def func(a, b, *args, **kwargs):
        print(f"a = {a}, b = {b}")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")

    func(1, 2, 3, 4, 5, x=10, y=20)

    print("\n=== Example 4: Unpacking arguments ===")
    def add(a, b, c):
        return a + b + c

    numbers = [1, 2, 3]
    print(f"Unpacking list: add(*numbers) = {add(*numbers)}")

    data = {'a': 5, 'b': 10, 'c': 15}
    print(f"Unpacking dict: add(**data) = {add(**data)}")

    print("\n=== Example 5: Forwarding arguments to another function ===")
    def wrapper(*args, **kwargs):
        print("Wrapper got:", args, kwargs)
        # Forward to another function
        return sum(*args) if args else None

    print(f"wrapper(1, 2, 3) = {wrapper(1, 2, 3)}")

    return "See prints above for examples of *args and **kwargs usage."

def test():
    result = solve()
    print(f"\nQ004: {result}")

if __name__ == "__main__":
    test()