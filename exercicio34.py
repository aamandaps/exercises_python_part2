#Declarando as variáveis
num:int=0
tabuada:int=0
cont:int=0

#Inicio

num = int(input('Insira um número pra calcular sua tabuada de 0 a 10: '))

#Laço para calcular a tabuada
while cont<=10:
    tabuada = num*cont
    cont+=1
    print(tabuada)
#Fim laço

#Fim