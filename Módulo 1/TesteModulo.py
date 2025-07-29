nomes = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio']
# # estrutura que irá armazenar o número de letras de cada nome
# qtd_letras = {}
# # calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
# for nome in nomes:
#  qtd_letras[nome] = len(nome)
# print(type(qtd_letras))
# print(type(nomes))
# print(type({1, 3, 1, 4, 3, 2, 2, 0, 4}))
# n = input()
# beijo = [n/2 for n in range(0, 10) if n > 3]
# print(beijo)
nome = input()
beijo = [nome[len(nome)] for nome in nomes]
print(beijo)