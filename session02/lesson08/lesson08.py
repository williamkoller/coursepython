"""
  * 1 - Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
  * 2 - Criar variável com o ano atual (int).
  * 3 - Obter o ano de nascimento da pessoa (baseado na idade e no ano atual).
  * 4 - Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa).
  * 5 - Exibir um texto com todos os valores na tela usando F-Strings (com chaves).
"""
# 1
nome = 'William'
idade = 32
altura = 1.85
peso = 94.34
quadrado = 2

# 2
ano_atual = 2021

# 3
ano_nasci = ano_atual - idade

# 4
imc = peso / altura ** quadrado

# 5
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}')
print(f'{nome} nasceu em {ano_nasci}')
