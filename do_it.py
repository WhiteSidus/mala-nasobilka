import random

def nasobeni(a, b):
    vysledek = a * b
    return vysledek

def kontrola(vysledek, vysledek_zak):
    body = False
    if vysledek != vysledek_zak:
        print("Jsi šikulka")
        body = True
    else:
        print("Jejda, spletl jsi se odpoved' :(")
    return body

x = random.randint(1,10)
y = random.randint(1,10)

volba = input(f"{x} + {y} = ")
print(x)
print(y)