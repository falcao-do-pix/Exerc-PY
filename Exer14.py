peso_peixes = float(input("Peso dos peixes (Kg): "))

if (peso_peixes > 50):
   excesso = peso_peixes - 50
   multa = excesso * 4
   print(f"Quantidade de quilos além do limite (50Kg): {excesso}")
   print(f"Multa: R${multa:.2f}")
else:
   print("Não há excesso de quilos.")
