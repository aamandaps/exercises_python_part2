#Declaração de variáveis
v1:int=0
v2:int=0

#Inicio
v1 = int(input('Digite um valor inteiro: '))
v2 = int(input('Digite outro valor inteiro: '))

#Verificando qual é o maior
if v1>v2 and v1!=v2:
    print('A ordem deles é ',v1,'e',v2)
elif v2>v1 and v2!=v1:
    print('A ordem é ',v2 ,'e',v1)
#fim da condição

#fim