number1 = float(input("Enter value: "))
operators = input("Enter the operator (+,-,*,/,**,//,%): ")
number2 = float(input("Enter value: "))

if operators == "+":
    result = number1 + number2
    print(round(result,3))
elif operators == "-":
    result = number1 - number2
    print(round(result,3))
elif operators == "*":
    result = number1 * number2
    print(round(result,3))
elif operators == "/":
    result = number1 / number2
    print(round(result,3))   
elif operators == "**":
    result = number1 ** number2
    print(round(result,3))    
elif operators == "//":
    result = number1 // number2
    print(round(result,3))   
elif operators == "%":
    result = number1 % number2
    print(round(result,3))
else:
    print("Enter valid input!")





