#Revisão do aprendendopython2.py

# numero = int(input('Digite sua idade: '))

# if numero < 16:
#     print('')
#     print('Você não pode votar!')
# elif numero < 18:
#     print('')
#     print('Você pode escolher se vai votar ou não!')
# elif numero > 65:
#     print('')
#     print('Seu voto retorna a ser opcional!')
# else:
#     print('')
#     print('Você deve votar!')

# ===========================================================================================================================

# Aula 3:

# Parte 1:
# numero = int(input('Digite um número: '))
# while numero != 0:
#     print('Valor digitado é', numero)
#     numero1 = int(input('Digite um número: '))

# Parte 2:
# contador = 0
# for contador in range(5):
#     print('Contador é: ', contador)

# while contador < 5:
#     print(contador)
#     contador = contador + 1

# Parte 3:
# numero = int(input('Digite um número: '))
# for contador in range(1,11):
#     resultado = numero * contador
#     print(f"{numero} * {contador} = ", resultado)
#     contador += 1

# ===========================================================================================================================

# Tentativa de Tabuada Pausada (falha)
# contador = 0
# numero = int(input('Digite um número: '))
# resultado = numero * contador

# while contador != 0:
#     for contador in range(11):
#         print(f"{numero} * {contador} = ", resultado)
#         numero = int(input('Digite um número: '))
#         contador += 1

# ===========================================================================================================================

# Anotações:
# range: quantidade de vezes que ele irá executar