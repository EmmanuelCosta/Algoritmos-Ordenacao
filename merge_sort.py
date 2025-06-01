def merge_sort(lista):
    """
    Função que implementa o algoritmo Merge Sort.
    Ordena a lista fornecida em ordem crescente.

    Vantagem: performance se mantem igual independente da entrada, não vai mexer em números iguais

    Desvantagens: não é tão ideal para listas pequenas, usa mais espaço para criar listas auxiliares
    """
    if len(lista) > 1:
        # Encontra o ponto médio da lista
        meio = len(lista) // 2
        esquerda = lista[:meio]  # Primeira metade
        direita = lista[meio:]   # Segunda metade

        # Chama recursivamente o merge_sort para cada metade
        merge_sort(esquerda)
        merge_sort(direita)

        # Índices para percorrer as sublistas e a lista principal
        i = j = k = 0

        # Mescla as sublistas ordenadas na lista principal
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1


            # (5, 4, 3, 2) 
            # (esquerda = (5,4) direita = (3,2) (
            # chamar a funcao novamente: esquerda da esquerda:(5) direita da esquerta:(4) (3) (2)
            #))
            #

        # Adiciona os elementos restantes da esquerda (se houver)
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da direita (se houver)
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

# --------------------------------------------
# Lista fixa de exemplo
# --------------------------------------------

numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numeros)

# Chama a função de ordenação
merge_sort(numeros)

# Exibe a lista ordenada
print("Lista ordenada:", numeros)
