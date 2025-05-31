print("\nWelcome to Bruno Silveira's Store!")

# Data input to installment and order value
valorDoPedido = float(input("\nEntre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

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

print(f"\nParcelamento em {quantidadeParcelas}x com juros de {juros * 100:.0f}%:")
print(f"Valor de cada parcela: R$ {valorDaParcela:.2f}")
print(f"Valor total parcelado: R$ {valorTotalParcelado:.2f}")