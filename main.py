import os

class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2= valor2

    def Somar(self):
        return self.valor1+self.valor2
    
    def Subtracao(self):
        return self.valor1-self.valor2

    def Multiplicao(self):
        return self.valor1*self.valor2

    def Divisao(self):
        return self.valor1*self.valor2


def menu():
    print("""
======= CALCULADORA BÁSICA ========
| 1 - Somar                       | 
| 2 - Subtração                   | 
| 3 - Multiplicação               |
| 4 - Divisão                     |
| 5 - Sair                        |
___________________________________         
""")
    
while True:
    menu()
    opcao = int(input("Digite a opcão que deseja efetuar: "))

    if opcao == 1:
        os.system("cls")
        
        v1 = float(input("Digite o valor 1: "))
        v2 = float(input("Digite o valor 2: "))

        calcular = Calculadora(v1, v2)

        resultado = calcular.Somar()

        print(f"\nO resultado da soma é: {resultado}")

    elif opcao ==2:
        os.system("cls")
        
        v1 = float(input("Digite o valor 1: "))
        v2 = float(input("Digite o valor 2: "))

        calcular = Calculadora(v1, v2)

        resultado = calcular.Subtracao()

        print(f"\nO resultado da Subtração é: {resultado}")

    elif opcao == 3:
        os.system("cls")
        
        v1 = float(input("Digite o valor 1: "))
        v2 = float(input("Digite o valor 2: "))

        calcular = Calculadora(v1, v2)

        resultado = calcular.Multiplicao()

        print(f"\nO resultado da Multiplicação é: {resultado}")

    elif opcao == 4:
        os.system("cls")
        
        v1 = float(input("Digite o valor 1: "))
        v2 = float(input("Digite o valor 2: "))
        calcular = Calculadora(v1, v2)
        resultado = calcular.Divisao()
        print(f"\nO resultado da Divisão é: {resultado}")
    
    elif opcao == 5:
        break

    else:
        print("\nOpção digitada é inválida!, Por favor digite a operação adequada") 

