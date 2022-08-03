from time import sleep
compras = []
valor = []
cont= total = 0
print('Bem-vindo ao mercado Casagrande')
sleep(.5)
while True:
    pro=str(input('Digite o produto ou fim para encerrar: '))
    if 'fim' in pro:
        break
    compras.append(pro)
    sleep(.2)
    val=float(input('Digite o valor do produto: '))
    total +=val
    valor.append(val)
    sleep(.2)
print('Lista da compra:')
for c in compras:
    print(f'item {c} valor R${valor[cont]:.2f}')
    cont+=1
    sleep(0.5)
print(f'Valor total de R${total:.2f}.')
