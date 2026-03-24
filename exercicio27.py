#Declaração das variáveis
num_v:int=0
metros:float=0
tempo:float=0
vel_m:float=0

#Inicio
num_v = int(input('Insira o número de voltas: '))
metros = float(input('Insira quantos metros foram percorridos: '))
tempo = float(input('Insira o tempo do percurso: '))

#Verificando o número de voltas para calcular a velocidade média
if num_v>1:
    metros = num_v*metros
    metros = metros/1000
    tempo = tempo/60
    vel_m = metros/tempo
    print(f'A velocidade média desse percurso foi: {vel_m:.2f}km/h')
elif num_v == 1:
    metros = metros/1000
    tempo/60
    vel_m = metros/tempo
    print(f'A velocidade média desse percurso foi: {vel_m:.2f}km/h')
else:
    print('Insira um número de voltar igual ou maior que 1')
#Fim condição

#Fim