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
        estado_civil = str(input('*Estado civil:?'))
        if estado_civil.isnumeric():
            print('\033[1;41mNão aceitamos números neste campo. Apenas escrita por extenso.\033[0;0m')
        elif estado_civil == '':
            print('\033[1;41mEste campo também não poderá ficar em branco.\033[0;0m')
        else:
            break
    print('---' * 24)
    while True:
        n = str(input(f'Seu nome completo é: {nome} :? Digite [S - SIM ou C - CORRIGIR]:?')).strip().upper()
        print('---' * 24)
        if n == 'S':
            break
        elif n == 'C':
            print('(*corrigindo) - ',end=' ')
            nome = str(input('*Digite seu nome completo:'))
        elif n == '':
            print(f'\033[1;41mDIGITE APENAS [S - SIM ou C - CORRIGIR]:\033[0;0m')
            if n == 'S':
                break
            elif n == 'C':
                break
    while True:
        cpf = str(input('*Digite o número do seu CPF:?')).strip().replace('.','').replace(',','').replace('-','')
        if cpf.isnumeric():
            if len(cpf) == 11:
                break
            elif len(cpf) < 11:
                print('\033[1;41mNúmero de CPF inválido. Preencha novamente!\033[0;0m')
                continue
        else:
            print('\033[1;41mDigite somente números./Este campo também não poderá ficar em branco.\033[0;0m')
    print('---' * 24)
    while True:
        profissao = str(input('*Profissão:?')).strip()
        if profissao.isnumeric():
            print('\033[1;41mNão aceitamos números neste campo. Somente escrita or extenso.\033[0;0m')
            continue
        else:
            break
    while True:
        print('---' * 24)
        salario = str(input('*Digite seu salário:? R$:')).strip().replace('.','').replace(',','')
        print('---' * 24)
        if salario.isnumeric():
            salariocliente = float(salario)
            break
        else:
            print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')
    while True:
        emprestado = str(input('*Digite o valor que você deseja financiar:? R$:')).strip()
        print('---' * 24)
        if emprestado.isnumeric():
            valoremprestado = float(emprestado)
            break
        else:
            print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS (sem pontos e virgulas)\033[0;0m\n\033[1;41m- não é necessário digitar números decimais:                   \033[0;0m')
    while True:
        parcelas = str(input('*Em quantas parcelas você gostaria de pagar seu financiamento:?')).strip().replace('.','').replace(',','')
        print('---' * 24)
        if parcelas.isnumeric():
            totparcelas = int(parcelas[:2])
            if totparcelas < 6:
                print(f'\033[1;41mA QUANTIDADE MÍNIMA DE PARCELAS É 6: [DIGITE NOVAMENTE]:\033[0;0m')
                continue
            elif totparcelas > 42:
                print(f'\033[1;41mA QUANTIDADE MÁXIMA DE PARCELAS É 42: [DIGITE NOVAMENTE]:\033[0;0m')
                continue
            break
        else:
            print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')
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
            reiniciar = str(input('*Digite N P/ NOVA SIMULAÇÃO: ou S P/ SAIR:? ')).strip().upper()[0]
            if reiniciar == 'N':
                break
            elif reiniciar == 'S':
                print()
                print('          -----| FIM DO PROGRAMA |-----')
                exit()
            else:
                print('\033[1;41mDigite N P/ NOVA SIMULAÇÃO: ou S P/ SAIR:\033[0;0m')
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
        contratar = str(input('*Deseja contratar sua proposta:? Digite: [C - CONFIRMA / S - SAIR]?:')).strip().upper()[0]
        if contratar == 'C':
            print('---' * 24)
            print('Antes de finalizar precisaremos de informações complementares')
            print('---' * 24)
            print('Abaixo seguem as informações já inseridas:')
            print(f'Nome completo:{nome}')
            print(f'Estado civil: {estado_civil}')
            print(f'Seu número de CPF é: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
            print(f'Profissão: {profissao}')
            print('---' * 24)
            print('Para concluir a contratação necessitaremos novas informações.\nPreencha o formulário a seguir:')
            print('---' * 24)
        elif contratar == 'S':
            print()
            print('          -----| FIM DO PROGRAMA |-----')
            exit()
        else:
            print('\033[1;41mDigite somente C ou S.\033[0;0m')
        while True:
            email = str(input('*E-mail:?'))
            if email.isnumeric():
                print('\033[1;41mNão aceitamos números neste campo. Apenas seu endereço de e-mail por extenso.\033[0;0m')
                continue
            elif email == '':
                print('\033[1;41mEste campo também não poderá ficar em branco.\033[0;0m')
                continue
            else:
                break
        print('---' * 24)
        while True:
            estado = str(input('*Estado onde reside:?')).strip()
            if estado.isnumeric():
                print('\033[1;41mNão aceitamos números neste campo. Apenas escrita por extenso.\033[0;0m')
            elif estado == '':
                print('\033[1;41mEste campo também não poderá ficar em branco.\033[0;0m')
            else:
                break
        print('---' * 24)
        while True:
            cidade = str(input('*Cidade onde reside:?')).strip()
            if estado.isnumeric():
                print('\033[1;41mNão aceitamos números neste campo. Apenas escrita por extenso.\033[0;0m')
            elif cidade == '':
                print('\033[1;41mEste campo também não poderá ficar em branco.\033[0;0m')
            else:
                break
        print('---' * 24)
        while True:
            endereco = str(input('*Endereço:?')).strip()
            if endereco.isnumeric():
                print('\033[1;41mNão aceitamos números neste campo. Apenas escrita por extenso.\033[0;0m')
            elif endereco == '':
                print('\033[1;41mEste campo também não poderá ficar em branco.\033[0;0m')
            else:
                break
        print('---' * 24)
        while True:
            n_residencia = str(input('*Nº da casa:?')).strip().replace('.', '').replace(',', '')
            if n_residencia.isnumeric():
                break
            else:
                print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')
                continue
        print('---' * 24)
        while True:
            cep = str(input('*Digite seu CEP:?'))
            if cep.isnumeric():
                break
            else:
                print(f'\033[1;41mVALOR INVÁLIDO - DIGITE SOMENTE NÚMEROS :\033[0;0m')
                continue
        print('---' * 24)
        print('Verifique se todas as informações estão corretas. Caso haja divergência\nde dados, seu financiamente poderá ser recusado e todo processo terá que ser\nrefeito novamente.')
        print('---' * 24)
        print('Abaixo seguem todas informações inseridas:')
        print('---' * 24)
        print(f'Nome completo:{nome}')
        print(f'Estado civil: {estado_civil}')
        print(f'Número de CPF: {cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}')
        print(f'Profissão: {profissao}')
        print(f'Remuneração mensal: {salariocliente:.2f}')
        print(f'Residente na cidade de: {cidade}, {estado}')
        print(f'Mais precisamente na {endereco}, nº {n_residencia}')
        print(f'Cep: {cep}')
        print(f'Você optou por financiar R$: {valoremprestado:.2f}\nem {totparcelas} parcelas dê R$ {somatudo:.2f} já acrescida com nossas taxas.')
        print('---' * 24)
        confere_dados = str(input('*As informações acima conferem:? Digite:[C - CONFIRMAR ou R - REFAZER TODO PROCESSO]:?')).strip().upper()
        if confere_dados.isnumeric():
            print('\033[1;41mNão aceitamos números neste campo. Apenas C ou R.\033[0;0m')
        elif confere_dados == 'C':
            print('---' * 24)
            print()
            print('          -----| FIM DO PROGRAMA |-----')
            exit()
            print(f'Proposta contratada com sucesso. Aguarde ! Em breve você receberá um e-mail solicitando\ndocumentos e as últimas informações adicionais.')
            exit()
        elif confere_dados == 'F':
            break
        print('---' * 24)

