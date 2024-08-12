print(f"Python Exception Handling")

# source : https://www.geeksforgeeks.org/python-exception-handling/


# syntax error
"""
amount = 10000
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")

"""

# type error :
"""
x = 5
y = "hello"
z = x + y

"""
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")
    # raise ValueError("Original error")
    raise TypeError("Invalid")
