import math

def calc_hipo(cateto_a, cateto_b):
    return math.sqrt(cateto_a**2 + cateto_b**2)

# Ejemplo de uso
a = 3
b = 4
print("La hipotenusa es:", calc_hipo(a, b))
