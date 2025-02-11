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