nome = "Gonçalo" # str
idade = 38       # int

print(f"Ola mundo, {nome}, sou de Lisboa, tenho {idade} anos")
print("Ola mundo,", nome,", sou de Lisboa, tenho", idade, "anos")

# cmt


"ola mundo"

"""
cmt 
multi
linha    
    
"""

'''

cmt 
multi
linha    
    
'''


print("""
      multi
cmt         multi         
multi multi
linha   multi 
    
""")


print("\n   multi\ncmt      multi\nmulti multi\nlinha   multi")




"""
    
\n - > new line -> muda de linha
\t -> cria uma tab (4 espaços)
    
"""


'''1. Strings com Aspas Triplas
a) Uso de """ ... """ ou ''' ... '''
Você pode escrever uma string que ocupa várias linhas usando aspas triplas, seja com aspas duplas ou simples. Esse recurso é útil quando você quer definir uma string que já vem formatada com quebras de linha e espaçamentos exatamente como você escreveu.

Exemplo:

python
Copiar
Editar
"""
cmt 
multi
linha    
    
"""
e

python
Copiar
Editar
'''
cmt 
multi
linha    
    
'''
Observações:

Essas strings mantêm as quebras de linha e espaços.
Embora muitas vezes sejam usadas como "comentários" ou para documentar funções (docstrings), elas não são comentários de fato. O Python ignora as docstrings em certos contextos, mas o correto para comentar linhas é usar o caractere #.
2. Uso do print com String Multi-linha
a) Imprimindo uma string multi-linha escrita com aspas triplas:
python
Copiar
Editar
print("""
      multi
cmt         multi         
multi multi
linha   multi 
""")
Neste caso:

A string entre as aspas triplas já contém as quebras de linha e espaços exatamente como foram escritos.
Quando você chama print(), o Python exibe o conteúdo exatamente dessa forma.
b) Imprimindo com sequências de escape (\n):
python
Copiar
Editar
print("\n   multi\ncmt      multi\nmulti multi\nlinha   multi")
Aqui:

\n é uma sequência de escape que indica "nova linha". Ou seja, sempre que o Python encontra \n, ele pula para a próxima linha.
Se você usasse \t, seria inserida uma tabulação (normalmente equivalente a 4 espaços, mas isso pode variar conforme o ambiente).
Exemplo com \t:

python
Copiar
Editar
print("multi\tcmt\tmulti")
Esse comando imprime "multi", depois um tab, "cmt", outro tab e "multi". A tabulação ajuda a alinhar o texto.

3. Diferença Prática
Com aspas triplas:
Você escreve o texto exatamente como quer que apareça, mantendo a formatação (quebras de linha, espaços) sem precisar usar sequências de escape.

Com \n e \t:
Você constrói a string em uma única linha (ou várias, mas controlando manualmente as quebras e tabulações) usando sequências de escape para indicar onde devem ocorrer as quebras de linha ou as tabulações.

Resumindo
Aspas triplas (""" ou):
Permitem escrever strings que se estendem por várias linhas, preservando a formatação. Útil para textos longos ou para criar docstrings (que servem de documentação para funções e classes).

Sequência de escape \n:
Insere uma nova linha dentro da string.
Sequência de escape \t:
Insere uma tabulação (um espaço maior, normalmente 4 espaços).

Ambas as abordagens têm seus usos e a escolha depende do que você achar mais legível ou adequado para o seu caso.

'''


"""
    
    str -> Texto 
    int -> inteiros 
    float -> deciamais
    bool - T / F  
    
    
"""


idade_str = input("qual a sua idade: ")

idade2 = int(idade_str) # criar um int a partir de uma str

print(f"a idade é , {idade2}")


idade3 = int(input("qual a sua idade: "))
print(f"a idade é , {idade3}")

