def celsiustofahren(celsius):
    return (( celsius * 9 ) / 5 ) + 32

celsius = float(input("Digite sua temperatura em Celsius: "))
fahrenheit = celsiustofahren(celsius)
print(f"A temperatura em Fahrenheits é: {fahrenheit}")
