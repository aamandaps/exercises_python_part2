#Declarando as variáveis
n1:int=0
n2:int=0
num:int=0
divisor:int=0
qnt_div:int=0

#Inicio

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

num = n1

#Laço que vai percorrer os números
while num<=n2:
    qnt_div = 0
    divisor = 1

    #Laço que vai percorrer os divisores
    while divisor<=num:

        #Verificando se é primo ou não
        if num % divisor == 0:
            qnt_div = qnt_div + 1
        #Fim-condicional 1
        divisor += 1
    #Fim-laço 2

    #Verificando as quantidades de números primos
    if qnt_div == 2:
        print (f'Os números primos entre esses dois valores são {num}')
    #Fim- condicional 2
    
    num += 1

#Fim-laço 1

#Fim