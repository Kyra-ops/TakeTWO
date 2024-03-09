weight = int(input("How much do you weight? "))
# input uses string so I used str to convert the string into int, so weight can be entered
unit = input("(K)g or (L)bs? ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + converted)

else:
    converted = weight * 0.45
print("Weight in Kgs: " + str(converted))
# notice the str before converted, conerting the float back into a string

print("Done")