def maior_numero(a, b):
    return a if a > b else b

# Exemplo de uso:
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"O maior número é: {maior_numero(n1, n2)}")