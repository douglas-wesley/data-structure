def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o ponto médio da lista
        left_half = arr[:mid] # Divide a lista em duas metades
        right_half = arr[mid:]

        merge_sort(left_half)   # Ordena a primeira metade recursivamente
        merge_sort(right_half)  # Ordena a segunda metade recursivamente

        # Agora, mescla as duas metades ordenadas
        i = j = k = 0

        # Copia dados para as listas temporárias left_half e right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se algum elemento restou na left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica se algum elemento restou na right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Exemplo prático
print("\n--- Merge Sort ---")
lista_merge = [38, 27, 43, 3, 9, 82, 10]
print(f"Lista original: {lista_merge}")
lista_merge_ordenada = merge_sort(lista_merge)
print(f"Lista ordenada: {lista_merge_ordenada}") # Saída: [3, 9, 10, 27, 38, 43, 82]