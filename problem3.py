#!/usr/bin/env python3
"""
Question 3:
What are MRO and how does Python resolve method calls in multiple inheritance?
"""

def solve():
    """
    MRO stands for Method Resolution Order.
    It is the order in which Python looks for methods in a class hierarchy
    when multiple inheritance is involved.

    Python uses the C3 linearization algorithm (also called C3 superclass linearization)
    to compute the MRO. It ensures:
    - Subclasses come before superclasses.
    - The order respects the inheritance hierarchy.
    - The order is consistent (monotonic).

    You can view the MRO of any class using:
    - ClassName.__mro__
    - ClassName.mro()
    - help(ClassName)
    """

    print("=== Example 1: Simple Inheritance ===")
    class A:
        def method(self):
            return "A's method"

    class B(A):
        def method(self):
            return "B's method"

    class C(B):
        def method(self):
            return "C's method"

    print(C.__mro__)   # (C, B, A, object)
    c = C()
    print(c.method())  # C's method

    print("\n=== Example 2: Multiple Inheritance ===")
    class X:
        def method(self):
            return "X's method"

    class Y:
        def method(self):
            return "Y's method"

    class Z(X, Y):
        pass

    print(Z.__mro__)   # (Z, X, Y, object)
    z = Z()
    print(z.method())  # X's method (first in MRO)

    print("\n=== Example 3: Diamond Problem (Diamond Inheritance) ===")
    class Base:
        def method(self):
            return "Base's method"

    class Left(Base):
        def method(self):
            return "Left's method"

    class Right(Base):
        def method(self):
            return "Right's method"

    class Bottom(Left, Right):
        pass

    print(Bottom.__mro__)   # (Bottom, Left, Right, Base, object)
    b = Bottom()
    print(b.method())       # Left's method (first in MRO)

    # Explanation:
    # The C3 algorithm ensures a consistent order that respects the local precedence
    # and monotonicity. Base is called only once, and the method from Left is used
    # because Left appears before Right in the inheritance list.

    print("\n=== Example 4: Complex Hierarchy ===")
    class Animal:
        def speak(self):
            return "Animal"

    class Mammal(Animal):
        def speak(self):
            return "Mammal"

    class Bird(Animal):
        def speak(self):
            return "Bird"

    class Bat(Mammal, Bird):
        pass

    print(Bat.__mro__)      # (Bat, Mammal, Bird, Animal, object)
    bat = Bat()
    print(bat.speak())      # Mammal

    # The C3 order: Bat -> Mammal -> Bird -> Animal -> object
    # Mammal is before Bird because Bat inherits from Mammal first.

    return "\nMRO explained with examples. Check the prints above."

def test():
    result = solve()
    print(f"\nQ003: {result}")

if __name__ == "__main__":
    test()
    