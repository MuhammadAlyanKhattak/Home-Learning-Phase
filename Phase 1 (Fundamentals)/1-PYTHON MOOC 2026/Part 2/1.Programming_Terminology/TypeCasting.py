# Programming Exercise: Typecasting
# University of Helsinki Python MOOC
#
# Task:
# When programming in Python, often we need to change the data type of a value.
# For example, a floating point number can be converted into an integer with the function int.
#
# Please write a program which asks the user for a floating point number and
# then prints out the integer part and the decimal part separately. Use the Python int function.
# You can assume the number given by the user is always greater than zero.
#
# Example of expected behaviour:
# Sample output:
# Please type in a number: 1.34
# Integer part: 1
# Decimal part: 0.34




# My solution written here
usernum = float(input("Please type in a number: "))
integernum = int(usernum)

# integernum = print("Integer part:", int(usernum))   , and got stuck for few minutes but found out that it intergernum included print so it did not stored the input value at all thats why when i tried to "-" it said below line of code  operator "-" not supported for types "float" and "None" so the fix is store the variable in the integernum and then print in last line as u would seee , print do not store value data even if u assign it to a variable .
print(f"Integer part:{integernum}")
decimalf = usernum - integernum

print(f"Decimal part:{decimalf}")
