#Declarando as variáveis
num:int=0
cont:int=0
prim:int=0
seg:int=1
prox:int=0

#Inicio
num= int(input('Insira um número: '))

#Calculando a sequência
for cont in range(cont,num,1):
    prox = prim + seg
    #Atualizando a sequência
    prim = seg
    seg = prox
    print(f'A sequência é {prim}')
#Fim-for

#Fim