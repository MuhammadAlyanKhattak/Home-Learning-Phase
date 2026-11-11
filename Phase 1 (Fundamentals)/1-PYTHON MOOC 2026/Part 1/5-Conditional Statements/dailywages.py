# ! This program calculate the wages of employees :
# on all days of the week the wages are normal
# but on sunday its 2x
# Write your solution here
hourlywage = float(input("Hourly wage:"))
hoursworked = float(input("Hours Worked:"))
dayoftheweek = input("Day of the week:")

DailyWages = hourlywage * hoursworked
SundayWages = DailyWages * 2

if dayoftheweek != "Sunday":
    print(f"Daily wages: {DailyWages} euros")
else:
    print(f"Daily wages: {SundayWages} euros")
