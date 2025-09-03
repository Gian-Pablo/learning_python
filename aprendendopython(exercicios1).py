# exemplo de saida: Olá Jose, seja bem-vinda!
# 2. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

# 3. Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

# 4. Faça um programa em Python que:
# Leia a largura e a altura de uma parede em metros.
# Calcule a área da parede.
# Calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m².

# 5. Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

# 6. Sistema de Votação (if/elif/else)
# Crie um programa que leia a idade de uma pessoa e informe se ela:
# não vota (menor que 16 anos)
# voto opcional (16 ou 17 anos, ou acima de 65 anos)
# voto obrigatório (de 18 a 65 anos)

# 7. Aprovação do Aluno (if/else)
# Faça um programa que leia a média final de um aluno e informe se ele está:
# Aprovado (média maior ou igual a 6)
# Reprovado (média menor que 6)

#Exercício 1:
# 1. Fazer um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = "Gian Pablo Benvive Torres"

print('Exercicio 1:')
print('')
print(f' Bem-vindo {nome} ao Visual Studio Code!')
print('')

#Exercício 2:

numero01 = int(input('Digite um número: '))
duplicacao = numero01 * 2
triplicacao = numero01 * 3
raiz = pow(numero01, 0.5)

print('Exercicio 2:')
print('')
print(f'O dobro é: ', duplicacao)
print(f'O triplo é: ', triplicacao)
print(f'A raiz é: ', raiz)
print('')

#Exercício 3:

vlmetro = int(input('Digite um valor em metros: '))
vlcentimetros = vlmetro * 100
vlmilimetros = vlmetro * 1000

print('Exercício 3:')
print('')
print(f'O valor é de {vlcentimetros} centímetros.')
print(f'O valor é de {vlmilimetros} milímetros.')
print('')

#Exercício 4:

largura = int(input('Digite o valor da largura: '))
altura = int(input('Digite o valor da altura: '))

print('Exercício 4:')
print('')
print(f'')