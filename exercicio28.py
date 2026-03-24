#Declaração das variáveis
m_mensal:float=0
preco_a:float=0
preco_n:float=0

#Inicio
preco_a = float(input('Insira o preço atual do produto: '))
m_mensal = float(input('Insira a média mensal das vendas desse produto: '))

#Verificando se o preço recebe +10%
if m_mensal<500 and preco_a<30.00:
    preco_n = preco_a*1.10
    print(f'O novo preço do produto com 10% de aumento é: {preco_n:.2f}')
#Verificando se preço recebe +15%
elif m_mensal>=500 and m_mensal<1000 and preco_a>=30.00 and preco_a<80.00:
    preco_n = preco_a*1.15
    print(f'O novo preço do produto com 15% de aumento é: {preco_n:.2f}')
elif m_mensal >=1000 and preco_a>=80.00:
    preco_n = preco_a*(1-0.5)
    print(f'O novo preço do produto com desconto de 5% é: {preco_n:.2f}')
else:
    print('O preço permanece o mesmo') 
#Fim condição

#Fim
