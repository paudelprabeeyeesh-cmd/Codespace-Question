#!/usr/bin/env python3
"""
Question 6:
What is the difference between `list.append()` and `list.extend()`?
"""

def solve():
    """
    Both list.append() and list.extend() are used to add elements to a list,
    but they work differently:

    - list.append(x): Adds a single element x to the end of the list.
                       The element can be any type (int, str, list, etc.)
                       If x is a list, the entire list is added as one element.

    - list.extend(iterable): Extends the list by appending all elements
                              from the iterable (list, tuple, string, etc.).
                              Each element is added individually.
    """

    print("=== Example 1: append() with various types ===")
    lst = [1, 2, 3]
    print(f"Original list: {lst}")
    
    lst.append(4)
    print(f"After append(4): {lst}")
    
    lst.append([5, 6])
    print(f"After append([5,6]): {lst}")
    print(f"Length: {len(lst)}")
    
    lst.append("hello")
    print(f"After append('hello'): {lst}")
    print(f"Length: {len(lst)}")

    print("\n=== Example 2: extend() with various iterables ===")
    lst2 = [1, 2, 3]
    print(f"Original list: {lst2}")
    
    lst2.extend([4, 5])
    print(f"After extend([4,5]): {lst2}")
    
    lst2.extend((6, 7))
    print(f"After extend((6,7)): {lst2}")
    
    lst2.extend("abc")
    print(f"After extend('abc'): {lst2}")
    
    lst2.extend(range(3))
    print(f"After extend(range(3)): {lst2}")

    print("\n=== Example 3: append() vs extend() with list of lists ===")
    matrix = [[1, 2], [3, 4]]
    print(f"Original matrix: {matrix}")
    
    # append adds the entire list as one element
    matrix_append = [[1, 2], [3, 4]]
    matrix_append.append([5, 6])
    print(f"append([5,6]) result: {matrix_append}")
    print(f"Length: {len(matrix_append)}")
    
    # extend adds each element individually
    matrix_extend = [[1, 2], [3, 4]]
    matrix_extend.extend([5, 6])
    print(f"extend([5,6]) result: {matrix_extend}")
    print(f"Length: {len(matrix_extend)}")

    print("\n=== Example 4: Performance comparison (theoretical) ===")
    # append() is O(1) amortized
    # extend() is O(k) where k is the length of the iterable
    import timeit
    
    time_append = timeit.timeit(
        'lst = []; [lst.append(i) for i in range(1000)]',
        number=10000
    )
    time_extend = timeit.timeit(
        'lst = []; lst.extend(range(1000))',
        number=10000
    )
    
    print(f"Time for append in loop: {time_append:.6f} seconds")
    print(f"Time for extend with range: {time_extend:.6f} seconds")
    print("extend() is generally faster because it's implemented in C")

    print("\n=== Summary ===")
    summary = """
    append():
    - Adds a single element
    - If element is iterable, adds it as one item
    - O(1) amortized time complexity
    
    extend():
    - Adds multiple elements from an iterable
    - Each element from the iterable is added individually
    - O(k) where k is length of iterable
    - More efficient than using append in a loop
    """
    print(summary)

    return "See prints above for detailed comparison."

def test():
    result = solve()
    print(f"\nQ006: {result}")

if __name__ == "__main__":
    test()