altura = float(input("Informe a sua altura (M): "))
sx = input("Sexo: [M/F] ").upper()

while sx not in "MF":
   print("\033c", end="")
   print("Valor inválido! Tente novamente.")
   sx = input("Sexo: [M/F] ").upper()

if sx == "M":
   peso_ideal = (72.7 * altura) - 58
else:
   peso_ideal = (62.1 * altura) - 44.7

print("\033c", end="")

print(f"Altura: {altura:.2f}m")
print(f"Sexo: {sx}")
print(f"Peso ideal: {peso_ideal:.2f}Kg")
