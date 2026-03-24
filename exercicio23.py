#Declaração de variáreis
v1:int=0
v2:int=0
v3:int=0
v4:int=0

#Inicio
v1 = int(input('Insira um valor: '))
v2 = int(input('Insira um valor maior do que o anterior: '))
v3 = int(input('Insira um valor maior do que o anterior: '))
v4 = int(input('Insira um valor aleatório: '))

#Verificando a ordem do quarto valor
if v4<=v1:
    print('A ordem correta é: ',v4,v1,v2,v3)
elif v4>v1 and v4<=v2:
    print('A ordem correta é: ',v1,v4,v2,v3)
elif v4>v2 and v4<=v3:
    print('A ordem correta é: ',v1,v2,v4,v3)
elif v4>v3:
    print('A ordem correta é: ',v1,v2,v3,v4)
#fim da condição

#fim