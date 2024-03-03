"""
Faculdade Martha Falcão Wyden
Disciplina: Desenvolvimento Rápido de Aplicações em Python
Aluno: Leonardo Fabrício de Ávila Silva
Matrícula: 202203284649

14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
os dados do programa com as mensagens adequadas.
"""

peso_peixes = float(input("Peso dos peixes (Kg): "))

if (peso_peixes > 50):
   excesso = peso_peixes - 50
   multa = excesso * 4
   print(f"Quantidade de quilos além do limite (50Kg): {excesso}")
   print(f"Multa: R${multa:.2f}")
else:
   print("Não há excesso de quilos.")
