#Declaração de variáveis
a:int=0
b:int=0

#Inicio
a = int(input('Digite um valor: '))
b = int(input('Digite um segundo valor: '))

#Verificando o maior e menor, e se eles são múltiplos um do outro
if a>b and a%b==0:
    print('O primeiro(maior) valor é múltiplo do segundo(menor)')
elif b>a and b%a==0:
    print('O segundo(maior) valor é múltiplo do primeiro(menor)')
else:
    print('Não são múltiplos um do outro')
#Fim da condição

#Fim