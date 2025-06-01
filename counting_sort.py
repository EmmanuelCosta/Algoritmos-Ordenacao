def counting_sort(lista):
    """
    Implementação do Counting Sort.
    Ordena uma lista de inteiros não negativos.

    Vantagem: Muito rapido para listas pequenas, não vai perder tempo com números iguais(repetidos)

    Desvantagens: Só pode ser usado com números inteiros, não deve ser usado com listas grandes.
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
