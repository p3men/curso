valor_compra = float(input("Digite o valor a comprar: "))
if valor_compra >=100:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print("Parabens! voce ganhou seu desconto de 10%")
    print("Valor final da compra: R$", valor_final)
else:
    print("infelizmente, voce nao ganhou desconto")
print("Valor final da compra: R$", valor_compra)