#!/usr/bin/env python3
"""
Question 11:
What is the difference between a shallow copy and a deep copy? How do you make each?
"""

def solve():
    """
    Shallow copy: Copies the object itself but references nested objects.
    Deep copy: Recursively copies all nested objects.
    """
    import copy
    
    # Original nested structure
    original = [1, 2, [3, 4]]
    print(f"Original: {original}")
    
    # Shallow copy
    shallow = copy.copy(original)
    print(f"Shallow copy: {shallow}")
    
    # Deep copy
    deep = copy.deepcopy(original)
    print(f"Deep copy: {deep}")
    
    print("\n=== Modifying nested structure ===")
    original[2].append(5)
    print(f"After modifying original: {original}")
    print(f"Shallow copy: {shallow}")  # Changed!
    print(f"Deep copy: {deep}")        # Unchanged!
    
    print("\n=== Explanation ===")
    print("""
    Shallow copy:
    - Copies only the top-level object
    - Nested objects are shared between copies
    - Use: copy.copy(obj)
    
    Deep copy:
    - Recursively copies all objects
    - Creates independent copies of nested objects
    - Use: copy.deepcopy(obj)
    
    When to use:
    - Shallow: For simple objects or when sharing is desired
    - Deep: For complex objects when independence is needed
    """)
    
    return "Shallow copy copies references to nested objects, deep copy copies everything recursively."

def test():
    result = solve()
    print(f"\nQ011: {result}")

if __name__ == "__main__":
    test()