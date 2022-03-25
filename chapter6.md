# Chapter 6: Design with Functions

Abstraction: coping with complexity by simplifying ot hiding it

Functions can help eliminate redundancy in programs (can use a function instead of re-writing the same algorithm each time)

Hide complexity:

Algorithm: general method for solving a class of problems, individual problems that make up the "class" are *problem instances*

Each function should provide a single coherent task

## Top-Down Design

Starts with a global view of the problem, then breaks it into smaller pieces

## Recursive Functions

recursive: a function that calls itself

Function may run once, then call itself using the results from previous run as parameters

Most recursive functions expect at least one argument, to test the base case that ends the recursive process

Recursive functions can be turned into infinite recursions if there's no base case to terminate the process

Recursion is often simpler than using a lööp, but recursive functions may use more call stack (memory)

## Namespace

Module variables: introduced at the module level

Parameters: behaves like a variable, introduced in a function header

Temporary variables: introduced in the body of a function

Methods: defined in the *str* type

Temporary variables are restricted to the body of the function where they are introduced

Module variables have a scope anywhere in the function below the point where they are introduced

Functions can reference a module variable, but cannot assign a new value to it: a new, temporary variable of the same name is introduced for the function

Variable's lifetime is defined as the time during a program when a variable has memory assigned to it

Required arguments are listed first, optional arguments have a default value when not listed

Programmers can specify optional arguments in function definitions:
def <function name>(<required argument>, <key 1> = <value 1>, <key 2> = <value 2>)

Default (optional) arguments can be supplied in function call by position, or by keyword

## Higher Order functions

Expects a function and data values as arguments

Functions in Python are first-class data objects: can be assigned to variables, passed as arguments to other functions, returned as the value of other functions, and stored in data structures

Mapping! 
Applies a function to each value in a sequence

Filtering!
Predicate ("true" condition) is applied to each value in a list

Reducing!
Take a list of values and repeatedly apply a function to accumulate a single value (import functools)

**lambda** is an anonymous function: contains the names of its arguments and a single expression, no name of its own

Jump table: dictionary of functions keyed by command names