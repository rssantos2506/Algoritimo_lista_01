def quick_sort(element_list):
    """
    Algoritmo: Quick Sort (Ordenação Rápida)
    
    Como funciona:
    Escolhe um elemento de referência chamado 'pivô'. Particiona o restante 
    da lista em duas subpartes: uma contendo os elementos menores que o pivô e 
    outra com os maiores. O processo é repetido recursivamente nas subpartes.
    
    Complexidade:
    - Melhor e Médio Caso: O(N log N)
    - Pior Caso (pivô mal escolhido): O(N²)
    - Espaço Auxiliar: O(log N) devido à pilha de recursão
    
    Vantagens: Um dos algoritmos mais rápidos na prática para uso geral; in-place eficiente.
    Desvantagens: Instável e vulnerável a piores casos com escolhas ruins de pivô.
    """
    if len(element_list) <= 1:
        return element_list
        
    pivot = element_list[len(element_list) // 2]
    smaller_elements = [x for x in element_list if x < pivot]
    equal_elements = [x for x in element_list if x == pivot]
    larger_elements = [x for x in element_list if x > pivot]
    
    return quick_sort(smaller_elements) + equal_elements + quick_sort(larger_elements)