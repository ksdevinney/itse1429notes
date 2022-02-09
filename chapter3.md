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

### Loop Errors
#### Off By One
Usually caused by the upper bound being specified incorrectly

range() can also have 3 arguments, the 3rd is a *step value* (interval between the numbers)

Loops can also count down, using a negative number as the step argument. Thus, the first argument for range() will be the upper bound, second argument will be the lower bound minus 1