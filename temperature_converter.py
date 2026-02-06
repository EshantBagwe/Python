unit = input("select unit Celsius and Fahrenheit (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((9*temperature)/5+32,1)
    print(f"your temperature is : {round(temperature,1)}°F")
elif unit == "F":
    temperature = round((temperature-32)*5/9,1)
    print(f"your temperature is : {round(temperature,1)}°C")
else:
    print(f"{unit} is invalid unit of temperature measurement")
