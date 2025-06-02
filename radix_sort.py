def counting_sort_digito(lista, exp):
    """
    Counting Sort adaptado para o dígito específico (exp = 1, 10, 100, ...).
    """
    n = len(lista)
    output = [0] * n
    contagem = [0] * 10  # Dígitos de 0 a 9

    # Conta as ocorrências de cada dígito
    for num in lista:
        indice = (num // exp) % 10
        contagem[indice] += 1

    # Atualiza a contagem para posições acumuladas
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    # Constrói o output (lista ordenada parcialmente)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        output[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1
        i -= 1

    # Copia o output para a lista original
    for i in range(n):
        lista[i] = output[i]

def radix_sort(lista):
    """
    Função principal do Radix Sort.

    Vantagens: rápido para inteiros pequenos, mantém a ordem dos números repetidos

    Desvantagens: ineficiente para números muito grandes, ocupa mais espaço na hora de rodar.

    Obs.: Complexidade O(d * (n + k)) onde d é o número de dígitos dos maiores números, n é o número de elementos, k é a base (ex: 10 para decimal).
    """
    if not lista:
        return

    # Encontra o maior número para saber o número de dígitos
    max_num = max(lista)

    # Ordena por cada dígito, começando pelas unidades
    exp = 1
    while max_num // exp > 0:
        counting_sort_digito(lista, exp)
        exp *= 10

# Exemplo de uso
numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", numeros)

radix_sort(numeros)
print("Lista ordenada:", numeros)
