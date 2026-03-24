#Declaração de variáveis
a:int = 0
b:int = 0
c:int = 0
delta:float = 0
x1:float = 0
x2:float = 0

#Inicio
a = int(input('Escreva o valor de A: '))
b = int(input('Escreva o valor de B: '))
c = int(input('Escreva o valor de C: '))

#Calculando delta
delta = (b**2)-4*a*c

#Verificando se há raízes
if delta<0:
    print('Não há raízes')
elif delta>=0:
    x1 = (-b + (delta**0.5))/ (2*a)
    x2 = (-b - (delta**0.5))/ (2*a) 
    print('As raízes são: ', x1 ,'e',x2)
#fim condição

#fim