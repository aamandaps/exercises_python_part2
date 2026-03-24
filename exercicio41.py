#Declarando as variáveis
d1:int=1
d2:int=1
soma:int=0

#Inicio

#Laço que vai percorrer o primeiro dado
for d1 in range (1,7):

    #Laço que vai percorrer o segundo dado
    for d2 in range (1,7):
        soma = d1+d2

        #Verificando até a soma resultar em 7
        if soma == 7:
            print(f'Combinação que resulta em 7: {d1} + {d2}')
        #Fim-condicional

    #Fim-laço 2

#Fim-laço 1

#Fim