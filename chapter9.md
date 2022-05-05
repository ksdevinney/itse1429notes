# Chapter 9: Classes

Objects are abstractions: packages a set of values and operations that can be easily referenced

Class definitions contain:
* definitions of all methods that can be used on the object
* definitions of data structures used to maintain the state

Class names are typically capitalized

Classes should be defined in a seperate file, then imported

method definitions must include a "self" parameter, even though the variable name when the method is called binds the object instance to the method

Most classes include __init__ as the constructor to to initialize the object's attributes

Attributes of an object are represented as instance variables

Accessors: allow you to view the object's state

Mutators: allow you to modify an object's state

* Plan the behavior and attributes of the objects of your new class
* Choose an appropriate class name and methods
* Write a test script to instantiate the class and use its methods
* Choose the best data structures to represent the attributes
* Fill the class template with an __init__ method and a __str__ method
* Complete and test the remaining methods
* Document your code, include a docstring

Operator overloading: you can "overload" the default operations by defining a new operation using the same method name

Comparison methods: once the implementer of the class has defined methods for ==, <, >= the others are automatically provided

Not all objects can be compared for inequality, but all objects can be compared for equality 

Pickling: converting an object to text for storage
pickle.dump: puts things in a text file
pickle.load: puts things from a text file into a program (use *try...except*)

uhhhhhhhhhh

## 2-D Grids

Container where you organize things by row and column

import Grid
Grid(rows = , columns = , *optional* fillValue)

Also, need to get good at:
* Data encapsulation
* Inheritance
* Polymorphism (allowing several classes to use same method names)

all classes extend "object" and inherit properties of object. 
All new subclasses inherit instance variables and methods of ancestor classes

Imperative programming: consists of input and output statements; based on having sets of commands

Procedural programming: useing cooperating subprograms to solve problems

Functional programming: programs as a set of cooperating functions