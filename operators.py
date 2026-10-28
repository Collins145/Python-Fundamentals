# Operators:

# 1) Arithmetic operators
# Used for simple mathematical calculations (+,-,/,*,//)
x = 20
y = 30

# i) Addition
print(x+y)

# ii) Subtraction
print(x-y)

# iii) Multiplication
print(x*y)

# iv) Division
print(x/y)

# v) Modulus (Percentage)
print(x//y)
# N/B: Modulus divides two numbers and returns the remainder

# 2) Comparison Operators
# Used for comparing two or more values and return a boolean
num1 = 45
num2 = 30
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) #Equal to
print(num1 != num2) #Not equal to

# 3) Assignment Operators
# Used to store or assign values in variables
number = 80 # Variable number assigns or stores the value 80
print(number)

# Operator precedence (BODMAS)
# Addition assignment operator
number += 2
print(number)

# Subtraction assignment
number -= 2
print(number)

# 4) Logical Operators
# Used to check more than one condition to determine a result

    # i) AND operator (&) : Returns a TRUE result ONLY if ALL conditions are TRUE
print( 100==40 & 60 < 90)

    # ii) OR operator () : Returns a TRUE result ONLY if ANY of the conditions is TRUE even if others are FALSE
print( 100==40 or 60 < 90)

    # iii) NOT operator (!) : Returns a
print( not (100==40 & 60 < 90) )