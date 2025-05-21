# Clase para implementar una pila básica
class Pila:
    def __init__(self):
        # La pila se almacena en una lista interna
        self.items = []

    def esta_vacia(self):
        # Retorna True si la pila no contiene elementos
        return len(self.items) == 0

    def apilar(self, item):
        # Agrega un elemento al final de la lista (top de la pila)
        self.items.append(item)

    def desapilar(self):
        # Elimina y retorna el último elemento de la lista (top de la pila)
        return self.items.pop()

    def cima(self):
        # Retorna el último elemento sin eliminarlo (útil para validaciones)
        return self.items[-1] if not self.esta_vacia() else None

# Función para verificar si los paréntesis están balanceados en una cadena
def parentesis_balanceados(cadena):
    pila = Pila()  # Creamos una pila vacía

    # Diccionario que relaciona cada paréntesis de cierre con su apertura correspondiente
    pares = {')': '(', ']': '[', '}': '{'}

    # Recorremos cada carácter de la cadena
    for caracter in cadena:
        if caracter in '([{':
            # Si el carácter es un paréntesis de apertura, lo apilamos
            pila.apilar(caracter)
        elif caracter in ')]}':
            # Si es un paréntesis de cierre:
            if pila.esta_vacia():
                # Si no hay nada que cerrar, entonces no está balanceado
                return False
            if pila.desapilar() != pares[caracter]:
                # Si el paréntesis que se cierra no corresponde al último que se abrió
                return False

    # Si al final la pila está vacía, todos los paréntesis estaban balanceados
    return pila.esta_vacia()