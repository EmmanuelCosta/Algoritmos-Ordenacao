def bubble_sort(lista):
    """
    Função que implementa o algoritmo de ordenação Bubble Sort.
    Bubble Sort é um algoritmo de ordenação simples que funciona comparando elementos adjacentes e trocando-os de lugar se estiverem na ordem errada. 
    Isso faz com que os maiores (ou menores) valores "borbulhem" para o final da lista, daí o nome "bubble".

    
    Vantagens: um pouco simples de implementar, se os elementos forem iguais não precisa realizar troca.

    Desvantagens: ruim com listas grandes visto que pode ter que percorrer a lista várias vezes até 
    organiza-la. Complexidade de tempo O(n^2).
    """
    n = len(lista)
    
    # Percorre a lista várias vezes
    for i in range(n - 1):
        # variável para verificar se houve troca nesta passada
        trocou = False
        
        # Para cada par de elementos adjacentes
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # Troca se os elementos estiverem fora de ordem
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        # se nenhuma troca aconteceu, a lista já está ordenada
        if not trocou:
            break

# Exemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

bubble_sort(numeros)
print("Lista ordenada:", numeros)
