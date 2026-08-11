soma = 0

while True:
    num = float(input("Digite um número (ou 0 para sair): "))
    if num == 0:
        break
    soma += num

print(f"A soma de todos os valores digitados é: {soma}")