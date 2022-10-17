value = input("Expression: ")
x, y, z = value.split(" ")
x = float(x)
z = float(z)
if y == '+':
    sum = float(x + z)
    print(sum)
elif y == '-':
    substract = float(x - z)
    print(substract)
elif y == '*':
    multiply = float(x * z)
    print(multiply)
elif y == '/' and z == 0:
    print("Error")
    exit(1)
elif y == '/':
    devide = float(x / z)
    print(devide)