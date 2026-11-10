def radix_sort(element_list):
    """
    Algoritmo: Radix Sort
    
    Como funciona:
    Ordena números inteiros processando-os dígito por dígito, começando pelo 
    dígito menos significativo (unidades) até o mais significativo (centenas, 
    milhares, etc.). Utiliza um algoritmo estável de suporte (como Counting Sort) 
    para ordenar cada coluna de dígitos.
    
    Complexidade:
    - Pior, Médio e Melhor Caso: O(d * (N + b)), onde d é o número de dígitos e b a base
    - Espaço Auxiliar: O(N + b)
    
    Vantagens: Tempo quase linear para chaves de tamanho fixo; altamente eficiente.
    Desvantagens: Restrito a dados que podem ser representados por dígitos/caracteres.
    """
    if not element_list:
        return element_list

    def counting_sort_by_digit(arr, exponent):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            digit_index = (arr[i] // exponent) % 10
            count[digit_index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            digit_index = (arr[i] // exponent) % 10
            output[count[digit_index] - 1] = arr[i]
            count[digit_index] -= 1

        return output

    max_val = max(element_list)
    exp = 1
    sorted_arr = list(element_list)

    while max_val // exp > 0:
        sorted_arr = counting_sort_by_digit(sorted_arr, exp)
        exp *= 10

    return sorted_arr