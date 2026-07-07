#!/usr/bin/env python3
"""
Question 9:
Explain the difference between `@staticmethod`, `@classmethod`, and instance methods.
"""

def solve():
    """
    Instance methods: Take self as first parameter, can access instance attributes.
    Class methods: Take cls as first parameter, can access class attributes.
    Static methods: Take no special first parameter, can't access class or instance attributes.
    """
    
    class MyClass:
        class_var = 0
        
        def __init__(self, value):
            self.value = value
        
        # Instance method - can access both instance and class attributes
        def instance_method(self):
            self.value += 1
            MyClass.class_var += 1
            return f"Instance value: {self.value}, Class var: {MyClass.class_var}"
        
        # Class method - can only access class attributes
        @classmethod
        def class_method(cls):
            cls.class_var += 1
            return f"Class var: {cls.class_var}"
        
        # Static method - cannot access class or instance attributes
        @staticmethod
        def static_method():
            return f"This is a static method, no access to self or cls"
        
        # Another static method with parameters
        @staticmethod
        def add_numbers(a, b):
            return a + b
    
    # Create instance
    obj = MyClass(10)
    
    print("=== Instance Method ===")
    print(obj.instance_method())
    print(obj.instance_method())
    
    print("\n=== Class Method ===")
    print(MyClass.class_method())
    print(MyClass.class_method())
    
    print("\n=== Static Method ===")
    print(MyClass.static_method())
    print(f"Static method with params: {MyClass.add_numbers(5, 3)}")
    
    print("\n=== Key Differences Summary ===")
    print("""
    ┌─────────────────┬──────────────────┬─────────────────────┐
    │ Method Type     │ First Parameter   │ Can Access          │
    ├─────────────────┼──────────────────┼─────────────────────┤
    │ Instance        │ self             │ Instance + Class    │
    │ Class           │ cls              │ Class only          │
    │ Static          │ None             │ None (limited)      │
    └─────────────────┴──────────────────┴─────────────────────┘
    
    Use @classmethod for factory methods or when you need to modify class state.
    Use @staticmethod for utility functions that logically belong to the class.
    Use instance methods for most operations that need instance data.
    """)
    
    return "See prints above for detailed explanation."

def test():
    result = solve()
    print(f"\nQ009: {result}")

if __name__ == "__main__":
    test()