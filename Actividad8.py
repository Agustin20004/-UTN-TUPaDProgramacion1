# Pedimos el nombre
nombre = input("Ingresá tu nombre: ")

# Pedimos la opción
opcion = input("Elegí una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")

# Procesamos según la opción
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")