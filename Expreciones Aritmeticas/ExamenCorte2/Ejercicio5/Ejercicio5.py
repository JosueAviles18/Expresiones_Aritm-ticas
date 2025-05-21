# Clase Nodo para representar cada elemento de la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor     # Valor del nodo
        self.siguiente = None  # Referencia al siguiente nodo

# Clase ListaEnlazada que permite insertar y buscar valores
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista enlazada

    def insertar(self, valor):
        # Crear un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)

        if not self.cabeza:
            # Si la lista está vacía, el nuevo nodo es la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Si no, recorremos hasta el final y lo agregamos al final
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, valor):
        # Busca el valor y retorna su posición (iniciando en 0), o None si no está
        actual = self.cabeza
        posicion = 0

        while actual:
            if actual.valor == valor:
                return posicion  # Valor encontrado, retornar posición
            actual = actual.siguiente
            posicion += 1

        return None  # Valor no encontrado