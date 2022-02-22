# Chapter 4: String and Text Files

Strings are data structures. Strings are sequences of 0 or more characters

len() returns the length of a given string

Characters in a string are numbered from 0 to length-1

Strings are immutable: characters can be accessed, but not inserted, replaced, or removed.

Subscript operator: []
Allows you to examine one character of a string, string[n]
Use string[-1] for the last character

Slicing for Substrings: use a : in the subscript, ex string[0:1] will slice the first character
When 2 integers are included, the range goes from the first integer position, up to (not including) the second.
When an integer is excluded from either side of : the characters extending to the end or the beginning are included

*in* Operator: returns true if a substring is present in a given string
left: target substring
right: string to be searched

Ciphers in this chapter

Number systems: digits in all systems are counted from 0 to n-1

Different number systems still use the same positional value, determined by a digit's position in a number (place value by a different name)

### Converting

Binary to Decimal:

Binary is based on powers of 2

Digit can only be 0 or 1, so to calculate the value of a binary number, sum the positional value of all digits (2^n * 0 or 1)
n = digit's position in the number

Decimal to binary:

algorithm in book divides number by 2, adding on to the end of the number (0 if the divisor is odd, 1 if even)

Binary to octal:

Begin at right and group digits by 3s. Convert each group of digits.

Octal to binary:

Convert each digit into 3-bit binary

Hex to binary: 

Replace each hex digit with its 4-bit binary number

Binary to hex:

Same as with octal, but groups of 4 instead of 3