#Declarando variáveis
hora_i:int=0
minuto_i:int=0
hora_f:int=0
minuto_f:int=0
quant_h:int=0
quant_m:int=0

#Inicio
hora_i = int(input('Insira a hora que você começou a jogar: '))
minuto_i = int(input('Insira o(s) minuto(s) que você começou a jogar: '))
hora_f = int(input('Insira a hora que você parou de jogar: '))
minuto_f = int(input('Insira o(s) minuto(s) que você parou de jogar: '))

#Verificando quantas horas de jogo
if hora_f<hora_i:
    hora_f = hora_f+24
#Verificando minutos 
elif minuto_f<minuto_i:
    minuto_f = minuto_f+60
    hora_f = hora_f-1
#fim condição

#Calculando o horário exato
quant_h = hora_f - hora_i
quant_m = minuto_f - minuto_i
print('Você jogou por', quant_h,'hr e' ,quant_m,'m')