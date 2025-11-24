num1 = float(input("first number: "))
op = input("operator: ")
num2 = float(input("second number: "))

match op:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        while(num2 == 0):
            num2 = float(input("zero devision, please enter an other number: "))
        result = num1 / num2
print(f"equals: {result}")
