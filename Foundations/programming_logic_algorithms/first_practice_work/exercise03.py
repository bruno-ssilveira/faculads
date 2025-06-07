# Modelos e preços
modelos = {
    "MCS": 1.80,
    "MLS": 2.10,
    "MCE": 2.90,
    "MLE": 3.20
}

# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input(">>").upper()
        if modelo in modelos:
            return modelo, modelos[modelo]
        else:
            print("Escolha inválida, entre com o modelo novamente\n")

# Função para obter e validar o número de camisetas com desconto
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Entre com o número de camisetas: "))
            if quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez.\nPor favor, entre com o número de camisetas novamente.\n")
            elif quantidade >= 2000:
                return quantidade, quantidade * 0.88
            elif quantidade >= 200:
                return quantidade, quantidade * 0.93
            elif quantidade >= 20:
                return quantidade, quantidade * 0.95
            elif quantidade > 0:
                return quantidade, quantidade
            else:
                print("Quantidade inválida, digite novamente.\n")
        except ValueError:
            print("Valor não numérico, digite novamente.\n")

# Função para escolher o tipo de frete
def frete():
    while True:
        print("Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        opcao = input(">>")
        if opcao == "1":
            return 100.00
        elif opcao == "2":
            return 200.00
        elif opcao == "0":
            return 0.00
        else:
            print("Opção inválida, digite novamente.\n")


print("Bem-vindo a Fábrica de Camisetas do Bruno Silveira")


modelo, preco = escolha_modelo()

quantidade_original, quantidade_com_desconto = num_camisetas()

valor_frete = frete()

# Cálculo final
total = (preco * quantidade_com_desconto) + valor_frete

# Exibição do resultado final
print(f"Total: R$ {total:.2f} (Modelo: {preco:.2f} * Quantidade(com desconto): {quantidade_com_desconto:.0f} + frete: {valor_frete:.2f})")
