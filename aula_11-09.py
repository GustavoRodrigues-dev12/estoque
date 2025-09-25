print('Cadastro de Produtos')

matriz = []

while True:
    print('-=-' * 15)
    verify = input(f'Escolha uma opção:\n 1- Cadastrar\n 2- Visualizar\n 3- Editar(preço/quantidade)\n 4- Excluir\n ').lower()
    print('-=-' * 15)
    if verify == '1':
        produto = []
        nome = input('Digite o nome do produto: ')
        produto.append(nome)
        preço = float(input('Digite o preço do produto: '))
        produto.append(preço)
        quant = int(input('Digite a quantidade do produto: '))
        produto.append(quant)
        valor_total = preço * quant
        produto.append(valor_total)
        matriz.append(produto)
        print(produto)

    elif verify == '2':
        print(f'Produtos cadastrados: ')
        for p in matriz:
            print(f'Nome: {p[0]} | Preço: R${p[1]} | Quantidade: {p[2]} | Valor Total: R${p[3]}')

    elif verify == '3':
        operaçao = int(input('O que deseja editar?\n 1- Preço\n 2- Quantidade\n '))
        if operaçao == 1:
            nome_produto = input('Digite o nome do produto que deseja editar o preço: ')
            for p in matriz:
                if nome_produto in p:
                    novo_preço = float(input('Digite o novo preço: '))
                    p[1] = novo_preço
                    p[3] = novo_preço * p[2]
                    print(f'Preço atualizado com sucesso! Novo preço: R${p[1]} | Novo valor total: R${p[3]}') 

        elif operaçao == 2:
            nome_produto = input('Digite o nome do produto que deseja editar a quantidade: ')
            for p in matriz:
                if nome_produto in p:
                    nova_quantidade = int(input('Digite a nova quantidade: '))
                    p[2] = nova_quantidade
                    p[3] = nova_quantidade * p[1]
                    print(f'Quantidade atualizada com sucesso! Nova quantidade: {p[2]} | Novo valor total: R${p[3]}')

    elif verify == '4':
        nome_produto = input('Digite o nome do produto que deseja excluir: ')
        for p in matriz:
            if nome_produto in p:
                matriz.remove(p)
                print(f'Produto {nome_produto} excluído com sucesso!')
