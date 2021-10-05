"""
Iniciar com letra, pode conter numeros, sparador _, letras minúsculas
"""

nome = 'William Koller'
idade = 32
altura = 1.85
e_maior = idade > 18
peso = 94
print('Nome:', nome)
print('Idade', idade)
print('Altura', altura)
print('É maior', e_maior)
imc = peso / altura ** 2

print(nome, 'tem,', idade, 'de idade e seu imc é', imc)