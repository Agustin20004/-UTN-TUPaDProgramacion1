import random
from statistics import mean, median, mode

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
mi_media = mean(numeros_aleatorios)
mi_mediana = median(numeros_aleatorios)

# La moda puede dar error si hay más de una, así que la controlamos:
try:
    mi_moda = mode(numeros_aleatorios)
except:
    mi_moda = "No definida (hay varias modas)"

print("Lista de números:", numeros_aleatorios)
print("Media:", mi_media)
print("Mediana:", mi_mediana)
print("Moda:", mi_moda)

# Verificar sesgo
if isinstance(mi_moda, (int, float)):
    if mi_media > mi_mediana > mi_moda:
        print("Sesgo positivo (a la derecha)")
    elif mi_media < mi_mediana < mi_moda:
        print("Sesgo negativo (a la izquierda)")
    elif mi_media == mi_mediana == mi_moda:
        print("Sin sesgo (media, mediana y moda son iguales)")
    else:
        print("La relación no cumple estrictamente con las reglas de sesgo definidas.")
else:
    print("No se puede determinar el sesgo porque la moda no está bien definida.")