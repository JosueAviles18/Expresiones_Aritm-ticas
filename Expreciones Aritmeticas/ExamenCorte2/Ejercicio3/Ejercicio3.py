# Clase Nodo que representa cada canción en la lista de reproducción
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre       # Nombre de la canción
        self.siguiente = None      # Puntero a la siguiente canción
        self.anterior = None       # Puntero a la canción anterior

# Clase ListaReproduccion que usa una lista doblemente enlazada
class ListaReproduccion:
    def __init__(self):
        self.primera = None   # Primer nodo (canción) de la lista
        self.actual = None    # Nodo actual que está siendo reproducido

    def agregar_cancion(self, nombre):
        nueva = NodoCancion(nombre)  # Creamos un nuevo nodo con el nombre de la canción

        if self.primera is None:
            # Si la lista está vacía, esta canción será la primera y la actual
            self.primera = nueva
            self.actual = nueva
        else:
            # Recorremos hasta el final para insertar la nueva canción
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nueva
            nueva.anterior = temp

    def eliminar_cancion(self, nombre):
        temp = self.primera

        while temp:
            if temp.nombre == nombre:
                # Si encontramos la canción, la eliminamos ajustando los punteros
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                else:
                    self.primera = temp.siguiente  # Si es la primera, actualizamos el inicio

                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior

                if self.actual == temp:
                    self.actual = temp.siguiente or temp.anterior

                return True  # Canción eliminada con éxito
            temp = temp.siguiente
        return False  # No se encontró la canción

    def reproducir_siguiente(self):
        # Avanza al siguiente nodo si existe
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            return self.actual.nombre
        return "No hay siguiente canción."

    def reproducir_anterior(self):
        # Retrocede al nodo anterior si existe
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            return self.actual.nombre
        return "No hay canción anterior."

    def mostrar_lista(self):
        # Muestra todos los nombres de las canciones en la lista
        temp = self.primera
        canciones = []
        while temp:
            canciones.append(temp.nombre)
            temp = temp.siguiente
        return canciones