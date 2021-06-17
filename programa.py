valor = float(0)
salariocliente = 0
n = ''
valoremprestado = 0
totparcelas = 0

print('---' * 24)
print(f'\033[7;40m{"  CRÉDITO PARA TODXS - EMPRÉSTIMO PESSOAL  ":*^72}\033[0;0m')
print('---' * 24)
print('A melhor taxa do mercado, 2% ao mês. Além disso nossas análises e linhas\nde Créditos é com base em parcelas de no máximo 30% do seu salário, para\nque assim nossos clientes tenham mais saúde financeira e segurança! ')
print('---' * 24)
print(' -----------| TEMOS UMA PROPOSTA PARA VOCÊ! SIMULE AGORA! |-----------')
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
    emprestado = str(input('Digite o valor que você deseja financiar:? R$:')).strip().replace('.','').replace(',','')
    print('---' * 24)
    if emprestado.isnumeric():
        valoremprestado = float(emprestado)
        print(f'R$: {valoremprestado:.2f}'.replace('.',','))
        break
    else:
        print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

while True:
    parcelas = str(input('Em quantas parcelas você gostaria de pagar seu financiamento:?')).strip().replace('.','').replace(',','')
    print('---' * 24)

    if parcelas.isnumeric():
        totparcelas = int(parcelas)
        print(f'{totparcelas} parcelas'.replace('.',','))

        if totparcelas < 6:
            print(f'\033[1;41mA QUANTIDADE MÍNIMA DE PARCELAS É 6: [DIGITE NOVAMENTE]:\033[0;0m')
            continue


        break
    else:
        print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

# AQUI IRÁ TODO O CALCULO DO SISTEMA

resultado = float(valoremprestado/totparcelas)
addjurosmensal = float(0.02*resultado)
somatudo = float(resultado+addjurosmensal)
analisefinal = float(0.30*salariocliente)

if somatudo > analisefinal:
    print('---' * 24)
    print(f'Muito Obrigado Sr {nome}. Com base nas informações inseridas ')
    print(f'em nosso sistema. Temos uma excelente proposta para você !')
    print('---' * 24)
    print(f' ///////////////////////// ---|\033[1;41m NEGADO ! \033[0;0m|--- /////////////////////////')
    # print('///' * 24)
    print('---' * 24)
    print()
    print(f'Infelizmente sua solicitação foi negada por que o valor de sua parcela\né superior a 30% do seu salário! Queremos muito ajudar você ! Tente uma\nnova simulação com mais de {totparcelas} parcelas, ou escolha um valor de\nfinanciamento inferior a {valoremprestado:.2f}')
    print()
    print(f'Você optou por financiar R$: {valoremprestado:.2f} em {totparcelas} parcelas dê R$ {somatudo:.2f}.')
    print()
    print('---' * 24)
    print('///' * 24)
    print('---' * 24)



print('                -------- | FIM DO PROGRAMA | --------')