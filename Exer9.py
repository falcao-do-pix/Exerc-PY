def fahrentocelsius(fahrenheit):
    return (5 * ( (fahrenheit - 32) / 9))

fahrenheit = float(input("Digite sua temperatura em Fahrenheits: "))
celsius = fahrentocelsius(fahrenheit)
print(f"A temperatura em celsius é: {celsius}")
