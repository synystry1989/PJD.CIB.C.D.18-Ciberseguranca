print("----"*10, "ex 1",  "----"*10 )
#Faça um Programa que mostre a mensagem "ola mundo" na tela.
<<<<<<< Updated upstream

print("Ola Mundo")
=======
print("Ola mundo")

>>>>>>> Stashed changes

print("----"*10, "ex 2",  "----"*10 )
#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = float(input("Indique um número: "))

print("O número escrito foi:", numero)


print("----"*10, "ex 3",  "----"*10 )
#Faça um Programa que peça dois números e imprima a soma.

numero1 = float(input("Indique o primeiro número: "))

numero2 = float(input("Indique o segundo número: "))

soma = numero1 + numero2

print("A soma dos dois números é:", soma)


print("----"*10, "ex 4",  "----"*10 )
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Solicita as 4 notas bimestrais ao usuário e converte para float
nota1 = float(input("Indique a primeira nota: "))
nota2 = float(input("Indique a segunda nota: "))
nota3 = float(input("Indique a terceira nota: "))
nota4 = float(input("Indique a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média
print("A média das notas é:", media)



print("----"*10, "ex 5",  "----"*10 )
#Faça um Programa que converta metros para centímetros.

# Solicita ao usuário o valor em metros e converte para float
metros = float(input("Indique o valor em metros: "))

centimetros = metros * 100

print(f"{metros} metros equivalem a {centimetros} centímetros.")


print("----"*10, "ex 6",  "----"*10 )
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

#pequena interacao com o pedido anterior fazendo a conversao inversa
lado = float(input("Indique o valor em centimetros do lado do quadrado: "))

area = lado ** 2
dobroArea = (area * 2)/100

5
print(f"O dobro da área do quadrado é: {dobroArea} metros")


print("----"*10, "ex 7",  "----"*10 )
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#    Calcule e mostre o total do seu salário no referido mês.

vHora = float(input("Quanto ganha por hora?: "))

hTrabalhadas = float(input("Indique o número de horas trabalhadas no mês: "))

salario = vHora * hTrabalhadas

#fui ver como formatar com duas casas decimais 
print(f"O salário ganho este mes foi de {salario:.2f} €")


2
