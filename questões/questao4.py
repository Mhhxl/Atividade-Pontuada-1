import os
os.system('clear')

valor_total = 0
desconto = valor_total * 0.10
fruta=input("""Digite a fruta desejada: 
            1 para Morango
            2 para Maçã
            """)
if fruta == "1":
    fruta = "Morango"
    peso = float(input("Digite o peso desejado (em kg): "))
    if peso <= 5:
        valor_por_kg = 2.50
    else:
        valor_por_kg = 2.20
elif fruta == "2":
    fruta = "Maçã"
    peso = float(input("Digite o peso desejado (em kg): "))
    if peso <= 5:
        valor_por_kg = 1.80
    else:
        valor_por_kg = 1.50
else:
    print("Fruta inválida")
    exit()


if peso > 10 or valor_total > 15:
    print(f"Desconto: R${desconto:.2f}")
else:
    print("Sem desconto")

                 

valor_total = peso * valor_por_kg
if peso > 10 or valor_total > 15:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto

print(f"Fruta: {fruta}")
print(f"Peso: {peso}kg")
print(f"Valor total: R${valor_total:.2f}")

#anotações:
#treinar essa questão em casa, tive muita dificuldade e ainda assim teve alguma coisa errada.