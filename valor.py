valor_compra = float(input("Digite o valor da compra: R$ "))
valida_desconto= valor_compra >= 100

if valida_desconto:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"Valor com desconto: R$ {valor_final:.2f}")
else:
    print(f"Valor a pagar: R$ {valor_compra:.2f}")
