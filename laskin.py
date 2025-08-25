def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Nollalla jakaminen ei ole sallittua!"
    return x / y
    
if valinta == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif valinta == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif valinta == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif valinta == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Virheellinen valinta")
