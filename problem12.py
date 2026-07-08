#!/usr/bin/env python3
"""
Question 12:
How does `__slots__` affect memory usage and attribute access?
"""

def solve():
    """
    __slots__ restricts attribute creation and reduces memory usage.
    It prevents __dict__ from being created for each instance.
    """
    import sys
    
    class WithoutSlots:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    class WithSlots:
        __slots__ = ['name', 'age']
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    # Create instances
    no_slots = WithoutSlots("Alice", 30)
    with_slots = WithSlots("Bob", 25)
    
    # Memory comparison
    print(f"Without __slots__: {sys.getsizeof(no_slots)} bytes")
    print(f"With __slots__: {sys.getsizeof(with_slots)} bytes")
    
    # Attribute access speed (approximate)
    print("\n=== Attribute Access ===")
    import timeit
    
    time_no_slots = timeit.timeit(
        'no_slots.name',
        globals={'no_slots': no_slots},
        number=1000000
    )
    time_with_slots = timeit.timeit(
        'with_slots.name',
        globals={'with_slots': with_slots},
        number=1000000
    )
    
    print(f"Without __slots__: {time_no_slots:.6f}s")
    print(f"With __slots__: {time_with_slots:.6f}s")
    
    print("\n=== Key Points ===")
    print("""
    1. __slots__ prevents creation of __dict__ and __weakref__
    2. Reduces memory usage significantly
    3. Slightly faster attribute access
    4. Cannot add new attributes not in __slots__
    5. Useful for classes with many instances
    """)
    
    # Attempt to add new attribute
    try:
        with_slots.city = "NYC"
    except AttributeError as e:
        print(f"\nCannot add new attribute: {e}")
    
    return "__slots__ saves memory by preventing __dict__ creation."

def test():
    result = solve()
    print(f"\nQ012: {result}")

if __name__ == "__main__":
    test()