# BMI
# < 16              starvation
# 16.00 - 16.99     emaciation
# 17.00 - 18.49     underweight
# 18.50 - 24.99     correct weight
# 25.00 - 29.99     over weight
# 30.00 - 34.99     first degree obesity
# 35.00 - 39.99     second degree obesity clinical
# > 34              third degree obesity extreme

height = float(input("Height in meters: "))
weight = int(input("Weight in kilograms: "))
BMI = weight/(height * height)

if (BMI <= 16.00):
    print("Diagnostic: starvation")
    print("BMI: ", BMI)
elif(16.00 <= BMI <= 16.99):
    print("Diagnostic: emaciation")
    print("BMI: ", BMI)
elif(17.00 <= BMI <= 18.99):
    print("Diagnostic: underweight")
    print("BMI: ", BMI)
elif(18.50 <= BMI <= 24.99):
    print("Diagnostic: correct weight")
    print("BMI: ", BMI)
elif(25.00 <= BMI <= 29.99):
    print("Diagnostic: over weight")
    print("BMI: ", BMI)
elif(30.00 <= BMI <= 34.99):
    print("Diagnostic: first degree obesity")
    print("BMI: ", BMI)
elif(35.00 <= BMI <= 39.99):
    print("Diagnostic: second degree obesity clinical")
    print("BMI: ", BMI)
else:
    if(BMI > 40.00):
        print("Diagnostic: third degree obesity extreme")
        print("BMI: ", BMI)

weight_min = 18.50 * (height ** 2)
weight_max = 24.99 * (height ** 2)

print("The correct interval is between: ")
print("Min", weight_min)
print("Max", weight_max)
