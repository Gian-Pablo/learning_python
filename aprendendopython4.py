# Aula 4

# Exemplo uso do Array
# nomes = ['Gian Pablo', 'Luciane Aparecida', 'Joaquim Abel']
# print(nomes)
# print(nomes[2])


# Quantos clientes você quer cadastrar? (Exemplo 1)
# qt_clientes = int(input('Quantos clientes você quer cadastrar?'))
# vetor = [0 for i in range(qt_clientes)] # Quantidade de posições a depender da quantidade de clientes cadastrados.
# print(vetor)


# Quantos clientes você quer cadastrar? (Exemplo 2)
# qt_clientes = int(input('Digite a quantidade de clientes que você quer cadastrar: '))
# clientes = []
# vetor = [0 for i in range(qt_clientes)]

# for i in range(qt_clientes):
#     clientes.insert(i, input('Digite o nome do cliente: '))
#     clientes.pop(0)
#     print(clientes)


# Array Tipo: ???
# clientes = [['Jose Carlos', 'Vanessa', 'Camila'], [35, 40, 10], ['Amarelo', 'Verde', 'Vermelho']]
# print(clientes[0][1])
# print(clientes[1][1])
# print(clientes[2][1])


# Array usando Lista Bi-Multi Dimensional
# qt_clientes = int(input('Digite quantos clientes você quer cadastrar: '))
# vetor = [0 for i in range(qt_clientes)]

# for i in range(qt_clientes):
#     print('')
#     print(f'Digite os dados do cliente {i}')
#     nome = input('Nome: ')
#     idade = input('Idade: ')
#     sexo = input('Sexo: ')

#     vetor[i] = {
#         'Nome': nome,
#         'Idade': idade,
#         'Sexo': sexo
#     }

#     print('')
#     print('Lista de Pessoas Cadastradas: ')
#     for pessoas in vetor:
#         print(pessoas)

# Decisão Aleatória de Número
# from random import randint
# computador = randint(0, 10)
# print(computador)