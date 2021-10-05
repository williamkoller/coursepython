nome = 'William'
idade = 32
altura = 1.85
e_maior = idade > 18
peso = 94
imc = peso / altura ** 2

print(nome, 'tem,', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

# parametors por posição
print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
# Parametros nomeados
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
