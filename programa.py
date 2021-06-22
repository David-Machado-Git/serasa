valor = float(0)
salariocliente = 0
n = ''
valoremprestado = 0
totparcelas = 0


print('---' * 24)
print(f'\033[7;40m{"  CRÉDITO PARA TODXS - EMPRÉSTIMO PESSOAL  ":*^72}\033[0;0m')
print('---' * 24)
print('A melhor taxa do mercado, 2% ao mês. Além disso nossas análises e linhas\nde Créditos é com base em parcelas de no máximo 30% do seu salário, para\nque assim nossos clientes tenham mais saúde financeira e segurança! ')

while True:
    print('---' * 24)
    print(' -----------| TEMOS UMA PROPOSTA PARA VOCÊ! SIMULE AGORA! |-----------')
    print('---' * 24)
    nome = str(input('*Digite seu nome completo:'))
    print('---' * 24)
    if nome == '':
        print(f'\033[1;41mSeu nome não pode estar em branco :\033[0;0m')
        nome = str(input('*Por favor digite seu nome completo:'))
        while nome == '':
            print(f'\033[1;41mSeu nome não pode estar em branco :\033[0;0m')
            nome = str(input('*Por favor digite seu nome completo:'))

    while True:
        n = str(input(f'Seu nome completo é: {nome} :? Digite [S - SIM ou C - CORRIGIR]:?')).strip().upper()[0]
        print('---' * 24)
        if n == 'S':
            break
        elif n == 'C':
            print('(*corrigindo) - ',end=' ')
            nome = str(input('*Digite seu nome completo:'))
        elif n != 'S' or 'C':
            print(f'\033[1;41mDIGITE APENAS [S - SIM ou C - CORRIGIR]:\033[0;0m')
            if n == 'S':
                break
            elif n == 'C':
                break
    while True:
        cpf = str(input('*Digite o número do seu CPF:?'))
        if cpf.isnumeric():
            break
        else:
            print('\033[1;41mDigite somente números./Este campo também não poderá ficar em branco.\033[0;0m')
    while True:
        print('---' * 24)
        salario = str(input('Digite seu salário:? R$:')).strip().replace('.','').replace(',','')
        print('---' * 24)
        if salario.isnumeric():
            salariocliente = float(salario)
            # print(f'R$: {salariocliente:.2f}'.replace('.',','))
            break
        else:
            print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')

    while True:
        emprestado = str(input('Digite o valor que você deseja financiar:? R$:')).strip().replace('.','').replace(',','')
        print('---' * 24)
        if emprestado.isnumeric():
            valoremprestado = float(emprestado)
            # print(f'R$: {valoremprestado:.2f}'.replace('.',','))
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
        print(f'Infelizmente sua solicitação foi negada pois o valor da parcela mensal\nexcede 30% do seu salário! A boa notícia é que queremos muito ajudar\nvocê ! Tente uma nova simulação com mais de {totparcelas} parcelas, ou escolha um\nvalor de financiamento inferior a {valoremprestado:.2f}')
        print()
        print()
        print(f'Obs: Nossas orientações: Para que possamos lhe ajudar, e oferecer uma\nproposta que seja saudável, o valor de suas parcelas mensais não\npoderão exceder 30% de sua remuneração mensal.')
        print()
        print()
        print(f'Você optou por financiar R$: {valoremprestado:.2f}\nem {totparcelas} parcelas dê R$ {somatudo:.2f} já acrescida com nossas taxas.')
        print()
        print('---' * 24)
        print('///' * 24)
        print('---' * 24)
        while True:
            reiniciar = str(input('Digite N P/ NOVA SIMULAÇÃO: ou S P/ SAIR:? ')).strip().upper()[0]

            if reiniciar == 'N':
                break

            elif reiniciar != 'N' and reiniciar != 'S':
                reiniciar = str(input('Digite somente C P/ CONTINUAR: ou S P/ SAIR:? ')).strip().upper()[0]


            elif reiniciar == 'S':
                print()
                print('          -----| FIM DO PROGRAMA |-----')
                exit()
    elif somatudo < analisefinal:
        print('---' * 24)
        print(f'Muito Obrigado Sr {nome}. Com base nas informações inseridas ')
        print(f'em nosso sistema. Temos uma excelente proposta para você !')
        print('---' * 24)
        print(f'//////////////////// ---|\033[1;42m SIMULAÇÃO APROVADA ! \033[0;0m|--- ////////////////////')
        print('---' * 24)
        print()
        print('Parabéns ! ')
        print(f'Você optou por financiar R$: {valoremprestado:.2f}\nem {totparcelas} parcelas dê R$ {somatudo:.2f} já acrescida com nossas taxas.')
        print()
        print('---' * 24)
        print('///' * 24)
        print('---' * 24)
        contratar = str(input('Deseja contratar sua proposta:? Digite: [S - SIM / N - NÃO]?:')).strip().upper()[0]

        if contratar == 'S':
            print('---' * 24)
            print('Antes de finalizar precisaremos de informações complementares')
            print('---' * 24)
            print('Abaixo seguem as informações já inseridas:')
            print(f'Nome completo:{nome}')
            print(f'Seu número de CPF é: {cpf}')









