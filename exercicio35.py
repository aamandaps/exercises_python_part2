#Declarando as variáveis
n1:int=0
n2:int=0
soma:int=0
cont:int=0
maior:int=0
menor:int=0
#Inicio
n1 = int(input('Inisira um valor: '))
n2 = int(input('Insira um segundo valor: '))

#Condição para verificar qual é o maior
if n1>n2:
    maior=n1
    menor=n2
else:
    maior=n2
    menor=n1
#Fim da primeira condição

cont = menor+1

#Laço para repetir somente os número ímpares
while cont<maior:
    #Condição para verificar é o número é ímpar
    if cont%2!=0:
        soma += cont
    #Fim da segunda condição
    cont += 1
#Fim laço
print(f'A soma dos número ímpares entre esses dois valores é:{soma}')

#Fim
