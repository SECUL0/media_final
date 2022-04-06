nome = input('Escreva o nome: ')
nota1 = float(input('Digite a nota da AV1: '))
nota2 = float(input('Digite a nota da AVD: '))
nota3 = float(input('Digite a nota da AV2: '))

mf = round( ((nota1 + nota2 + nota3) / 3), 2)

if mf >= 6:
	print(nome,'conseguiu média',mf,'está aprovado(a)')
	print('Parabéns!')
	if mf==10:
		print('Nota MAXIMA!!!')
else:
	print(nome,'conseguiu média',mf,'está reprovado(a)')
	print('Estude mais...')
print('Fim do programa')