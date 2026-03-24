#Declarando as variáveis
num:int=0
fatorial:int=1
cont:int=0

#Inicio
num =  int(input('Digite um número: '))

#Laço que vai calcular o fatorial
while num>1:
    fatorial = fatorial*num
    num -= 1
#Fim laço
print(f'O fatorial desse número é {fatorial}')

#Fim
