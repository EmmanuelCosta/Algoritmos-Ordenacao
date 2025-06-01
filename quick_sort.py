def quick_sort(lista):
    """
    Função que implementa o algoritmo Quick Sort.
    Ordena a lista fornecida em ordem crescente.

    Vantagem: rapido de implementar, não tão complexo

    Desvantagem: performance pode ser pior dependendo do pivo, vai rodar mesmo que os numeros já estejam
    na ordem certa
    """
    if len(lista) <= 1:
        return lista  # Lista com 0 ou 1 elemento já está ordenada

    # Escolhe o elemento "pivô" (neste caso, o último)
    pivo = lista[-1]

    # Cria listas para os menores, iguais e maiores que o pivô
    menores = [x for x in lista[:-1] if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista[:-1] if x > pivo]

    print(f"Pivô escolhido: {pivo}")
    print(f"Menores: {menores}, Iguais: {iguais}, Maiores: {maiores}")

    # Chama o Quick Sort recursivamente nas partes
    return quick_sort(menores) + iguais + quick_sort(maiores)

# --------------------------------------------
# Lista fixa de exemplo
# --------------------------------------------
numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numeros)

# Chama a função de ordenação
numeros_ordenados = quick_sort(numeros)

print("Lista ordenada:", numeros_ordenados)
