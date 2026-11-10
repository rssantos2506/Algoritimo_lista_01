def selection_sort(element_list):
    """
    Algoritmo: Selection Sort (Ordenação por Seleção)
    
    Como funciona:
    Divide a lista conceitualmente em duas partes: a sublista ordenada (à esquerda) 
    e a sublista não ordenada (à direita). A cada passo, o algoritmo varre a sublista 
    não ordenada para encontrar o menor elemento, trocando-o de posição com o primeiro 
    elemento não ordenado, expandindo a parte ordenada em uma unidade.
    
    Complexidade:
    - Pior, Médio e Melhor Caso: O(N²)
    - Espaço Auxiliar: O(1) (In-place)
    
    Vantagens: Simples de implementar e realiza o número mínimo de trocas (máximo O(N)).
    Desvantagens: Desempenho quadrático, tornando-se inviável para grandes volumes.
    """
    n = len(element_list)
    for current_index in range(n):
        min_index = current_index
        for j in range(current_index + 1, n):
            if element_list[j] < element_list[min_index]:
                min_index = j
        if min_index != current_index:
            element_list[current_index], element_list[min_index] = element_list[min_index], element_list[current_index]
    return element_list