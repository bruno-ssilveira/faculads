print("Bem vindo à Empresa do Bruno Silveira")

lista_funcionarios = []
id_global = 5354784

def cadastrar_funcionario(id):
    print("\n---------- MENU CADASTRAR FUNCIONÁRIO --------------")
    print(f"Id do Funcionário: {id}")
    
    funcionario = {}
    funcionario['id'] = id
    funcionario['nome'] = input("Por favor entre com o nome do Funcionário: ")
    funcionario['setor'] = input("Por favor entre com o setor do Funcionário: ")
    funcionario['salario'] = float(input("Por favor entre com o salário do Funcionário: "))

    lista_funcionarios.append(funcionario.copy())
    print("----------------------------------------------------\n")

def consultar_funcionarios():
    while True:
        print("---------- MENU CONSULTAR FUNCIONÁRIO --------------")
        print("1 - Consultar Todos")
        print("2 - Consultar por Id")
        print("3 - Consultar por Setor")
        print("4 - Retornar ao menu")
        opcao = input(">> ")

        if opcao == '1':
            for func in lista_funcionarios:
                print(f"\nId: {func['id']}")
                print(f"Nome: {func['nome']}")
                print(f"Setor: {func['setor']}")
                print(f"Salário: {func['salario']:.2f}")
            print("----------------------------------------------------")
        elif opcao == '2':
            id_busca = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for func in lista_funcionarios:
                if func['id'] == id_busca:
                    print(f"\nId: {func['id']}")
                    print(f"Nome: {func['nome']}")
                    print(f"Setor: {func['setor']}")
                    print(f"Salário: {func['salario']:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opcao == '3':
            setor_busca = input("Digite o setor: ")
            encontrados = [f for f in lista_funcionarios if f['setor'].lower() == setor_busca.lower()]
            if encontrados:
                for func in encontrados:
                    print(f"\nId: {func['id']}")
                    print(f"Nome: {func['nome']}")
                    print(f"Setor: {func['setor']}")
                    print(f"Salário: {func['salario']:.2f}")
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == '4':
            return
        else:
            print("Opção inválida, tente novamente.\n")

def remover_funcionario():
    while True:
        try:
            id_remover = int(input("Digite o ID do funcionário que deseja remover: "))
            for i, func in enumerate(lista_funcionarios):
                if func['id'] == id_remover:
                    del lista_funcionarios[i]
                    print("Funcionário removido com sucesso.")
                    return
            print("Id inválido. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Digite um número.")

while True:
    print("--------------- MENU PRINCIPAL ------------------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = input(">> ")

    if opcao == '1':
        cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
