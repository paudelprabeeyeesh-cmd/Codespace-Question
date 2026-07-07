#!/usr/bin/env python3
"""
Question 8:
What is a decorator? Write a decorator that measures execution time.
"""

def solve():
    """
    A decorator is a function that takes another function as input,
    wraps it, adds functionality, and returns a new function.
    """
    
    import time
    import functools
    
    # Decorator to measure execution time
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"Function '{func.__name__}' took {elapsed:.6f} seconds to execute")
            return result
        return wrapper
    
    # Using the decorator
    @timer
    def slow_function():
        time.sleep(1)  # Simulate slow operation
        return "Done"
    
    @timer
    def fast_function():
        return sum(range(1000))
    
    print("Testing slow_function:")
    result1 = slow_function()
    print(f"Result: {result1}\n")
    
    print("Testing fast_function:")
    result2 = fast_function()
    print(f"Result: {result2}\n")
    
    # Decorator with arguments
    def repeat(n):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(n):
                    func(*args, **kwargs)
            return wrapper
        return decorator
    
    @repeat(3)
    def say_hello():
        print("Hello!")
    
    print("Decorator with argument (repeat 3 times):")
    say_hello()
    
    # Multiple decorators
    def uppercase(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result.upper()
        return wrapper
    
    @timer
    @uppercase
    def get_message():
        return "hello world"
    
    print("\nChained decorators (timer + uppercase):")
    print(get_message())
    
    return "Decorators are functions that modify other functions. Timer decorator shown above."

def test():
    result = solve()
    print(f"\nQ008: {result}")

if __name__ == "__main__":
    test()