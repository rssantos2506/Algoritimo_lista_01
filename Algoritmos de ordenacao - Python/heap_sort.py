def heap_sort(element_list):
    """
    Algoritmo: Heap Sort
    
    Como funciona:
    Organiza os dados em uma árvore binária implícita chamada Heap Máximo, 
    onde o elemento pai é sempre maior ou igual aos seus filhos. O maior elemento 
    da raiz é trocado com o último elemento da lista, reduzindo o tamanho do 
    heap e repetindo o ajuste (heapify) até ordenar toda a estrutura.
    
    Complexidade:
    - Pior, Médio e Melhor Caso: O(N log N) garantido
    - Espaço Auxiliar: O(1) (In-place)
    
    Vantagens: Garantia de tempo O(N log N) sem consumir memória extra considerável.
    Desvantagens: Instável e possui baixa localidade de referência em memória (cache misses).
    """
    n = len(element_list)

    def heapify(arr, heap_size, root_index):
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2

        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != root_index:
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            heapify(arr, heap_size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(element_list, n, i)

    for i in range(n - 1, 0, -1):
        element_list[i], element_list[0] = element_list[0], element_list[i]
        heapify(element_list, i, 0)

    return element_list