def insertion_sort(lista):
    """
    Função que implementa o algoritmo de ordenação Insertion Sort.
    Ordena a lista fornecida em ordem crescente.

    Vantagens: Facil de entender, bom para listas pequenas, não realiza troca de elementos iguas.

    Desvantagens: vai realizar várias interações para mudar os elementos de lugar e será muito 
    ineficiente com listas muito grandes.
    """
    n = len(lista)
    
    # Percorre a lista a partir do segundo elemento
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        
        # Move os elementos maiores que a chave uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insere a chave na posição correta
        lista[j + 1] = chave

# Exemplo de uso
numeros = [12, 11, 13, 5, 6]
print("Lista original:", numeros)

insertion_sort(numeros)
print("Lista ordenada:", numeros)
