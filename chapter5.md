# Lists and Dictionaries

Data structures combine several values into one unit. Elements are usually organized so they can be manipulated

List: allows the user to manipulate data values of any type

Dictionary: associates data values with other data values

## Lists

Sequence of elements, shares many characteristics of strings

Lists are enclosed in brackets and elements are seperated by commas

Can build lists of integers using *list* and *range* functions, len(), in, and subscript [] works the same as for strings. Can use loops as well.

Unlike strings, list elements can be changed. Subscript operator is used to change an element at a given position.
To replace every item in a list, use a for loop to loop through and change each element

Adding or removing:
* .append(element) adds element to end of list
* .extend(aList) adds elements of aList to the end of list
* .insert(index, element) adds element at index, otherwise adds element to the end
* .pop() removes and returns the last element of list
* .pop(index) removes and returns element at index

append and extend modify the original list, but + (concatenating) creates a new list

Searching: *in* usually used to search for a value in a list

Sorting: .sort() mutates a list by arranging its elements in ascending order

Mutator functions/methods return "none" when completed, so defining a new list while using these won't work properly

side effects: replacing one element in a list will also change that list when it is referenced by other variables.

Alias: two names referring to the same object, ex: first = [0, 1, 2]; second = first
Both "first" and "second" are names for the same list

To prevent this, create a new object and copy the contenat of the original. You can use a for loop or list() function
third = list(first)

Testing to see if two objects are equal: == returns true if one variable is an alias for the other, or if they are different but with the same contents
*is* returns true if one is an alias for another, but false if they are two different objects

**Tuple**: like a list, but immutable. Uses () instead of brackets
Best to use for a list whose contents should not change

## Functions

Functions consist of a header and a body

def functionName(parameters):
    body

Body contains statements that will execute when function is called

Functions can include a docstring (comment) that contains information about what the function does. help(functionName)

Functions defined with parameters require arguments when called

Returns: upon encountering a return statement, python evaluates the expression in the statement and returns control to the caller of the function. If there is no return statement, control is returned after evaluating the last line of code in the function and *none* is returned.

boolean functions return true or false

### Main Function

Usually expects no arguments and returns no values.

Purpose may be to take inputs, process them by calling other functions, and returning the results.

Function definitions do not need to be in any particular order, as long as main() is called at the end of the script

## Dictionaries

Organize information by association, written as key/value pairs seperated by commas

{}

Keys can be data of any immutable type, normally strings or integers. 
Values can be any type.

Key/value pairs can be added or replaced using []

dictionary[a key] = a value

Can use [a key] to lookup the associated value, but will raise an exception if that key does not exist
(you can use *in* to test for an uncertain key: if "job" in info:)

.get method also can test for a key:
info.get(key, default value)

Remove keys using .pop(key, default value)

To print a list:
* use a *for* loop to print each pair
* use list(dictionary.items())

help(dict) for full documentation