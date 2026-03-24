#Declarando as variáveis
tipo:str
poup:str = "poupança"
rend_fixa:str = "renda fixa"
rend:float=0.0
v:float=0.0

#Inicio
v = float(input('Digite o valor investido: '))
tipo = (input('Digite o tipo de investimento: '))

#Verificando o investimento e calculando o rendimento
if tipo == "poupança":
    rend = v*1.03
    print(f'O rendimento foi {rend:.2f}') 
elif tipo == "renda fixa":
    rend = v*1.05
    print(f'O rendimento foi: {rend:.2f}')
#Fim de condição

#Fim