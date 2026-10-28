# Exception:

# Exception handling: Error handling method
print(name)  # This line gives an error since we're trying to print the variable name yet it hasn't been defined
# Exception handling helps to resolve such errors using the following blocks
# 1)Try: Always goes through the program line by line to check of any future errors
# 2)Except: Allows the program handle the error incase it is encountered, thus the statement in the except block is returned
try:
    print(name)

except:
    print("error/Oops sorry!")