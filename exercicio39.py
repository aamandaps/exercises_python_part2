#Declarando as variáveis
casa:int=1
grao:int=1
soma:int=0

#Inico
while casa<=64:
    soma = soma+grao
    grao = grao*2
    casa += 1
#Fim-laço que dobra os grãos nas casas a cada volta

print(f'A soma de todos os grãos é {soma}')

#Fim