#!/usr/bin/env python3
"""
Question 10:
What is a closure? Provide an example.
"""

def solve():
    """
    A closure is a function that remembers the environment (scope) where it was created,
    even after the outer function has finished executing.
    """
    
    print("=== Example 1: Basic Closure ===")
    def outer(x):
        def inner(y):
            return x + y
        return inner
    
    add5 = outer(5)
    print(f"add5(10) = {add5(10)}")  # 15
    print(f"add5(20) = {add5(20)}")  # 25
    
    print("\n=== Example 2: Closure with modification ===")
    def counter():
        count = 0
        def increment():
            nonlocal count
            count += 1
            return count
        return increment
    
    counter1 = counter()
    print(f"counter1(): {counter1()}")
    print(f"counter1(): {counter1()}")
    print(f"counter1(): {counter1()}")
    
    counter2 = counter()
    print(f"counter2(): {counter2()}")
    
    print("\n=== Example 3: Closure for caching ===")
    def memoize():
        cache = {}
        def get_value(key):
            if key not in cache:
                cache[key] = key * key  # Simulate expensive calculation
            return cache[key]
        return get_value
    
    cached_calc = memoize()
    print(f"Calculate 5: {cached_calc(5)}")
    print(f"Calculate 5 again (from cache): {cached_calc(5)}")
    print(f"Calculate 10: {cached_calc(10)}")
    
    print("\n=== Example 4: Closure in loops ===")
    def create_multipliers():
        result = []
        for i in range(3):
            def multiplier(x):
                return i * x
            result.append(multiplier)
        return result
    
    mults = create_multipliers()
    print(f"multipliers[0](2) = {mults[0](2)}")  # Note: all return 4 (last i value)
    print("This happens because closures capture variables by reference, not value.")
    
    print("\n=== Example 5: Fixing closure in loop ===")
    def create_multipliers_fixed():
        result = []
        for i in range(3):
            def multiplier(x, fixed_i=i):
                return fixed_i * x
            result.append(multiplier)
        return result
    
    mults_fixed = create_multipliers_fixed()
    print(f"Fixed: multipliers[0](2) = {mults_fixed[0](2)}")
    print(f"Fixed: multipliers[1](2) = {mults_fixed[1](2)}")
    print(f"Fixed: multipliers[2](2) = {mults_fixed[2](2)}")
    
    print("\n=== Key Characteristics ===")
    print("""
    Closures have three main characteristics:
    1. They are nested functions
    2. They capture variables from the outer scope
    3. They can access those variables even after the outer function returns
    
    Common uses:
    - Function factories
    - Callbacks
    - Decoration
    - Memoization/caching
    - Maintaining state in functional programming
    """)
    
    return "See prints above for closure examples."

def test():
    result = solve()
    print(f"\nQ010: {result}")

if __name__ == "__main__":
    test()