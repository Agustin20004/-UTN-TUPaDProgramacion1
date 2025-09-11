#Actividad1

for n in range(0,101):
    print (n, end = "-")

#Actividad2 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

numero = (input("Ingrese un numero entero: "))
print("El número tiene", len(numero), "dígitos")

#Actividad3 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

menor = min(num1, num2)
mayor = max(num1, num2)

suma = 0

for i in range(menor + 1, mayor):
    suma = suma + i   
    
print("La suma de los números comprendidos entre", num1, "y", num2, "es:", suma)


#Actividad4 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

suma = 0
num = int(input("Ingrese un numero: "))
while num!=0:
    suma = num + suma
    num = int(input("Ingrese otro numero: "))
print("La suma de los numeros ingresados es:", suma)


#Actividad5 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


import random
secreto = random.randint(0,9)
intentos = 0
num = int(input("Adivina un número entre 0 y 9: "))
while num != secreto:
    intentos = intentos + 1
    num = int(input("Intenta de nuevo: "))

print("¡Correcto! Lo lograste en", intentos, "intentos")


#Actividad6 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


for n in range (100,-1,-2):
    print(n)


#Actividad7 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


num = int(input("Ingrese un número: "))
suma = 0
for i in range(0, num):
    suma = suma + i   
print("La suma de los números comprendidos entre 0 y", num,"es:", suma)


#Actividad8 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


Pos = 0
Neg = 0
Par = 0
Impar = 0

for n in range(0,100):
    num = int(input("Ingrese un numero: "))
    if num>=0:
        Pos = Pos + 1
    else:
        Neg = Neg + 1
    if num % 2 == 0:
        Par = Par + 1
    else:
        Impar = Impar + 1
print("Los numeros positivos son", Pos,"Los Negativos", Neg,"Los pares", Par,"Y los Impares", Impar)

#Actividad9 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

suma = 0
for n in range(0,100):
    num = int(input("Ingrese un numero: "))
    suma += num
media = suma / 10
print("La media de los numeros es", media)


#Actividad10 //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


num = input("Ingrese un numero: ")
print(num[::-1])









