def counting_sort(element_list):
    """
    Algoritmo: Counting Sort
    
    Como funciona:
    Não baseado em comparações. Conta a frequência de ocorrência de cada valor 
    distinto na lista de entrada, armazena em um vetor de contagem auxiliar e 
    utiliza esses valores somados para posicionar cada elemento diretamente 
    em seu lugar definitivo na lista de saída.
    
    Complexidade:
    - Pior, Médio e Melhor Caso: O(N + K), onde K é o intervalo dos dados (max - min)
    - Espaço Auxiliar: O(K)
    
    Vantagens: Extremamente rápido (linear) quando o intervalo de valores K é pequeno.
    Desvantagens: Ineficiente e consome muita memória se o valor máximo for muito grande.
    """
    if not element_list:
        return element_list

    min_val = min(element_list)
    max_val = max(element_list)
    range_val = max_val - min_val + 1
    
    count_array = [0] * range_val
    output_array = [0] * len(element_list)

    for num in element_list:
        count_array[num - min_val] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for num in reversed(element_list):
        output_array[count_array[num - min_val] - 1] = num
        count_array[num - min_val] -= 1

    return output_array