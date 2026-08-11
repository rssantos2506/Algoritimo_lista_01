numeros = []

for i in range(1, 6):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)

print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")