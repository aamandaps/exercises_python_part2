#Declarando as variáveis
num:int=1
den:int=1
soma:int=0

#Inicio

#Laço que vai percorrer o termo
while num<=50:
    soma += (num/den) #Calculando o termo
    num += 1
    den += 2
#Fim-laço

print(f'A série é igual a:{soma:.2f}')

#Fim