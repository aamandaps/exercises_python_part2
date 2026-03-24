#Declaração de variáveis
num:int=0
soma:int=1
cont:int=0

#Inicio
num = int(input('Insira um número: '))

#Laço de repetição
for cont in range(1, num+1): #O n+1 é para considerar o último número 
    soma += (1/cont)
    cont += 1
#Fim for
print(f'A soma é: {soma:.2f}')

#Fim