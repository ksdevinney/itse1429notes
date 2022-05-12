# Chapter 2: Software Development, Data Types, Expressions

## 2.1 Software Development Process

Planning and organizing a program

**Waterfall method**: request, analysis, design, implementation, integration, maintenance

Each phase flows to the next, though mistakes may require revisiting previous phase. Mistakes are cheaper to fix in earlier phases than maintenance phase

Testing: even if program loads with no syntax errors, you need to test for unexpected output (logic errors/design errors).

A *correct program* produces the expected output for any (correct) input

*test suite*: small set of inputs to test for correct output, if correct output is given for these values, the program should not have any logic errors

## 2.2 Strings, Assignments, Comments

Data type: set of values and operations that can be performed on those values

Literal: the way a value of a data type looks to the programmer

**String literal**: sequence of characters enclosed in quotation marks (double or single)
Use double quotes for a string that contains apostrophes/single quotation marks
To print a multiple-line paragraph, include the whole thing in triple quotation marks. Without print(), the newline character will appear in place of line breaks

**Escape sequences** express special characters

**Concatenation**: joining two or more strings
Can repeat a string using *
EX: " " * 10 prints 10 spaces

Variables: usually named in all lower case letters. Variable names with more than one word are usually camelCased, upper case letters and underscores usually used for constants

Assignment statement: <variable name> = <expression>
Python interpreter first evaluates the expression and then binds the variable name to the value

**Abstraction**: substituting a simple thing (variable name) for a more complex part of a program (expression)

Comments: program text that is ignored by the interpreter, but provides information to the programmer
Docstring: comment at the beginning of a program, stating the author's name and the program's use
End of line comments start with #

## Numeric Data Types

Float: for real numbers, from -10^308 to 10^308 with 16 digits of precision
Ord() and chr() convert characters to ASCII and back, respectively

## Expressions

Arithmetic operators: - negation, ** exponentiation, * multiplication, / division, // quotient, % remainder, + addition, - subtraction

Same rules of precedence apply: exponents, negation, multiplication, division/remainder, addition and subtraction; evaluated from left to right

When both operands are the same type, resulting value is also that type. When operands are different types, resulting value will be the more general type (float is more general than int)

// always produces an int, / produces a float

Mixed-mode arithmetic: calculations involving both int and float. Ints are converted to floats temporarily to perform operations.

Can convert values by using conversion functions:
int(<number or string>)
float(<number or string>)
str(<any value>)

Cannot concatenate a string and a number!
Convert number to string first

**strongly types language**: interpreter checks all data types before operators are applied

## Functions and Modules

**Function**: chunk of code that can be called to perform a task
*Parameters*: names that refer to arguments (specific data needed for the task)

Some functions have required arguments, some have optional arguments, some have both

Math module! Built in, unlike C++

Can use help(functionName) to get documentation on functions

Instead of referring to math.pi() or whatever, you can import certain functions:
from *math* import *pi*

Main module??

Good program format:
* Comment stating programmer's name and purpose of the program
* import needed modules
* initialize (and comment) any important variables
* prompt the user for input data and save to variables
* process inputs
* display results

Can run python programs in terminal: navigate to correct directory, type *python3 program.py*