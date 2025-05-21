# Definimos una clase llamada Pila para implementar la estructura tipo LIFO (Last In, First Out)
class Pila:
    def __init__(self):
        # Lista interna para almacenar los elementos de la pila
        self.items = []

    def esta_vacia(self):
        # Verifica si la pila está vacía (True si no hay elementos)
        return len(self.items) == 0

    def apilar(self, item):
        # Agrega un elemento al tope de la pila
        self.items.append(item)

    def desapilar(self):
        # Elimina y retorna el elemento en el tope de la pila
        return self.items.pop()

# Función que recibe una frase y devuelve la misma frase con las palabras en orden invertido
def invertir_frase(frase):
    pila = Pila()  # Creamos una pila vacía

    palabras = frase.split()  # Dividimos la frase en palabras usando el espacio como separador

    # Apilamos cada palabra en la pila
    for palabra in palabras:
        pila.apilar(palabra)

    frase_invertida = []  # Lista que contendrá las palabras en orden invertido

    # Sacamos las palabras de la pila en orden LIFO (última en entrar, primera en salir)
    while not pila.esta_vacia():
        frase_invertida.append(pila.desapilar())

    # Unimos las palabras invertidas con espacios y retornamos el resultado
    return ' '.join(frase_invertida)