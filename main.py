card = input('Digita cartão: ')
card = card.replace(" ", "") # retira espaços em branco

# card = '4003600000000014'
# print (card + '\n')

tam_card = len(card)


def alg_Luhn() :

	soma = int()
	for i in range(tam_card -2, -1, -2):
		n = int(card[i])
		# print('n : %i' %n)
		n2 = n * 2
		# print('n2: %i' %n2)
	
		if n2 < 10:
			soma += n2
		else:
			nd1 = n2 % 10
			# print('nd1: %i' %nd1)
			nd2 = ((n2 % 100) - nd1) / 10
			# print('nd2: %i' %nd2)
			soma += (nd1 + nd2)
	
	# print('Soma: %i' %soma)
	# print('\n\n\n')
	
	
	for i in range(tam_card -1, -1, -2):
		n = int(card[i])
		# print('n : %i' %n)
		soma += n
	
	# print('Soma total: %i' %soma)
	
	if soma % 10 == 0:
		# print('Cartão valido')
		return True
	else:
		# print('Cartão invalido')
		return False


def check_card(digito):
	return int(card[0:digito])
	
# print(check_card(2))
	

if tam_card >= 13 and tam_card <= 16 and alg_Luhn() == True:
	if tam_card == 16 and (check_card(2) >= 51 and check_card(2) <= 55) :
		print('MASTERCARD')
	elif tam_card == 15 and (check_card(2) == 34 or check_card(2) == 37):
		print('AMEX')
	elif check_card(1) == 4:
		print('VISA')
	else:
		print('INVALIDO')
else:
	print('INVALIDO')