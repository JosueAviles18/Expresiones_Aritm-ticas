# Importamos la clase ColaPrioridad desde funciones4.py
from funciones4 import ColaPrioridad

# Creamos una instancia de la cola de prioridad
cola = ColaPrioridad()

# Menú interactivo para gestionar la cola
while True:
    print("\n--- Menú Cola de Prioridad ---")
    print("1. Encolar elemento")
    print("2. Desencolar elemento con mayor prioridad")
    print("3. Mostrar cola actual")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del elemento: ")
        try:
            prioridad = int(input("Ingrese la prioridad (número, menor = mayor prioridad): "))
            cola.encolar(nombre, prioridad)
            print("Elemento encolado.")
        except ValueError:
            print("La prioridad debe ser un número entero.")
    elif opcion == '2':
        elemento = cola.desencolar()
        if elemento:
            print(f"Elemento desencolado: {elemento.nombre} (prioridad {elemento.prioridad})")
        else:
            print("La cola está vacía.")
    elif opcion == '3':
        print("Cola actual:")
        for nombre, prioridad in cola.mostrar_cola():
            print(f"- {nombre} (prioridad {prioridad})")
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")