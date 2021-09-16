# Programmers: Will and Terry
# Course: CS151, Dr. Rajeev
# Date: 9/16/21
# Lab Number: 1
# Program Inputs: We request the user input a number of milliliters
# Program Outputs: We display the converted amount of teaspoons and tablespoons

mil = float(input("Please input a number of milliliters"))
teaspoons=(mil/5)
tablespoons=(mil/15)

print("there are " + str(teaspoons) + " teaspoons in " + str(mil) + " milliliters")
print("there are " + str(tablespoons) + " tablespoons in " + str(mil) + " milliliters")