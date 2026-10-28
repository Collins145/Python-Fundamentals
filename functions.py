        # Functions:

# 1) Standard library / Built-in Functions: Already exist
x = min(45,89,90,32,67,57)
print(x)

y = max(45,89,90,32,67,57)
print(y)

# 2) User defined functions:  User creates the function of their own
# Users get to create and define the functions
# Example
# Program that prints the name eMobilis as a school

    # Steps to follow
# i) Use the keyword def (define)


def school():
    print("Welcome to eMobilis")

school() #Calling a Function

# def-Keyword
# school-Function
# school()-Calls the function
# N/B: For user defined functions to print or give the result, they have to be called

def add():
    x = 10 # We can use the input method
    y = 20
    print(x+y)

add()

# Parameters & Arguments
# In functions, for they MUST always be passed as parameters
def add(x,y): # X & Y are parameters/variables
    print(x+y)

add(10,20) # 10 & 20 are arguments
# N/B: Parameters are also variables
# Argument: Refers to the value passed while calling the function