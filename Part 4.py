# Function dimension
# Inputs: matriz, matriz de lista de listas, por referencia
# Outputs: filas, columnas, dimensión de la matriz.
def dimension(matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

# Function imprimir
# Inputs: A, matriz de lista de listas, por referencia
# Outputs: la matriz impresa en pantalla.
def imprimir(A):
    f, c = dimension(A)
    for i in range(0, f):
        print("| ", end="")
        for j in range(0, c):
            print("{:>5} |".format(A[i][j]), end="")
        print("")

# Function inicializar
# Inputs: nf, entero, por valor
#         nc, entero, por valor
# Outputs: A matriz de lista de listas, llena de ceros tamaño nf x nc
def inicializar(nf, nc):
    A = []
    for i in range(nf):
        fila = [0] * nc
        A.append(fila)
    return A

# Inputs: estado, matriz de estado (4x4) de lista de listas, por referencia
#         clave_redonda, matriz con los valores de la clave redonda (4x4), por referencia
# Outputs: resultado, matriz de lista de listas con el resultado de XOR (⊕)
def add_round_key(estado, clave_redonda):
    f, c = dimension(estado)
    resultado = inicializar(f, c)
    
    for i in range(f):
        for j in range(c):
            # Operación XOR entre cada elemento del estado y la clave redonda
            resultado[i][j] = estado[i][j] ^ clave_redonda[i][j]
    
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 50)
    print("DEMOSTRACIÓN: Add Round Key (AES)")
    print("=" * 50)
    
    # Matriz de estado inicial S (4x4)
    estado = [
        [0x19, 0xa0, 0x9a, 0xe9],
        [0x3d, 0xf4, 0x92, 0x11],
        [0xd6, 0xd1, 0x48, 0x6e],
        [0x27, 0x01, 0x0a, 0x20]
    ]
    
    # Clave redonda W (4x4) - valores de ejemplo
    clave_redonda = [
        [0xe0, 0x32, 0xfc, 0xf0],
        [0x90, 0x8f, 0x19, 0x4d],
        [0x2c, 0xdc, 0xf0, 0xdc],
        [0xd2, 0xd4, 0x2c, 0x4e]
    ]
    
    print("\nMatriz de Estado (S):")
    imprimir(estado)
    
    print("\nClave Redonda (W):")
    imprimir(clave_redonda)
    
    # Aplicar Add Round Key
    resultado = add_round_key(estado, clave_redonda)
    
    print("\nResultado después de Add Round Key (S ⊕ W):")
    imprimir(resultado)
    
    print("\n" + "=" * 50)
    print("Operación completada exitosamente")
    print("=" * 50)
