def tiene_punto_de_silla(matriz):
    for i in range(len(matriz)):
        fila_max = max(matriz[i])
        indices_max_fila = [index for index, value in enumerate(matriz[i]) if value == fila_max]

        for j in indices_max_fila:
            columna = [matriz[k][j] for k in range(len(matriz))]
            if matriz[i][j] == max(columna):
                continue
            else:
                return "NO"

    return "SI"


def main():
    while True:
        filas, columnas = map(int, input().split())
        
        if filas == 0 and columnas == 0:
            break
        
        matriz = []
        for _ in range(filas):
            fila = list(map(int, input().split()))
            matriz.append(fila)
        
        resultado = tiene_punto_de_silla(matriz)
        print(resultado)


if __name__ == "__main__":
    main()