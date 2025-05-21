# Importamos la clase ListaReproduccion desde funciones3.py
from funciones3 import ListaReproduccion

# Creamos una nueva lista de reproducción
lista = ListaReproduccion()

# Menú interactivo simple para probar las funciones
while True:
    print("\n--- Menú Lista de Reproducción ---")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Reproducir siguiente canción")
    print("4. Reproducir canción anterior")
    print("5. Mostrar lista de reproducción")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre de la canción: ")
        lista.agregar_cancion(nombre)
        print("Canción agregada.")
    elif opcion == '2':
        nombre = input("Ingrese el nombre de la canción a eliminar: ")
        if lista.eliminar_cancion(nombre):
            print("Canción eliminada.")
        else:
            print("Canción no encontrada.")
    elif opcion == '3':
        print("Reproduciendo:", lista.reproducir_siguiente())
    elif opcion == '4':
        print("Reproduciendo:", lista.reproducir_anterior())
    elif opcion == '5':
        print("Lista de reproducción actual:")
        for cancion in lista.mostrar_lista():
            print("-", cancion)
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")