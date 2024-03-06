"""
Aluno: Leonardo Fabrício De Ávila Silva
Matrićula: 202203284649

13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
"""

altura = float(input("Informe a sua altura (M): "))
sx = input("Sexo: [M/F] ").upper()
# O método upper deixa a string em maiúscula.

# O operador "not in" verifica se uma string NÃO está contida em outra. 
# A lógica aqui é permanecer no loop até que o usuário digite M ou F. Qualquer outro tipo de valor é considerado inválido para o propósito deste programa.

while sx not in "MF":
   print("\033c", end="")
   print("Valor inválido! Tente novamente.")
   sx = input("Sexo: [M/F] ").upper()

if sx == "M":
   peso_ideal = (72.7 * altura) - 58
else:
   peso_ideal = (62.1 * altura) - 44.7

# Imprime um caractere especial que limpa a tela.
print("\033c", end="")

print(f"Altura: {altura:.2f}m")
print(f"Sexo: {sx}")
print(f"Peso ideal: {peso_ideal:.2f}Kg")
