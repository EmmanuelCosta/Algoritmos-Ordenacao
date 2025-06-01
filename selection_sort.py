def selection_sort(lista):
    """
    Função que implementa o algoritmo de ordenação Selection Sort.
    Ordena a lista fornecida em ordem crescente.

    Vantagens: Facil de implementar, funciona bem com listas pequenas.

    Desvantagens: sempre vai rodar a lista inteira sendo ruim para listas grandes,
    pode alternar números iguais, sempre vai fazer o mesmo número de comparações
    independente da ordem que a lista começar.
    """
    n = len(lista)
    
    # Percorre toda a lista
    for i in range(n - 1):
        # Assume que o menor elemento está na posição atual
        indice_min = i
        
        # Percorre o restante da lista para encontrar o menor elemento
        for j in range(i + 1, n):
            if lista[j] < lista[indice_min]:
                indice_min = j
        
        # Troca o menor elemento encontrado com o elemento atual
        lista[i], lista[indice_min] = lista[indice_min], lista[i]

# Exemplo de uso

numeros = [64, 25, 12, 22, 11]
print("Lista original:", numeros)

selection_sort(numeros)
print("Lista ordenada:", numeros)
