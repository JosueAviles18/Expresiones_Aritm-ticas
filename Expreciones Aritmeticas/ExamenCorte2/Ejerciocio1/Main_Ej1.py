# Importamos la función que invierte la frase desde el archivo funciones.py
from funciones import invertir_frase

# Solicitamos al usuario que ingrese una frase cualquiera
frase = input("Ingrese una frase para invertir el orden de las palabras: ")

# Llamamos a la función que usa una pila para invertir el orden de las palabras
frase_invertida = invertir_frase(frase)

# Mostramos el resultado en pantalla
print("Frase invertida:", frase_invertida)