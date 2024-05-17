#Solicitar ao usuario que digite um numero
numero = float (input("Digite um numero: "))
#verificar se o numero e positivo, negativo ou zero
if numero > 0:
    print("O numero é positivo.")
elif numero < 0:
    print("O numero é negativo.")
else:
    print("O numero é zero")