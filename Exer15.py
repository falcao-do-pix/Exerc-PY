"""
Aluno: Leonardo Fabrício de Ávila Silva
Matrícula: 202203284649


15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
dê:

a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
      + Salário Bruto : R$
      - IR (11%) : R$
      - INSS (8%) : R$
      - Sindicato (5%) : R$
      = Salário Liquido : R$
"""

salario_hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalho = int(input("Qual foi a sua quantidade de horas trabalhadas no mês? "))

salario_bruto = salario_hora * horas_trabalho
valor_ir = salario_bruto * 0.11
valor_inss = salario_bruto * 0.08
valor_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (valor_ir + valor_inss + valor_sindicato)

print()
print("-" * 25)
print(f"Salário Bruto: R${salario_bruto:.2f}")
print()
print("Descontos: ")
print(f"IR (11%): R${valor_ir:.2f}")
print(f"INSS (8%): R${valor_inss:.2f}")
print(f"Sindicato (5%): R${valor_sindicato:.2f}")
print("-" * 25)
print()
print(f"Salário Líquido: R${salario_liquido:.2f}")
