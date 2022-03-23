#Faça um Programa que pergunte quanto você ganha por hora e o número 
#de horas trabalhadas no mês. Calcule e mostre o total do seu salário no 
#referido mês.
slro_hora = float(input('Quanto você recebe por hora: '))
hr_trab = int(input('Quantas horas foram trabalhadas [Valores inteiros apenas]: '))
print(f'Seu salário será de R$ {slro_hora*hr_trab:.2f}.')
