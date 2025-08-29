# Pedir datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("Ingresá el número de mes (1-12): "))
dia = int(input("Ingresá el día del mes: "))

# Determinar la estación (primero para hemisferio norte)
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

# Para hemisferio sur es lo contrario
if estacion_norte == "Invierno":
    estacion_sur = "Verano"
elif estacion_norte == "Verano":
    estacion_sur = "Invierno"
elif estacion_norte == "Primavera":
    estacion_sur = "Otoño"
else:
    estacion_sur = "Primavera"

# Mostrar según el hemisferio elegido
if hemisferio == "N":
    print("Estás en:", estacion_norte)
elif hemisferio == "S":
    print("Estás en:", estacion_sur)
else:
    print("Hemisferio no válido")