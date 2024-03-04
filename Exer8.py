def pagamento():
    
    h= float(input('Digite sua hora paga: '))
    H= float(input('Digite quantas horas trabalhou: '))
    hH = H*h
    print(F'R${hH} serão depositados na sua conta ')

pagamento()
