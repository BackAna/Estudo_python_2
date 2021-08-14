print("Você vai digitar 20 valores")
lista = []
maior = 0
menor = 0
media = 0
for cont in range(0, 21):
    lista.append(int(input(f'digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
sum(lista) / 20
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')


