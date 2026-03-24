#Declaração de variáveis
n1:float=0
n2:float=0
n3:float=0
n4:float=0
media:float=0

#Inicio
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
n4 = float(input('Insira a quarta nota: '))

#Cálculo da média
media = (n1+n2+n3+n4)/4

#Verificando a média final
if media>=6:
    print('Aluno aprovado')
elif media>=3 and media<6:
    print('Realizar exame')
else:
    print('Aluno retido')
#Fim da condição

#Fim