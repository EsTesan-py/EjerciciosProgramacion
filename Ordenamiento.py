#BURBUJA
def bubble_sort(arr):#Se define la funcion
    n = len(arr)#Se obtiene el largo del vector
    for i in range(n - 1):#Se itera hasta el largo del vector menos uno
        for j in range(0, n - i - 1):#
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Arreglo ordenado mediante el método de burbuja:")
print(array)
#BURBUJA 2
vector=[10,20,30,15,5,25,40,105,45]
bandera=False
while bandera==False:
    bandera=True
    for i in range(len(vector)-1):
        if vector[i]>vector[i+1]:
            aux=vector[i]
            vector[i]=vector[i+1]
            vector[i+1]=vector[i]
            bandera=False
print(vector)

#QUICKSORT
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Ejemplo de uso
array = [64, 34, 25, 12, 22, 11, 90]
quick_sort(array, 0, len(array) - 1)
print("Arreglo ordenado mediante el método de Quicksort:")
print(array)