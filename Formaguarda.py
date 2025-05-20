def formaguarda(N, tipo, patron):
    colores = "abcdefghijklmnopqrstuvwxyz"
    guarda = ""
    
    if tipo == "NORMAL":
        while len(guarda) < N:
            guarda += patron
    
    elif tipo == "ESPEJADA":
        while len(guarda) < N:
            guarda += patron
            patron_inverso = patron[::-1]
            guarda += patron_inverso

    return guarda[:N]
N, tipo = input().split()
patron = input()
resultado = formaguarda(int(N), tipo, patron)
print(resultado)