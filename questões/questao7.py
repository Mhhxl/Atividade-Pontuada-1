import os 
os.system('clear')

#entrada
produto= "Frango"
preco_unid= 4.5
quantidade=(int(input("Digite a quantidade de frango: ")))
total = preco_unid * quantidade

#processamento
if quantidade <= 5:
    desconto = 0.02
    total = total - (total * desconto)
elif quantidade >= 5 and quantidade <= 10:
    desconto = 0.03
    total = total - (total * desconto)
elif quantidade >10:
    desconto = 0.05
    total = total - (total * desconto)


#saida
print(f"Produto: {produto}")
print(f"Preço unitário: R${preco_unid:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R${total:.2f}")