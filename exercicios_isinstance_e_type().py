# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.

ano = 2024
print("EX1:", type(ano))

print("==========================================")

# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().

print("EX2:", isinstance(3.14159, float))

print("==========================================")

# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.

print("EX3:", type(100) == type(True))

print("==========================================")

# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.

print("EX4:", isinstance(True, int))

print("==========================================")

# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().

res = 5 / 2
print("EX5 type:", type(res))
print("EX5 isinstance float:", isinstance(res, float))

print("==========================================")

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.

def verifica_numero(x):
    if isinstance(x, (int, float, complex)):
        print("É número!")
    else:
        print("Não é número!")
print("EX6:")
verifica_numero(10); verifica_numero(3.14); verifica_numero(3+4j); verifica_numero("a")

print("==========================================")

# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

print("EX7 type==int:", type(True) == int)
print("EX7 isinstance int:", isinstance(True, int))

print("==========================================")

# EX8
# Descubra o tipo do número 3+4j
# usando type().

print("EX8:", type(3+4j))

print("==========================================")

# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().

print("EX9:", isinstance(None, type(None)))

print("==========================================")

# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.

print("Outros:", isinstance(3.0, (int, float, complex)))
print("int:", isinstance(3.0, int))

print("==========================================")
