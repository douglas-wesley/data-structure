def bubble_sort(arr):
    n = len(arr)
    # Loop para percorrer todos os elementos da lista
    for i in range(n - 1):
        # Flag para otimização: se nenhuma troca ocorrer em uma passagem, a lista está ordenada
        swapped = False
        # Últimos i elementos já estão no lugar
        for j in range(0, n - i - 1):
            # Compara elementos adjacentes
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Troca
                swapped = True
        # Se não houve trocas nesta passagem, a lista está ordenada
        if not swapped:
            break
    return arr

# Exemplo prático
print("\n--- Bubble Sort ---")
lista_bubble = [5, 1, 4, 2, 8]
print(f"Lista original: {lista_bubble}")
lista_bubble_ordenada = bubble_sort(lista_bubble)
print(f"Lista ordenada: {lista_bubble_ordenada}") # Saída: [1, 2, 4, 5, 8]