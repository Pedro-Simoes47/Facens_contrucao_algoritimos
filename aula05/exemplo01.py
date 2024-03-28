# Operadores aritméticos
# + - * / %

print( 5 / 2 )
print( 5 // 2 ) # divisão inteira
print( 5 % 2 ) # resto da divisão
print( 5 ** 2 ) # potência ( 5 elevado ao quadrado )

# Operadores relacionais
# > >= < <= != ==

print( 2 < 5 )
print( 2 >= 5 )
print( 2 != 5 )
print( 2 == 5 )


# Operadores lógicos
# or and not

# vai ter churrasco?
# 1- tem que ter carne
# 2- tem que ter carvão

carne = False
carvao = False

churrasco = carne and carvao # só é true se ambos forem true

print(churrasco)

# posso trocar a lâmpada?
# 1 - tem uma lâmpada igual
# 2 - tem uma lâmpada equivalente

lampada_igual = False
lampada_equivalente = False

trocar = lampada_igual or lampada_equivalente # só é false se ambas forem false

# print(trocar)

chuva = False
print(not chuva) # inverte true para false e vice-versa