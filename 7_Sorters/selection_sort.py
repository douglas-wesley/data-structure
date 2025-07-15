def selection_sort(arr):
    n = len(arr)
    # Percorre toda a lista
    for i in range(n):
        # Encontra o índice do menor elemento na porção não ordenada
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplo prático
print("\n--- Selection Sort ---")
lista_selection = [64, 25, 12, 22, 11]
print(f"Lista original: {lista_selection}")
lista_selection_ordenada = selection_sort(lista_selection)
print(f"Lista ordenada: {lista_selection_ordenada}") # Saída: [11, 12, 22, 25, 64]