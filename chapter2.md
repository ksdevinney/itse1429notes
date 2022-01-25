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