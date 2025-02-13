# listas
from numba.core.cgutils import sizeof

idades = [23,15,14, 18, 15,17]


print(idades[0])
print(idades[1])
print(idades[2])
# print(idades[3]) -> IndexError: list index out of range


idades[0] = 999
print(idades[0])


# add
idades.append(41) # adwiciona no final
print(idades)


idades.insert(30, 99)# adiciona na posicao
print(idades)


# remover
print(idades)
idades.remove(15) # remove o valor, a 1 vez que ele aparece
print(idades)

idades.pop() # remove o ultimo
print(idades)

i = idades.pop(4) # remove o valor na posicao 4
print(idades)

print(i)

# idades.remove(888) # ValueError: list.remove(x): x not in list

# idades.pop(40) # IndexError: pop index out of range

print(idades.__len__())
print(len(idades))

print(idades.count(15)) # conta quantas vezes o valor aparece na lista


# se esta contido


print(10 in idades)

print(14 in idades)



# loops



# for



# while