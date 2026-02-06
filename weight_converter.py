unit = input("select unit kilograms and Pounds (Kg or P): ")
weight = float(input("Enter your weight: "))

if unit == "Kg":
    weight *= 2.2025
    unit = "Lbs."
    print(f"your weight is : {round(weight,1)}{unit}")
elif unit == "P":
    weight /=2.2025
    unit = "Kgs."
    print(f"your weight is : {round(weight,1)}{unit}")
else:
    print(f"unit was not valid")
