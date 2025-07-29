
# lista = [7, 3.14, 42, -8, 0, 19, 2.71, -3, 100, 5]#
# soma = 0
# for numero in lista:
#     print(numero)
#     soma += numero
# print(soma)


### Código soma itens pares funcionando###

# lista = [12, 7, 5, 8, 3, 10, 6, 1, 4, 9, 8, 9,7,5,9,8,10]
# pares = []
# for numero in lista:
#     if numero % 2 == 0:
#         pares.append(numero)
#     soma = len(pares)
# print(soma )

### Maior e menor###

# lista = [23, 5, 89, 12, 77, 34, 2, 90, 11, 50]
# maior_numero = lista[0]
# menor_numero = lista[0]
# for numero in lista:
#     if numero > maior_numero:
#         maior_numero = numero
#     elif numero < menor_numero:
#         menor_numero = numero
# print(maior_numero)
# print(menor_numero)


### inversor de lista ###

# lista = [23, 5, 89, 12, 77, 34, 2, 90, 11, 50]
# lista_inversa = []
# while lista:
#
#     lista_inversa.append(lista.pop())
# print(lista_inversa)
### remova da lista se impar###

# lista = [23, 5, 89, 12, 77, 34, 2, 90, 11, 50]
# #criar uma nova lista para iterar pois mexer na mesma lista vai causar problemas
# for numero in lista[:]:
#     if numero % 2 != 0:
#         lista.remove(numero)
# print(lista)

### remoção de duplicatas

# lista = [4, 7, 2, 7, 3, 4, 2, 8, 9, 3, 1, 8, 5]
#
# for numeros in lista[:]:
#     if lista.count(numeros) > 1:
#         lista.remove(numeros)
# print(lista[:])

### produto dos elementos

# lista = [4, 7, 2, 7, 3, 4, 2, 8, 9, 3, 1, 8, 5]
# produto = 1
# for elemento in lista[:]:
#     produto *= elemento
# print(produto)

### separar pares e impares###
# lista = [4, 7, 2, 7, 3, 4, 2, 8, 9, 3, 1, 8, 5]
# lista_pares = []
# lista_impares = []
# for elemento in lista[:]:
#     if elemento % 2 == 0:
#         lista_pares.append(elemento)
#         lista.remove(elemento)
#     elif elemento % 2 != 0:
#         lista_impares.append(elemento)
#         lista.remove(elemento)
# print(lista_pares)
# print(lista_impares)

### Concatenar listas ##

# lista1 = [1, 3, 5, 7, 9]
# lista2 = [2, 4, 6, 8, 10]
#
# lista3 = []
#
# for i in range(len(lista1)):
#     lista3.append(lista1[i])
#     lista3.append(lista2[i])
#
# print(i)
# print(lista3)