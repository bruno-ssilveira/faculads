# Mensagem de boas-vindas e menu
print("Welcome to the Bruno Silveira's Restaurant")

print("\n--- Cardápio ---")
print("Sabores disponíveis:")
print("BA - Bife Acebolado")
print("FF - Filé de Frango")
print("\nTamanhos e Preços:")
print("P - Pequeno: BA = R$16, FF = R$15")
print("M - Médio:   BA = R$18, FF = R$17")
print("G - Grande:  BA = R$22, FF = R$21")

# Acumulador do valor total
total = 0

# Loop principal
while True:
    sabor = input("\nDigite o sabor desejado (BA/FF): ").upper()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        continue

    tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue

    # Determina nome do sabor e preço
    if sabor == "BA":
        nome_sabor = "Bife Acebolado"
        if tamanho == "P":
            preco = 16
        elif tamanho == "M":
            preco = 18
        else:  # G
            preco = 22
    elif sabor == "FF":
        nome_sabor = "Filé de Frango"
        if tamanho == "P":
            preco = 15
        elif tamanho == "M":
            preco = 17
        else:  # G
            preco = 21

    # Adiciona ao total
    total += preco

    # Mostra item adicionado com nome e preço
    print(f"{nome_sabor} tamanho {tamanho} adicionado por R${preco:.2f}")

    # Pergunta se deseja continuar
    mais_pedidos = input("\nDeseja pedir mais alguma coisa? (Sim/Não): ").upper()
    if mais_pedidos == "SIM":
        continue
    else:
        break

# Mensagem final com o total
print(f"\nPedido finalizado. Total a pagar: R${total:.2f}")