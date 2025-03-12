import os
os.system ('clear')



#entrada 
valor_A=(input("Digite o valor de A: "))
valor_B=(input("Digite o valor de B: "))
valor_C=(input("Digite o valor de C: "))

#processamento
soma= valor_A + valor_B
#saida

if soma < valor_C:
    print("a soma de A e B é menor do que o valor C")
else:
    print("a soma de A e B é maior que o valor C")
