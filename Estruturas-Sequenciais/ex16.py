from math import ceil
print(100*'=')
print('Cálculo'.center(15))
area = float(input('Entre com a ârea a ser pintada: '))
latas = ceil(area/54)
PrecoTotal = latas*80.00
print(f'Serão necessárias {latas} latas de tinta.')
print(f'Isso custará R$ {PrecoTotal:.2f}')
print(100*'=')
