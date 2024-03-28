# Um(a) aluno(a) é aprovado (a) quando:
# 1 - tem nota acima de 7 E
# 2 - tem menos de 24 faltas

# Escreva um programa para exibir se um aluno(a) foi aprovado a partir da digitação
# de 2 notas, e do calculo da sua média

# 1. entrada de dados
entrada = input("Digite a primeira nota: ")
nota1 = float(entrada)

entrada = input("Digite a segunda nota: ")
nota2 = float(entrada)

entrada = input("Quantas faltas o aluno teve? ")
faltas = int(entrada)

# 2. processamento
media = (nota1 + nota2) / 2

# 3. saída
print("Média final:", media)
print("Quantidade de faltas:", faltas)
print("Aluno aprovado? ", (media >= 7) and (faltas < 24))