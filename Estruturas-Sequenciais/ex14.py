print(100*'=')
print('Calcula Excesso'.center(20))
PesoDePeixe = float(input('Entre com o peso: '))
excesso = PesoDePeixe-50
multa = excesso*4.00
print(f'Você possui {excesso} Kg em excesso!')
print(f'Você deve pagar R$ {multa:.2f} de multa!')
print(100*'=')
