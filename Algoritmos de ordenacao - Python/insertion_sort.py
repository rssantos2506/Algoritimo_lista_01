def insertion_sort(element_list):
    """
    Algoritmo: Insertion Sort (Ordenação por Inserção)
    
    Como funciona:
    Constrói a lista ordenada final iterando elemento por elemento. Cada novo 
    elemento é comparado com os elementos anteriores (já ordenados) e inserido 
    na sua posição correta, deslocando os maiores elementos para a direita.
    
    Complexidade:
    - Pior e Médio Caso: O(N²)
    - Melhor Caso (quase ordenada): O(N)
    - Espaço Auxiliar: O(1)
    
    Vantagens: Excelente performance em listas pequenas ou quase ordenadas; estável.
    Desvantagens: Lento para grandes conjuntos devido ao deslocamento contínuo de itens.
    """
    for i in range(1, len(element_list)):
        current_key = element_list[i]
        position = i - 1
        while position >= 0 and element_list[position] > current_key:
            element_list[position + 1] = element_list[position]
            position -= 1
        element_list[position + 1] = current_key
    return element_list