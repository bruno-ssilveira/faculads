print("\nWelcome to Bruno Silveira's Store!")

# Data input to installment and order value
quantidadeParcelas = 0
while quantidadeParcelas < 1:
    valorDoPedido = float(input("\nEntre com o valor do pedido: "))
    quantidadeParcelas = float(input("Entre com a quantidade de parcelas: "))
    if quantidadeParcelas < 1:
        print("A quantidade mínima de parcelas é 1x")
        

# Applying the installment logic
if quantidadeParcelas < 4:
    juros = 0
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

# Starting the final calculation with order value and installment fees
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

if quantidadeParcelas >= 4:
    print(f"\nParcelamento em {quantidadeParcelas:.0f}x com juros de {juros * 100:.0f}%:")
    print(f"Valor de cada parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total parcelado: R$ {valorTotalParcelado:.2f}")