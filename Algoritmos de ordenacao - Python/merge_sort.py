def merge_sort(element_list):
    """
    Algoritmo: Merge Sort (Ordenação por Intercalação)
    
    Como funciona:
    Utiliza a estratégia de Divisão e Conquista. Divide recursivamente a lista 
    ao meio até que cada sublista contenha apenas um elemento. Em seguida, 
    combina (merge) essas sublistas de forma ordenada, interligando-as até 
    recompor a lista completa e ordenada.
    
    Complexidade:
    - Pior, Médio e Melhor Caso: O(N log N) garantido
    - Espaço Auxiliar: O(N) (Não é in-place)
    
    Vantagens: Desempenho previsível e rápido para grandes volumes; algoritmo estável.
    Desvantagens: Requer memória adicional proporcional ao tamanho da lista.
    """
    if len(element_list) <= 1:
        return element_list

    mid_index = len(element_list) // 2
    left_half = merge_sort(element_list[:mid_index])
    right_half = merge_sort(element_list[mid_index:])

    return _merge_halves(left_half, right_half)


def _merge_halves(left_half, right_half):
    merged_list = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_list.append(left_half[i])
            i += 1
        else:
            merged_list.append(right_half[j])
            j += 1
    merged_list.extend(left_half[i:])
    merged_list.extend(right_half[j:])
    return merged_list