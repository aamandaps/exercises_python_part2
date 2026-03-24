#Declarando as variáveis
num:float
cont:int=1
maior:float=0.0
menor:float=0.0

#Inicio

num = float(input('Digite um número real: ')) #Entrada essencial

menor = num
maior = num

while cont<100:
    num = float(input('Digite um número real: '))
    if num>=0 and num>maior:
        maior = num
    #Fim-condicional que determina o maior
    if num>=0 and num<menor:
        menor = num
    #Fim-condicional que determina o menor

    cont += 1
#Fim-laço
print(f'O maior número é {maior} e o menor número é {menor}')

#Fim
