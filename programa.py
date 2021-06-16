valor = float(0)
salariocliente = 0
n = ''
valoremprestado = 0
totparcelas = 0

print('---' * 24)
print(f'\033[7;40m{"  CRÉDITO PARA TODXS - EMPRÉSTIMO PESSOAL  ":*^72}\033[0;0m')
print('---' * 24)
print('Nossas análises e linhas de Créditos é com base em parcelas de no máximo\n30% do seu salário, para que assim nossos clientes tenham mais saúde\nfinanceira e segurança! ')
print('---' * 24)

nome = str(input('Digite seu nome:'))
print('---' * 24)
while True:
    n = str(input(f'Seu nome completo é: {nome} :? Digite [S - SIM ou C - CORRIGIR]:?')).strip().upper()[0]
    print('---' * 24)
    if n == 'S':
        break
    elif n == 'C':
        print('(*corrigindo) - ',end=' ')
        nome = str(input('Digite seu nome:'))
    elif n != 'S' or 'C':
        print(f'\033[1;41mDIGITE APENAS [S - SIM ou C - CORRIGIR]:\033[0;0m')
        if n == 'S':
            break
        elif n == 'C':
            break
while True:
    salario = str(input('Digite seu salário:? R$:')).strip().replace('.','').replace(',','')
    print('---' * 24)
    if salario.isnumeric():
        salariocliente = float(salario)
        print(f'R$: {salariocliente:.2f}'.replace('.',','))
        break
    else:
        print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

while True:
    emprestado = str(input('Digite o valor que você precisa:? R$:')).strip().replace('.','').replace(',','')
    print('---' * 24)
    if emprestado.isnumeric():
        valoremprestado = float(emprestado)
        print(f'R$: {valoremprestado:.2f}'.replace('.',','))
        break
    else:
        print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

while True:
    parcelas = str(input('Em quantas parcelas você gostaria de pagar o valor emprestado:?')).strip().replace('.','').replace(',','')
    print('---' * 24)

    if parcelas.isnumeric():
        totparcelas = int(parcelas)
        print(f'{totparcelas} parcelas'.replace('.',','))
        break
    else:
        print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

print('---' * 24)
print(f'Muito Obrigado Sr {nome}. Com base nas informações inseridas ')
print(f'em nosso sistema. Temos uma excelente proposta para você !')
print('---' * 24)
print('///' * 24)
print('---' * 24)
print()
print()
print('\033[1;42m\033[1;30mEscrita...\033[0;0m')
print()
print()
print('---' * 24)
print('///' * 24)
print('---' * 24)
print('                -------- | FIM DO PROGRAMA | --------')