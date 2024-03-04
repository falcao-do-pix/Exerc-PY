var_int = []
var_float = float()

for cont in range(0, 3):
    if (cont == 2):
        var_float = float(input("Digite um valor decimal: "))
	#teste de valor 
    else:
        var_int.append(int(input("Digite um valor inteiro: ")))

a = (2 * var_int[0]) * (var_int[1] / 2)
b = (3 * var_int[0]) + (var_float)
c = (var_float ** 3)

print(f"Produto do dobro do primeiro com a metade do segundo: {a}\nSoma do triplo do primeiro com o terceiro: {b}\nO terceiro elevado ao cubo: {c}")
