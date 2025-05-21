# Importamos la función desde funciones2.py
from funciones2 import parentesis_balanceados

# Solicitamos al usuario una cadena de texto
cadena = input("Ingrese una cadena con paréntesis (), [], {}: ")

# Verificamos si los paréntesis están balanceados
if parentesis_balanceados(cadena):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis NO están balanceados.")