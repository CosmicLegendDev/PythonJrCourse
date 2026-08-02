# Python classes and objects

In Python, a class is a blueprint for creating objects. An object is an instance of a class. Classes encapsulate data for the object and methods to manipulate that data.

Class holds properties and its relevant methods.

_Example:_ House plan is a blueprint for building a house. It defines the structure and design of the house. Similarly, a **class** defines the structure and behavior of an object.
House you constructed using the blueprint is called an **object**. It is an instance of the **class**. You can create multiple houses (**objects**) using the same blueprint (**class**).

### 1. Define a class

To define a class in Python, we use the `class` keyword. The syntax is:

```python
class ClassName:
    # class body
```

_Example:_

````python
class House:
    pass  # This is an empty class
```
In this example, we defined a class named `House`. The `pass` statement is used as a placeholder for the class body, which means that the class does not have any attributes or methods yet.
````

## What is an object.

Object is an instance of class (blue print)
Using object, we can access the properties and methods defined in the class.

Using dot operator we can acces properties and methods.

_Example:_

```python
class House:
    def __init__(self, color, size):
        self.color = color  # attribute
        self.size = size    # attribute

house1 = House("red", "large")  # creating an object of the House class
print(house1.color)  # Output: red
print(house1.size)   # Output: large
```

# Home work

# Build a calculator using class and methods.

The calculator should have methods for addition, subtraction, multiplication, and division.
The calculator should take two numbers as input and perform the selected operation.

# OOPS - Object Oriented Programming..

OOPS is a programming paradigm that uses objects and classes to structure the code. It helps in organizing code, making it reusable, and easier to maintain.

## Encapsulation

Encapsulation is the concept of wrapping data and methods that operate on that data within a single unit, i.e., a class. It restricts direct access to some of the object's components.

## Inheritance

Inheritance is a mechanism in OOP that allows a class to inherit attributes and methods from another class. The class that is inherited from is called the **parent class** or **base class**, and the class that inherits is called the **child class** or **derived class**.

## Polymorphism

Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon.

## Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. It helps in reducing programming complexity and effort.
