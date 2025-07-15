def insertion_sort(arr):
    # Percorre de 1 até o tamanho do array
    for i in range(1, len(arr)):
        key = arr[i] # Elemento a ser inserido
        j = i - 1    # Posição do elemento anterior

        # Move os elementos de arr[0..i-1], que são maiores que key,
        # uma posição à frente de sua posição atual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key # Insere a chave na posição correta
    return arr

# Exemplo prático
print("\n--- Insertion Sort ---")
lista_insertion = [12, 11, 13, 5, 6]
print(f"Lista original: {lista_insertion}")
lista_insertion_ordenada = insertion_sort(lista_insertion)
print(f"Lista ordenada: {lista_insertion_ordenada}") # Saída: [5, 6, 11, 12, 13]