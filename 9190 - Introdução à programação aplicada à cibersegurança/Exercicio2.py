print("----"*21, "ex  8",  "----"*21 )


# Faça um Programa que pergunte dois numeros e imprima o maior
numero = int(input("introduza o primeiro numero: "))
numero2 = int(input("introduza o segundo numero: "))

if numero > numero2:
    print(f"o maior numero é o numero {numero}")
elif numero2 > numero:
    print(f"o maior numero é o numero {numero2}")
else:
    print("os numeros sao iguais")

