# Clase que representa un elemento con prioridad
class Elemento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre              # Nombre del elemento
        self.prioridad = prioridad        # Prioridad (número entero, menor = más prioritario)

# Clase que implementa la cola de prioridad
class ColaPrioridad:
    def __init__(self):
        # Lista que usaremos como la cola principal
        self.cola = []

    def encolar(self, nombre, prioridad):
        # Crea un nuevo elemento y lo agrega a la cola
        nuevo = Elemento(nombre, prioridad)
        self.cola.append(nuevo)

    def desencolar(self):
        if not self.cola:
            return None  # Si la cola está vacía, no hay nada que desencolar

        # Buscar el elemento con la mayor prioridad (menor número)
        indice_prioritario = 0
        for i in range(1, len(self.cola)):
            if self.cola[i].prioridad < self.cola[indice_prioritario].prioridad:
                indice_prioritario = i

        # Sacamos el elemento de la lista y lo retornamos
        return self.cola.pop(indice_prioritario)

    def mostrar_cola(self):
        # Retorna la lista de elementos con sus prioridades como texto
        return [(e.nombre, e.prioridad) for e in self.cola]