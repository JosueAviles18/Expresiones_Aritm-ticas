# Importamos la clase ListaEnlazada desde funciones5.py
from funciones5 import ListaEnlazada

# Creamos una nueva lista enlazada vacía
lista = ListaEnlazada()

# Menú interactivo para insertar y buscar valores
while True:
    print("\n--- Menú Lista Enlazada ---")
    print("1. Insertar valor")
    print("2. Buscar valor")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        valor = input("Ingrese el valor a insertar: ")
        lista.insertar(valor)
        print("Valor insertado en la lista.")
    elif opcion == '2':
        valor = input("Ingrese el valor a buscar: ")
        posicion = lista.buscar(valor)
        if posicion is not None:
            print(f"Valor encontrado en la posición {posicion}.")
        else:
            print("Valor no encontrado en la lista.")
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")