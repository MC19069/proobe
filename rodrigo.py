import math

x = float(input("Ingrese el valor de x: "))
gamma_value = x
n = 1
term2= 1
tolerance = 1e-8
while abs(term2) >= tolerance:
    term2=(x / (n * math.pi))
    term = (1 - term2**2)
    gamma_value *= term
    n += 1
    print(gamma_value)
print(f"El valor de γ({x}) es aproximadamente: {gamma_value}")
