def bubble_sort(element_list):
    """
    Algoritmo: Bubble Sort (Ordenação por Bolha)
    
    Como funciona:
    Compara repetidamente pares de elementos adjacentes na lista. Se o elemento 
    da esquerda for maior que o da direita, eles trocam de lugar. Os maiores elementos 
    vão 'borbulhando' progressivamente para o final da lista a cada passada completa.
    
    Complexidade:
    - Pior e Médio Caso: O(N²)
    - Melhor Caso (já ordenada): O(N) devido à otimização de parada antecipada
    - Espaço Auxiliar: O(1)
    
    Vantagens: Muito intuitivo; detecta rapidamente se a lista já está ordenada.
    Desvantagens: Realiza muitas trocas e comparações redundantes, sendo muito lento.
    """
    n = len(element_list)
    for i in range(n):
        has_swapped = False
        for j in range(0, n - i - 1):
            if element_list[j] > element_list[j + 1]:
                element_list[j], element_list[j + 1] = element_list[j + 1], element_list[j]
                has_swapped = True
        if not has_swapped:
            break
    return element_list