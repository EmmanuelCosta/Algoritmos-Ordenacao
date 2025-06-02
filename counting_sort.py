def counting_sort(lista):
    """
    Implementação do Counting Sort.
    Ordena uma lista de inteiros não negativos.
    Ordenar um array de números inteiros quando o intervalo dos valores (mínimo e máximo) é conhecido e não é muito grande.

    Vantagem: Muito rapido para listas pequenas, não vai perder tempo com números iguais(repetidos)
    
    Desvantagens: Só pode ser usado com números inteiros, não deve ser usado com listas grandes.

    Obs.: Complexidade O(n + k) onde n = número de elementos no array de entrada, k = tamanho do intervalo dos valores
    """
    if not lista:
        return []

    # Passo 1: Descobrir o maior valor da lista
    max_valor = max(lista)

    # Passo 2: Criar um array de contagem (tamanho = max_valor + 1)
    contagem = [0] * (max_valor + 1)

    # Passo 3: Contar as ocorrências de cada número
    for num in lista:
        contagem[num] += 1

    # Passo 4: Reconstruir a lista ordenada
    resultado = []
    for i, freq in enumerate(contagem):
        resultado.extend([i] * freq)  # Adiciona o número 'i' 'freq' vezes

    return resultado

# Exemplo de uso
numeros = [4, 2, 2, 8, 3, 3, 1]
print("Lista original:", numeros)

ordenada = counting_sort(numeros)
print("Lista ordenada:", ordenada)
