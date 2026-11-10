from insertion_sort import insertion_sort

def bucket_sort(element_list, num_buckets=100):
    """
    Algoritmo: Bucket Sort (Ordenação por Baldes)
    
    Como funciona:
    Distribui os elementos uniformemente em vários compartimentos chamados baldes 
    (buckets). Cada balde individual é ordenado separadamente (utilizando outro 
    algoritmo, como Insertion Sort) e, por fim, os elementos de todos os baldes 
    são reunidos em sequência.
    
    Complexidade:
    - Melhor e Médio Caso: O(N + K) quando os dados são bem distribuídos
    - Pior Caso: O(N²) se todos os elementos caírem no mesmo balde
    - Espaço Auxiliar: O(N + K)
    
    Vantagens: Altamente eficiente quando os dados estão uniformemente distribuídos em um intervalo.
    Desvantagens: Sensível a distribuições irregulares de dados.
    """
    if not element_list:
        return element_list

    min_val = min(element_list)
    max_val = max(element_list)

    if min_val == max_val:
        return list(element_list)

    buckets = [[] for _ in range(num_buckets)]
    value_range = (max_val - min_val) / num_buckets

    for num in element_list:
        bucket_index = int((num - min_val) / value_range)
        if bucket_index == num_buckets:
            bucket_index = num_buckets - 1
        buckets[bucket_index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort(bucket))

    return sorted_arr