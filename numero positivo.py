numero = float(input("Digite um numero: "))
valida_pos = numero > 0
valida_neg = numero < 0
valida_zero = numero == 0

if valida_pos:
    print("O numero e positivo.")
elif valida_neg:
    print("O numero e negativo.")
elif valida_zero:
    print("O numero e zero.")
