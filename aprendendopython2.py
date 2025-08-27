# Operadores

numero01 = int(input('Digite um número: '))
numero02 = int(input('Digite um segundo número: '))

soma = numero01 + numero02
subtracao = numero01 - numero02
multiplicacao = numero01 * numero02
divisao = numero01 / numero02
divisaoInteira = numero01 // numero02
sobra = numero01 % numero02
potenciacao = numero01 ** numero02
raiz = pow(numero01, 0.5)

print('A soma é: ', soma)
print('A substração é: ', subtracao)
print('A multiplicação é: ', multiplicacao)
print('A divisão é: ', divisao)
print('A divisão inteira é: ', divisaoInteira)
print('A sobra é: ', sobra)
print('A potenciação é: ', potenciacao)
print('A raiz é: ', raiz)

# Funções Condicionais

print('============================================')
print('Seja Bem-Vindo ao Sistema de Horas!')
print('============================================')

hora = int(input('Digite um horário: '))

if hora < 12:
    print('Bom Dia!')
elif hora < 18:
    print('Boa Tarde!')
else:
    print('Boa Noite!')

# area = largura * altura
# 3º semana: laços de repetição
# 4º semana: array