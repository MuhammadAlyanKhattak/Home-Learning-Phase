# ! Problem:
# !Ask the user for tomorrow's temperature (°C) and rain forecast (yes/no),
# ! then suggest cumulative clothing recommendations based on conditions:
# ! - Base outfit: Jeans and a T-shirt
# !- <= 20°C: Add a jumper
# !- <= 10°C: Add a jacket
# !- <= 5°C:  Upgrade to a warm coat and add gloves
# !- Rain ("yes"): Add an umbrella

# This was the second last problem of Part 1 overall there are 14 parts and this second last
# i will cleanly start documenting from second part as i go thru
# Write your solution here
print("What is the weather forecast for tomorrow?")
Temp = int(input("Temprature:"))
Rain = input("Will it rain (yes/no):")


if Temp > 20:
    print("Wear jeans and a T-shirt")

if 10 < Temp <= 20:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if 5 < Temp <= 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

if Temp <= 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if Rain == "yes":
    print("Don't forget your umbrella!")
