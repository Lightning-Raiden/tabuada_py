def tabuada(numero):
    print(f"Tabuada do número: {numero}")
    for i in range(1 , 11):
        print(10* "-")
        print(f"{i} x {numero}: {i * numero}")

num = input("Digite o número inteiro da tabuada que deseja ver: ")
print("")

while True:
    try:
        num = int(num)
        break
    
    except ValueError:
        num = input("Valor inválido! Digite um número inteiro: ")

tabuada(num)