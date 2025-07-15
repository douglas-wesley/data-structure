def heapify(arr, n, i):
    """
    Função auxiliar para transformar um sub-árvore com raiz no índice i em um heap.
    n é o tamanho do heap.
    """
    largest = i  # Inicializa o maior como a raiz
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Se o filho esquerdo for maior que a raiz
    if left_child < n and arr[largest] < arr[left_child]:
        largest = left_child

    # Se o filho direito for maior que o maior até agora
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        # Heapify recursivamente a sub-árvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo (reorganiza o array)
    # Começa do último nó pai e vai até a raiz
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        # Move a raiz atual para o final
        arr[i], arr[0] = arr[0], arr[i]
        # Chama heapify na heap reduzida
        heapify(arr, i, 0)
    return arr

# Exemplo prático
print("\n--- Heap Sort ---")
lista_heap = [12, 11, 13, 5, 6, 7]
print(f"Lista original: {lista_heap}")
lista_heap_ordenada = heap_sort(lista_heap)
print(f"Lista ordenada: {lista_heap_ordenada}") # Saída: [5, 6, 7, 11, 12, 13]