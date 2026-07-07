#!/usr/bin/env python3
"""
Question 7:
How do you reverse a string in Python?
"""

def solve():
    """
    There are multiple ways to reverse a string in Python:
    1. Slicing: s[::-1]
    2. reversed() + join: ''.join(reversed(s))
    3. Manual loop
    4. Recursion
    """
    
    s = "Hello World"
    
    print(f"Original: {s}")
    
    # Method 1: Slicing (most Pythonic)
    method1 = s[::-1]
    print(f"Slicing: {method1}")
    
    # Method 2: reversed() with join
    method2 = ''.join(reversed(s))
    print(f"reversed() + join: {method2}")
    
    # Method 3: Manual loop
    method3 = ""
    for char in s:
        method3 = char + method3
    print(f"Manual loop: {method3}")
    
    # Method 4: Using list reverse
    method4 = list(s)
    method4.reverse()
    method4 = ''.join(method4)
    print(f"List reverse: {method4}")
    
    # Method 5: Recursion
    def reverse_recursive(s):
        if len(s) <= 1:
            return s
        return s[-1] + reverse_recursive(s[:-1])
    
    method5 = reverse_recursive(s)
    print(f"Recursion: {method5}")
    
    # Method 6: Using reduce
    from functools import reduce
    method6 = reduce(lambda x, y: y + x, s)
    print(f"Reduce: {method6}")
    
    # Performance comparison
    import timeit
    
    print("\n=== Performance Comparison ===")
    large_str = "a" * 10000
    time_slice = timeit.timeit('large_str[::-1]', globals={'large_str': large_str}, number=1000)
    time_reversed = timeit.timeit('''''.join(reversed(large_str))''', globals={'large_str': large_str}, number=1000)
    
    print(f"Slicing: {time_slice:.6f} seconds")
    print(f"reversed() + join: {time_reversed:.6f} seconds")
    print("Slicing is the fastest and most Pythonic method.")
    
    return "Use s[::-1] for the fastest and most readable approach."

def test():
    result = solve()
    print(f"\nQ007: {result}")

if __name__ == "__main__":
    test()