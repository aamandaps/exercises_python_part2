#Declarando as variáveis
den:int=0
num:int=1
soma:int=0
fracao:float=0.0

#Inicio

#Laço que vai percorrer o termo
while num<=15: 

    #Calculando a série
    den = num*num 
    fracao = num/den

    #Verificando se a próxima operação vai ser subtração ou adição
    if num % 2 ==0:
        soma -= fracao
    else: 
        soma += fracao
    #Fim-condicional

    num += 1

#Fim-laço

print(f'A série é igual a: {soma}')

#Fim 

