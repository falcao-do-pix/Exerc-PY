def media():
 soma = 0
 for i in range(4):
     nota = float(input(f'Digite a nota {i+1}: '))
     soma += nota

 media = soma / 4

 print(f'A média das notas é: {media}')




media()