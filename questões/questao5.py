import os
os.system('clear')

#entrada
valor_A=int(input("Digite o valor de A: "))
valor_B=int(input("Digite o valor de B: "))
operacao=input("""Digite a operação desejada:
                + para adição
                - para subtração
                * para multiplicação
                / para divisão
                """)
#processamento
match operacao:
    case "+":
        resultado= valor_A + valor_B
    case "-":
        resultado= valor_A - valor_B
    case "*":
        resultado= valor_A * valor_B
    case "/":
        resultado= valor_A / valor_B
    case _: 
        print("Operação inválida")
        resultado=0

#saida
print(f"O resultado da operação é: {resultado}")
print(f"o operador escolhido foi: ", {operacao})