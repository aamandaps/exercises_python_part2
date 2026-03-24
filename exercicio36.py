#Declarando as variáveis
num:int=0
fatorial:int=1
cont1:int=0
soma:int=1
cont2:int=1

#Inicio
num = int(input('Digite um número: '))

#Primeiro laço para o denominador ir até num
for cont1 in range (1,num + 1):
    fatorial = 1
    #Segundo laço para calcular o fatorial de num
    for cont2 in range (1,cont1 + 1):
        fatorial = fatorial*cont2
    #Fim segundo laço
    soma = soma + (1/fatorial)
#Fim primeiro laço
print(f'{soma:.2f}')

#Fim