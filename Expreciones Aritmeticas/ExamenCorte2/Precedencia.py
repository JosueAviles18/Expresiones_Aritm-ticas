# Función que devuelve la precedencia de los operadores
def precedencia(op):
    if op == '(':            # El paréntesis de apertura tiene menor precedencia
        return 0
    elif op in '+-':         # Suma y resta tienen precedencia 1
        return 1
    elif op in '*/':         # Multiplicación y división tienen precedencia 2
        return 2
    else:                    # Cualquier otro símbolo (no válido)
        return -1

# Función para convertir una expresión infija a postfija (notación polaca inversa)
def conv_postfija(EI):
    PILA = []      # Pila para operadores
    EPOS = ''      # Cadena para la expresión postfija
    
    # Recorrer cada símbolo de la expresión infija
    for simb in EI:
        if simb.isalnum():   # Si el símbolo es un operando (letra o número)
            EPOS += simb     # Se agrega directamente a la salida postfija
        else:
            if simb == '(':   # Si es un paréntesis de apertura
                PILA.append(simb)  # Se coloca en la pila
            elif simb == ')': # Si es un paréntesis de cierre
                # Sacar operadores de la pila hasta encontrar el paréntesis de apertura
                while PILA and PILA[-1] != '(':
                    EPOS += PILA.pop()
                PILA.pop()  # Eliminar el paréntesis de apertura '(' de la pila
            else:  # Si es un operador (+, -, *, /)
                # Sacar operadores con mayor o igual precedencia que el actual
                while PILA and precedencia(PILA[-1]) >= precedencia(simb):
                    EPOS += PILA.pop()
                PILA.append(simb)  # Colocar el nuevo operador en la pila
    
    # Vaciar la pila al final del recorrido, agregando los operadores restantes
    while PILA:
        EPOS += PILA.pop()
    
    return EPOS  # Devolver la expresión convertida a postfija

# Parte principal del programa
# Solicitar al usuario que ingrese una expresión infija sin espacios
expresion_infija = input("Ingrese la expresión infija (sin espacios): ")

# Convertir la expresión a notación postfija
expresion_postfija = conv_postfija(expresion_infija)

# Mostrar el resultado
print("Expresión en notación postfija:", expresion_postfija)
