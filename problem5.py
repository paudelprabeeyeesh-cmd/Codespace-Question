#!/usr/bin/env python3
"""
Question 5:
How does `range` work? Is it a generator or a sequence?
"""

def solve():
    """
    range() is a built-in function that returns an immutable sequence of numbers.
    It is NOT a generator; it is a sequence type that supports:
    - indexing (__getitem__)
    - length (__len__)
    - membership (__contains__)
    - slicing (returns a new range)

    However, range is lazy: it doesn't create the entire list in memory; it computes
    values on demand when iterating. This gives it memory efficiency similar to a generator,
    but it is technically a sequence because it supports the sequence protocol.

    You can create a range with:
    - range(stop)            -> 0 to stop-1
    - range(start, stop)     -> start to stop-1
    - range(start, stop, step) -> start to stop-1 with step
    """

    print("=== Example 1: Basic usage ===")
    r = range(5)
    print(f"range(5) = {r}")
    print(f"list(r) = {list(r)}")
    print(f"len(r) = {len(r)}")
    print(f"r[2] = {r[2]}")
    print(f"3 in r = {3 in r}")
    print(f"6 in r = {6 in r}")

    print("\n=== Example 2: Start and stop ===")
    r2 = range(2, 8)
    print(f"range(2,8) = {list(r2)}")

    print("\n=== Example 3: Step ===")
    r3 = range(0, 10, 2)
    print(f"range(0,10,2) = {list(r3)}")

    print("\n=== Example 4: Negative step ===")
    r4 = range(10, 0, -2)
    print(f"range(10,0,-2) = {list(r4)}")

    print("\n=== Example 5: Slicing (returns a new range) ===")
    r5 = range(0, 100, 3)
    sliced = r5[5:15]   # slice returns a range object
    print(f"r5 = {list(r5)[:20]}...")
    print(f"r5[5:15] = {list(sliced)}")

    print("\n=== Example 6: Checking if it's a generator ===")
    import types
    print(f"Is range a generator? {isinstance(r, types.GeneratorType)}")
    print(f"Is range an iterator? {hasattr(r, '__next__')}")  # It is iterable but not its own iterator
    print(f"Is range a sequence? {hasattr(r, '__getitem__') and hasattr(r, '__len__')}")  # True

    print("\n=== Example 7: Memory efficiency ===")
    import sys
    big_range = range(1000000)
    big_list = list(range(1000000))
    print(f"Memory of range: {sys.getsizeof(big_range)} bytes")
    print(f"Memory of list: {sys.getsizeof(big_list)} bytes")

    return "range is a lazy immutable sequence, not a generator. It supports sequence operations without storing all elements."

def test():
    result = solve()
    print(f"\nQ005: {result}")

if __name__ == "__main__":
    test()
    