#Declarando as variáveis
base:int=0
exp:int=0
pot:int=1
cont:int=1

#Inicio

base = int(input('Insira o valor da base: '))
exp = int(input('Insira o valor do expoente: '))

#Laço que calcula a potência
while cont<=exp:
    pot *= base
    cont += 1
#Fim-laço

print(f'O resultado da potência: {pot}')

#Fim