"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""
import datetime
import os
from time import sleep


def tempo():
    return datetime.datetime.now()


log_ex02 = open('log.txt', 'a')
tipo_certo = ''
while tipo_certo != 'yes':
    os.system('clear')
    print(50*'=')
    try:
        numero = float(input('Informe um número:\n'))
        if numero >= 0:
            print(f'{numero} é um número Positivo')
        else:
            print(f'{numero} é um número Negativo')
    except ValueError as TipoErrado:
        data = str(tempo())
        print('Um valor númerico deve ser informado!')
        log_ex02.write(data+' - '+str(TipoErrado)+'\n')
        sleep(2)
    except KeyboardInterrupt:
        data = str(tempo())
        print('Programa finalizado pelo usuário!')
        log_ex02.write(data+' - '+'Programa encerrado abruptadamente pelo usuário'+'\n')
        sleep(2)
        break
    else:
        tipo_certo = 'yes'
    finally:
        print(50*'=')
