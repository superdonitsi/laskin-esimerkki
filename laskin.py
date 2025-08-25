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

print("Valitse toiminto:")
print("1. Lisää")
print("2. Vähennä")
print("3. Kerro")
print("4. Jaa")
valinta = input("Syötä valinta (1/2/3/4): ")
num1 = float(input("Syötä ensimmäinen luku: "))
num2 = float(input("Syötä toinen luku: "))
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