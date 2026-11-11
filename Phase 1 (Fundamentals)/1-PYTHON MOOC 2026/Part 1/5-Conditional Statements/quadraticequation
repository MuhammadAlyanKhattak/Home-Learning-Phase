# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("Value of a: "))

b = int(input("Value of b: "))

c = int(input("Value of c: "))
# ! Python follows standard math order of operations (PEMDAS/BODMAS), meaning division happens before subtraction.

# ! Mistakes i made =
## Exponents use **, not ²
## 2. Multiplication needs *: In math, writing 4ac or 2a means multiplication. In Python, writing 4ac makes Python look for a single variable literally named 4ac, causing a SyntaxError. I must write 4 * a * c and 2 * a


xplus = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)

# in -b - sqrt((b**2) - (4*a*c)) / (2*a) = this is wrong wtihout () wrapping from -b to the )) because  then -b is not made a part of division at all

xminus = (-b - sqrt((b**2) - (4 * a * c))) / (2 * a)

print(f"The roots are {xplus} and {xminus}")
