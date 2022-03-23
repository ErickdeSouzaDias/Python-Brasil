#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme 
#e mostre a temperatura em graus Celsius.
faren = float(input('Informe a temperatura em ºF: '))
cels = 5*((faren - 32)/9)
print(f'A temperatura é {cels:.2f}ºC.')
