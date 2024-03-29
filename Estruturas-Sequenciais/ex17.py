"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações: comprar
    apenas latas de 18 litros; comprar apenas galões de 3,6 litros; sempre arredonde os valores para cima, isto é,
    considere latas cheias. """
from math import ceil

comprador_area = float(input("Quantos metros quadrados serão pintados? "))

galoes18 = comprador_area/(6*18)
valor18 = ceil(galoes18)*80

galoes36 = comprador_area/(6*3.2)
valor36 = ceil(galoes36)*25

print(f"Comprar apenas latas de 18 litros. Serão necessárias {ceil(galoes18)} latas pelo valor de R$ {valor18:.2f}.")

print(f"Comprar apenas latas de 3,6 litros. Serão necessárias {ceil(galoes36)} latas pelo valor de R$ {valor36:.2f}.")
