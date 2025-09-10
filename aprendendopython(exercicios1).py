#Exercício 1:
# 1. Fazer um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
# exemplo de saida: Olá Jose, seja bem-vinda!

print('Exercicio 1:')
print('')

nome = (input('Digite um nome: '))

print('')
print(f' Bem-vindo {nome} ao Visual Studio Code!')
print('')

#Exercício 2:
# 2. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('Exercicio 2:')
print('')

numero01 = int(input('Digite um número: '))
duplicacao = numero01 * 2
triplicacao = numero01 * 3
raiz = pow(numero01, 0.5)

print('')
print(f'O dobro é: ', duplicacao)
print(f'O triplo é: ', triplicacao)
print(f'A raiz é: ', raiz)
print('')

#Exercício 3:
# 3. Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

print('Exercício 3:')
print('')

vlmetro = int(input('Digite um valor em metros: '))
vlcentimetros = vlmetro * 100
vlmilimetros = vlmetro * 1000


print('')
print(f'O valor é de {vlcentimetros} centímetros.')
print(f'O valor é de {vlmilimetros} milímetros.')
print('')

#Exercício 4:
# 4. Faça um programa em Python que:
# Leia a largura e a altura de uma parede em metros.
# Calcule a área da parede.
# Calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m².

print('Exercício 4:')
print('')

largura = int(input('Digite o valor da largura: '))
altura = int(input('Digite o valor da altura: '))
area_parede = largura * altura
qt_tinta = area_parede * 0.5

print('')
print(f'A área da parede é de {area_parede} metros quadrados.')
print('')
print(f'A quantidade de tinta necessária para pintar a parede é de {qt_tinta} litros.')
print('')

# 5. Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

print('Exercício 5:')
print('')

nota01 = int(input('Digite o valor da 1º Menção: '))
nota02 = int(input('Digite o valor da 2º Menção: '))
resultado = nota01 + nota02
media = resultado / 2

print('')
print(f'O valor da média é {media}.')
print('')

# 6. Sistema de Votação (if/elif/else)
# Crie um programa que leia a idade de uma pessoa e informe se ela:
# não vota (menor que 16 anos)
# voto opcional (16 ou 17 anos, ou acima de 65 anos)
# voto obrigatório (de 18 a 65 anos)

print('Exercício 6:')
print('')

idade = int(input('Digite a sua idade: '))

print('')
if idade < 16:
    print('Você não pode votar ainda.')
elif idade < 18:
    print('Você pode votar. Mas não é obrigado a fazer isso.')
elif idade > 65:
    print('Aqui você também não é obrigado a votar.')
else:
    print('Você deve votar!')
print('')

# 7. Aprovação do Aluno (if/else)
# Faça um programa que leia a média final de um aluno e informe se ele está:
# Aprovado (média maior ou igual a 6)
# Reprovado (média menor que 6)

print('Exercício 7:')
print('')

mencao01 = int(input('Digite o valor da 1º Nota: '))
mencao02 = int(input('Digite o valor da 2º Nota: '))
mencao03 = int(input('Digite o valor da 3º Nota: '))
mencao04 = int(input('Digite o valor da 4º Nota: '))
resultado = mencao01 + mencao02 + mencao03 + mencao04
mencaofinal = resultado / 4


print('')
print(f'O valor da sua menção final é {mencaofinal}.')
print('')
if mencaofinal >= 6:
    print('Parabéns! Você foi aprovado neste bimestre!')
else:
    print('Infelizmente você foi reprovado neste bimestre. Faça-o novamente para tentar passar para o próximo!')