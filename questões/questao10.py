import os
os .system('clear')

#entrada
combustivel=(input("""Digite qual o tipo de combustível:
            A para Álcool
            G para Gasolina
"""))
preco_litro_alcool= 3.79
preco_litro_gasolina= 6.59

#processamento
if combustivel == "A" or combustivel == "a":
    litros= float(input("Digite a quantidade de litros: "))
    if litros <= 25:
        desconto = 0.02 
    else:
        desconto = 0.05
    preco_litro_alcool -= preco_litro_alcool * desconto
    total = litros * preco_litro_alcool

if combustivel == "G" or combustivel == "g":
    litros= float(input("Digite a quantidade de litros: "))
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.06
    preco_litro_gasolina -= preco_litro_gasolina * desconto
    total = litros * preco_litro_gasolina

#saida
print(f"Combustível: {combustivel}")
print(f"Total: R${total:.2f}")
print("==FIM==")

#Anotações:
#meio complicadinha, revisar também