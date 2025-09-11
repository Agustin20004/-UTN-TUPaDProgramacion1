pi = 3.1416

radio = float(input("Ingrese el radio del círculo: "))
print(radio)


area = pi * radio**2
print(area)


perimetro = 2 * pi * radio
print(perimetro)

# Mostrar mensaje final
print(f"El área del círculo es {area:.2f} y su perímetro es {perimetro:.2f}")