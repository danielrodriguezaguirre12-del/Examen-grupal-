# Operación que desplaza circularmente las filas de la matriz de estado

def shift_rows(state):
    """
    Aplica la transformación Shift Rows a la matriz de estado 4x4
    - Fila 0: sin cambios
    - Fila 1: desplazamiento circular izquierdo de 1 posición
    - Fila 2: desplazamiento circular izquierdo de 2 posiciones
    - Fila 3: desplazamiento circular izquierdo de 3 posiciones
    """
    result = [[0 for _ in range(4)] for _ in range(4)]
    
    # Fila 0: sin cambios
    result[0] = state[0][:]
    
    # Fila 1: shift left 1
    result[1] = state[1][1:] + state[1][:1]
    
    # Fila 2: shift left 2
    result[2] = state[2][2:] + state[2][:2]
    
    # Fila 3: shift left 3
    result[3] = state[3][3:] + state[3][:3]
    
    return result

# Ejemplo de uso
if __name__ == "__main__":
    # Matriz de estado de ejemplo (4x4)
    state = [
        [0x00, 0x01, 0x02, 0x03],
        [0x10, 0x11, 0x12, 0x13],
        [0x20, 0x21, 0x22, 0x23],
        [0x30, 0x31, 0x32, 0x33]
    ]
    
    print("Estado original:")
    for row in state:
        print([hex(x) for x in row])
    
    # Aplicar Shift Rows
    shifted = shift_rows(state)
    
    print("\nDespués de Shift Rows:")
    for row in shifted:
        print([hex(x) for x in row])
