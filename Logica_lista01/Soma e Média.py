soma = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    soma += num

media = soma / 10

print(f"Soma total: {soma}")
print(f"Média: {media}")