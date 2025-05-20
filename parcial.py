filas = 0
columnas = 0
tiene_puntos = False

while True:
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    if filas == 0 and columnas == 0:
        break

    matriz = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1}: ").split()))
        matriz.append(fila)

    tiene_puntos = False

    for i in range(filas):
        min_fila = matriz[i][0]
        for j in range(1, columnas):
            if matriz[i][j] < min_fila:
                min_fila = matriz[i][j]

        for j in range(columnas):
            max_columna = matriz[0][j]
            for k in range(1, filas):
                if matriz[k][j] > max_columna:
                    max_columna = matriz[k][j]

            if matriz[i][j] == min_fila and matriz[i][j] == max_columna:
                tiene_puntos = True
                break

        if tiene_puntos:
            break

    if tiene_puntos:
        print("SI")
    else:
        print("NO")