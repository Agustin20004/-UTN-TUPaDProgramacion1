texto = input("Ingrese una frase o palabra ")
vocales = "aeiouAEIOU"
if texto[-1] in vocales:
    texto = texto + "!"
    print(texto)
else:
    print(texto)