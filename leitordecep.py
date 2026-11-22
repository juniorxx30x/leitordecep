
#INICIO DO CODIGO / BIBLIOTECAS


import requests
import time

print("\033[36m/////// SISTEMA DE CONSULTA DE CEP juniorxx30 ////////////\033[m")

#PAINEL DE CONSULTA

def consultar_cep():
    print('Tudo bem, abrindo painel de consultas...')
    time.sleep(2)
    cep = input('\033[32mOlá, Seja Muito Bem Vindo, Digite O Seu CEP Sem Hífen (-):\033[m  ')
    cep = cep.strip()
    cep = cep.replace('-', '').replace('.', '')


#VERIFICAR SE O CODIGO TEM CARACTERES OU ULTRAPASSA O LIMITE 

    

    while not cep.isnumeric() or len(cep) != 8:
        cep = input('\033[32mDigite Somente Números, Digite O Seu CEP Sem Hífen (-):\033[m  ')
        cep = cep.strip()
        cep = cep.replace('-', '').replace('.', '')

#CONSULTA O CEP

    print('Consultando CEP...')
    time.sleep(2)
    #API VIACEP
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        resultado = requests.get(url, timeout=10) 
        resultado.raise_for_status()
        dados = resultado.json()

    except requests.exceptions.JSONDecodeError:
        print('O servidor retornou uma resposta inválida.')
        return

    except requests.exceptions.RequestException:
        print('Ocorreu Um Erro Na Consulta, Verifique Sua Conexão e Tente Novamente.')
        return

#RESULTADO PAINEL

    if dados.get('erro') == 'true':
        print('O Seu CEP é Inválido!! Abrindo O Painel Novamente...')
    else:
        print('\033[36m................ DADOS COLETADOS ................\033[m')
        print(f"Rua: \033[32m{dados.get('logradouro', 'Não informado')}\033[m")
        print(f"Bairro: \033[32m{dados.get('bairro', 'Não informado')}\033[m")
        print(f"Município: \033[32m{dados.get('localidade', 'Não informado')}\033[m")
        print(f"Estado: \033[32m{dados.get('uf', 'Não informado')}\033[m")
        print('País: \033[32mBra\033[33msil\033[m')


#PAINEL INICIAL

while True:
    print('\033[34m....................\033[m')
    print('1 - Consultar CEP')
    print('2 - Sair')
    print('\033[34m....................\033[m')

    opcao = input('Escolha Uma Opção:  ')

    if opcao == '1':

        time.sleep(2)
        consultar_cep()

    elif opcao == '2':
        print('\033[31mFechando O Sistema...\033[m')
        time.sleep(2)
        break
    else:
        print('\033[31mOpção Inválida!!\033[m')



    
