# 2. Faça um programa que leia 4 valores,
#  calcule a média e imprima positivo ou negativo (para ser positivo a média deve ser acima de 1).



a = float(input('digite um número: '))
b = float(input('digite um número: '))
c = float(input('digite um número: '))
d = float(input('digite um número: '))

media = (a + b + c + d) / 4

print('A média é: ',media)

if media < 0: 
    print('negativo: ', media)
elif media > 0: 
    print('positivo: ', media)    
