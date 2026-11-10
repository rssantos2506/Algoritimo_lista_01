import random
import sys
import time

# Importando os 9 algoritmos de ordenação de seus respectivos módulos
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from bucket_sort import bucket_sort

# Aumenta o limite de recursão para suportar listas grandes em algoritmos recursivos
sys.setrecursionlimit(200000)

def formatar_tempo(tempo_segundos):
    """
    Formata o tempo de execução convertendo para a unidade ideal 
    (segundos, milissegundos, microssegundos ou nanossegundos).
    """
    if tempo_segundos >= 1.0:
        return f"{tempo_segundos:.4f} segundos (s)"
    elif tempo_segundos >= 1e-3:
        return f"{tempo_segundos * 1e3:.4f} milissegundos (ms)"
    elif tempo_segundos >= 1e-6:
        return f"{tempo_segundos * 1e6:.4f} microssegundos (µs)"
    else:
        return f"{tempo_segundos * 1e9:.4f} nanossegundos (ns)"

def executar_e_medir(nome_algoritmo, funcao_ordenacao, dados):
    """
    Função auxiliar para medir o tempo de execução de alta precisão 
    de um algoritmo de ordenação.
    """
    # Cria uma cópia da lista para que cada algoritmo ordene do zero de forma justa
    dados_copia = list(dados)
    
    # perf_counter fornece a maior precisão de relógio disponível no sistema
    inicio = time.perf_counter()
    resultado = funcao_ordenacao(dados_copia)
    fim = time.perf_counter()
    
    tempo_gasto = fim - inicio
    tempo_formatado = formatar_tempo(tempo_gasto)
    
    print(f"[{nome_algoritmo:<15}] -> Tempo: {tempo_formatado}")
    return tempo_gasto

def main():
    # Usaremos 10.000 elementos para conseguir testar os 9 algoritmos (incluindo os O(N²)) em tempo hábil
    TAMANHO_AMOSTRA = 10_000
    
    print(f"Gerando lista aleatória de {TAMANHO_AMOSTRA:,} elementos...")
    dados_originais = [random.randint(0, 100_000) for _ in range(TAMANHO_AMOSTRA)]
    print("Lista gerada com sucesso!\n")
    
    print("=" * 60)
    print(f"INICIANDO BENCHMARK DE ORDENAÇÃO ({TAMANHO_AMOSTRA:,} ELEMENTOS)")
    print("=" * 60)
    
    # Dicionário contendo o nome descritivo e a respectiva função importada
    algoritmos = [
        ("Selection Sort", selection_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort),
        ("Radix Sort", radix_sort),
        ("Bucket Sort", bucket_sort)
    ]
    
    tempos_resultados = []
    
    for nome, funcao in algoritmos:
        try:
            tempo_bruto = executar_e_medir(nome, funcao, dados_originais)
            tempos_resultados.append((nome, tempo_bruto))
        except Exception as e:
            print(f"[{nome:<15}] -> Erro na execução: {e}")

    print("=" * 60)
    
    # Ordena os resultados do mais rápido para o mais lento (menor tempo bruto primeiro)
    tempos_resultados.sort(key=lambda x: x[1])
    
    print("\n🏆 RANKING DE DESEMPENHO (Do mais rápido para o mais lento):")
    for posicao, (nome, tempo_bruto) in enumerate(tempos_resultados, 1):
        print(f"{posicao}º lugar: {nome:<15} -> {formatar_tempo(tempo_bruto)}")

    print("\n[Nota]: Algoritmos lineares em tempo de execução como Counting Sort e Radix Sort")
    print("frequentemente se destacam na casa dos milissegundos ou microssegundos com inteiros.")

if __name__ == "__main__":
    main()