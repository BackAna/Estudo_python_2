#print('1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:'('\n'))


# tamanho do vetor 

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- a)')
print("Tamanho do vetor: " + str(len(L))) 
print('\n')

# maior valor da lista

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- b)')
max_value = max(L)
print('maior valor: ', max_value)
print('\n')

# menor valor da lista 

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- c)')
min_value = min(L)
print('Menor valor: ', min_value)
print('\n')

# soma de todos os elementos

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- d)')
soma_dos_elementos = sum(L)
print('A soma é: ', soma_dos_elementos)
print('\n')

# lista em ordem crescente

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- e)')
ordem_crescente = sorted(L)
print (ordem_crescente)
print('\n')

# lista em ordem decrecente

L = [5, 7, 2, 9, 4, 1, 3]

print('Questão 1- f)')
ordem_decrescente = sorted(L, reverse=True) 
print (ordem_decrescente)
print('\n')
