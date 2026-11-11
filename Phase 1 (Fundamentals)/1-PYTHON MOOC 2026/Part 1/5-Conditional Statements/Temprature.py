# !Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".:


# Write your solution here
# 1: Ask user for temperature in degrees Fahrenheit =
usertempF = int(input("Please type in a temperature (F):"))

# 2:Then print the user input in F into C degree celsius
Cdegree = (usertempF - 32) * 5 / 9
if Cdegree >= 0:
    print(f"{usertempF} degrees Fahrenheit equals {Cdegree} degrees Celsius ")


# 3: If the the converted temp falls below zero degree celsius the program should also print out "Brr! It's cold in here!".
if Cdegree < 0:
    print(f"{usertempF} degrees Fahrenheit equals {Cdegree} degrees Celsius ")
    print("Brr! It's cold in here!")


# 4:∘C=(∘F−32)×59
