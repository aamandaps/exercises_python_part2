#Declarando variáveis
valor:int=0

#Inicio
valor = int(input('Digite um valor: '))

#Verificando se é divisível por 3 e 2
if valor%2==0 and valor%3==0:
   print('Esse número é divisível por 2 e 3')
else:
   print('Esse número não é divisível por 2 e nem por 3')
#Fim condição

#Fim  