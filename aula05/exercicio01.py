# escreva um programa que leia a idade de uma pessoa
# e mostre true se ele pode dirigir, e false caso contrário
# condição para dirigir é ter idade pelo menos 18 anos

idade = int( input('Qual sua idade? ') )

# print(type(idade))

pode_dirigir = idade >= 18

print('Você pode dirigir?', pode_dirigir)