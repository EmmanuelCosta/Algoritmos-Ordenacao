def bucket_sort(lista):
    """
    Implementação simples do Bucket Sort para números entre 0 e 1.
    Bucket Sort é um algoritmo que divide os dados em vários "baldes" (subgrupos), ordena cada balde individualmente 
    (geralmente com um algoritmo simples como Insertion Sort) e depois junta tudo para formar o array ordenado.

    Vantagens: Muito eficiente para floats uniformes, rasoavelmente facil de implementar.

    Desvantagens: Exige conhecimento do intervalo dos numeros, usa listas extras para auxiliar.
    Obs.: Complexidade de tempo vai depender da distribuição dos buckets e qual algoritmo de ordenação  vai ser feito dentro do bucket. 
    O(n+k) onde n é o número de elementos e k é o número de buckets.
    """
    n = len(lista)
    if n == 0:
        return lista

    # Passo 1: Criar os buckets
    buckets = [[] for _ in range(n)]

    # Passo 2: Distribuir os elementos nos buckets
    for num in lista:
        # Supondo números entre 0 e 1 (para valores fora desse intervalo, ajustar a fórmula)
        indice = int(num * n)
        if indice == n:
            indice = n - 1  # Se o valor for 1.0, evita índice fora da lista
        buckets[indice].append(num)

    # Passo 3: Ordenar cada bucket
    for bucket in buckets:
        bucket.sort()  # Pode usar Insertion Sort ou outro

    # Passo 4: Concatenar os buckets
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado

# Exemplo de uso
numeros = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Lista original:", numeros)

ordenada = bucket_sort(numeros)
print("Lista ordenada:", ordenada)
