#Declarando variáveis
v1:int = 0
v2:int = 0
d:int = 0

#Inicio
v1 = int(input('Digite um valor inteiro: '))
v2 = int(input('Digite outro valor inteiro: '))

#condição para verificar a diferença
if v1>v2:
    d = v1-v2
    print('A diferença entre os valores é: ',d)
else:
    d = v2-v1
    print('A diferença entre os valores é: ',d)
#fim if

#fim
