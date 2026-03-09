numero = float(input("Digite um número: "))
valida_pos = numero > 0
valida_neg = numero < 0
valida_zero = numero == 0

if valida_pos:
    print("O número é positivo.")
elif valida_neg:
    print("O número é negativo.")
elif valida_zero:
    print("O número é zero.")
