#!/usr/bin/env python3
"""
Question 2:
How does Python handle memory management? Explain reference counting and garbage collection.
"""

def solve():
    """
    Python uses automatic memory management with two main mechanisms:
    1. Reference counting – each object keeps a count of references to it.
       When the count drops to zero, the object is deallocated immediately.
    2. Garbage collection (GC) – a cyclic garbage collector detects and cleans up
       objects that reference each other (cycles) which cannot be freed by reference counting alone.
    """
    
    print("=== Reference Counting Example ===")
    # Create an object and track references
    import sys
    
    class MyObject:
        def __init__(self, name):
            self.name = name
        def __del__(self):
            print(f"Deleting {self.name}")
    
    # Create object
    obj = MyObject("obj1")
    ref_count = sys.getrefcount(obj)  # includes temporary reference
    print(f"Initial reference count: {ref_count}")
    
    # Add more references
    obj2 = obj
    obj3 = obj
    print(f"After two extra refs: {sys.getrefcount(obj)}")
    
    # Delete references
    del obj2
    print(f"After deleting one ref: {sys.getrefcount(obj)}")
    del obj3
    print(f"After deleting second ref: {sys.getrefcount(obj)}")
    
    # Now delete the last reference – __del__ is called
    del obj
    
    print("\n=== Garbage Collection for Cycles ===")
    import gc
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        def __del__(self):
            print(f"Deleting Node {self.value}")
    
    # Create a cycle
    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a  # cycle
    
    # Delete references to break the cycle (normally would be handled by GC)
    # But we can't delete del a, b because they still reference each other.
    # The cyclic GC can detect and break the cycle.
    print("Cycle created: a <-> b")
    print("Deleting references to a and b...")
    del a
    del b
    
    # Force garbage collection to clean the cycle
    print("Running cyclic garbage collector...")
    gc.collect()
    
    # The __del__ methods will be called after GC breaks the cycle.
    print("\nCyclic references are cleaned by the garbage collector.")
    print("Reference counting handles non-cyclic memory immediately.")
    
    return "Memory management overview demonstrated."

def test():
    result = solve()
    print(f"\nQ002: {result}")

if __name__ == "__main__":
    test()