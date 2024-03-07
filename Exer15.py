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
