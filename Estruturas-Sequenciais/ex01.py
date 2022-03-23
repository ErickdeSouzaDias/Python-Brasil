# Faça um programa que mostre a mensagem "Alô mundo" na tela.

#1º maneira
print('Alô mundo!')
#2º maneira
msg = 'Alô mundo!'
print(msg)
#3º maneira
print('Alô'+' mundo!')
#4º maneira
print('A'+'l'+'ô', 'm'+'u'+'n'+'d'+'o'+'!')
#5º maneira
letter = ('####A#####', '####l#####', '####ô#####', '#### #####', '####m#####', '####u#####', '####n#####', '####d#####', '####o#####', '####!#####')
for ltr in range(0, 10):
	print(letter[ltr].upper())
