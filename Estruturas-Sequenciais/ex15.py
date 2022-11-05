print(100*'=')
print('Salário'.center(20))
SaldoHora = float(input('Ganho por hora: '))
HorasTrabalhadas = float(input('Horas trabalhadas: '))
Salario = SaldoHora*HorasTrabalhadas
print(
f'''    + Salário Bruto : R$ {Salario:.2f}
    - IR (11%) : R$ {Salario*0.11:.2f}
    - INSS (8%) : R$ {Salario*0.08:.2f}
    - Sindicato (5%) R$ {Salario*0.05}
    = Salário Liquido : R$ {Salario-(Salario*0.24):.2f}'''
)
print(100*'=')
