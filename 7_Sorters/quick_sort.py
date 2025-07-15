def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        maiores = [i for i in array[1:] if i < pivo]
        menores = [i for i in array[1:] if i >= pivo]
        return quick_sort(maiores) + [pivo] + quick_sort(menores)
    
print(quick_sort([3,2,4,5]))