from time import sleep
compras = []
valor = []
quantidade = []
cont= total = val = quant = itotal = 0
print('Bem-vindo ao mercado Casagrande')
sleep(.5)
while True:
    pro=str(input('Digite o produto ou fim para encerrar: '))
    if 'fim' in pro:
        break
    compras.append(pro)
    sleep(.2)
    quant=int(input('Quantos itens?'))
    itotal += quant
    quantidade.append((quant))
    pre=float(input('Digite o valor do produto: '))
    total +=(quant*pre)
    valor.append(pre)
    sleep(.2)
print('Lista da compra:')
for c in compras:
    print(f'{c} {quantidade[cont]} R${valor[cont]:.2f}  ')
    cont+=1
    sleep(0.5)
print(f'Itens totais {itotal}.')
print(f'Valor total de R${total:.2f}.')
pg=str(input('Qual a forma de pagamento:'
             'Dinheiro ou Pix:'
             'Cartão 1x:'
             'Cartão Parcelado:'))
