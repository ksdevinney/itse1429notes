# Chapter 3: Loops and Selection Statements

## 3.1 The For Loop

Loops repeat an action- each repetition is a "pass" or "iteration"

*definite iterations* repeat a predefined number of times, *indefinite iterations* repeat until the program tells it to stop

for <variable> in range(<integer expression>):
    <statement>

Integer expression determines how many times the loop will run, can be a constant
First line is called the loop header
Loop body is the statements to be executed (must be indented and aligned)

Count-controlled loops: count through a range of numbers
range() can accept 2 arguments: lower bound and upper bound (upper bound should be 1 greater than the desired count)

Augmented assignment: += and its friends
<variable> <operator>= <expression>

Loop Errors: Off By One
Usually caused by the upper bound being specified incorrectly

range() can also have 3 arguments, the 3rd is a *step value* (interval between the numbers)

Loops can also count down, using a negative number as the step argument. Thus, the first argument for range() will be the upper bound, second argument will be the lower bound minus 1

### Formatting Data

Output usually required to be in tabular format, either right-justified or left-justified

<format string> % <datum>

Example,
"%<field width>s" (s for string, d for integers)
"%6s" % "four" prints "  four"
"%-6s" % "four" prints "four  "

Positive field widths are right-justified, negative are left-justified

Can stack multiple format strings, with % to separate each column
Can use to format output of a for loop

For float:
%<field width>.<precision>f
precision is optional

## If and if else

Selection statements allow computers to make choices

**if-else** used to make a choice between two alternatives(two-way selection), often used to check inputs for errors

if <condition>:
    <first set of expressions>
else:
    <alternate expressions>

Condition must be a boolean expression
: required after condition and *else*
Expressions must be indented at least one space beyond if and else

If: one-way selection
If the statment is true, the expressions will evaluate. If false, the program will move on to the next statement following the selection

Multi-way if statements (else if)
Considers each statement until one evaluates to true, if no condition is true, action after the 'else' is performed

if <condition 1>:
    <expression>
elif <condition 2>:
    <expression>
else:
    <expression>

Logical operators:
and, or, not

Short circuit evaluation: program can evaluate if a statement should execute or not before the condition is fully evaluated, based on *and* (first statement is false, whole condition is false) and *or* (first part is true, so whole condition is true)