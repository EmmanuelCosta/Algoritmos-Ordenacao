def funcao_auxiliar(lista, n, i):
    """
    Função auxiliar para transformar a lista em um heap.
    - n: tamanho da lista
    - i: índice do nó raiz a ser ajustado

    """
    maior = i        # Inicialmente, o maior é a raiz
    esquerda = 2 * i + 1  # Índice do filho esquerdo
    direita = 2 * i + 2   # Índice do filho direito

    # Verifica se o filho da esquerda é maior que a raiz
    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    # Verifica se o filho da direita é maior que o maior até agora
    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    # Se o maior não for a raiz, troca e ajusta a subárvore
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        # Chama o heapify recursivamente no nó afetado
        funcao_auxiliar(lista, n, maior)

def heap_sort(lista):
    """
    Transforma o array em um heap, depois extrai o maior elemento repetidamente, reorganizando o heap até ordenar tudo.
    
    Vantagens: Util para grandes listas, complexidade não vai mudar.

    Desvantagens: pode gastar tempo com valores iguais, mais complexo de implementar.
    
    Função que implementa o algoritmo Heap Sort.
    Ordena a lista em ordem crescente.
        
    """
    n = len(lista)

    # Passo 1: Constrói o heap máximo (max heap)
    for i in range(n // 2 - 1, -1, -1):
        funcao_auxiliar(lista, n, i)

    # Passo 2: Remove elementos do heap, um por um
    for i in range(n - 1, 0, -1):
        # Troca a raiz (maior) com o último elemento
        lista[i], lista[0] = lista[0], lista[i]
        # Ajusta o heap reduzido
        funcao_auxiliar(lista, i, 0)

# --------------------------------------------
# Lista fixa de exemplo
# --------------------------------------------
numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numeros)

heap_sort(numeros)

print("Lista ordenada:", numeros)
