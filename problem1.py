#!/usr/bin/env python3
"""
# Question 1:
# What is the difference between 'is' and '=='? When should you use each?
"""

def solve():
    """
    Explanation:
    - '==' checks value equality: whether two objects have the same content.
    - 'is' checks identity equality: whether two variables refer to the exact same object in memory.
    
    Use '==' for value comparisons (most cases: strings, numbers, lists, dicts).
    Use 'is' for identity checks with None, True, False, and other singletons.
    """
    
    # Example 1: Value vs Identity
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    # Value equality
    print(a == b)  # True – because they have the same elements
    print(a == c)  # True – same content
    
    # Identity equality
    print(a is b)  # False – they are different objects in memory
    print(a is c)  # True – c points to the same object as a
    
    # Example 2: None check (correct usage)
    x = None
    if x is None:   # preferred
        print("x is None")
    
    # Example 3: Comparing numbers (use ==)
    num1 = 100
    num2 = 100
    print(num1 == num2)  # True
    # num1 is num2 might be True for small integers but not guaranteed; avoid
    
    # Example 4: String interning (don't rely on it)
    s1 = "hello"
    s2 = "hello"
    print(s1 == s2)  # True
    print(s1 is s2)  # May be True due to interning, but not reliable for all strings
    
    return "See prints above for detailed examples."

def test():
    result = solve()
    print(f"Q001: {result}")

if __name__ == "__main__":
    test()