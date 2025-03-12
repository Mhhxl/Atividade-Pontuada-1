import os 
os.system('clear')

cor=input("""Digite o numero correspondente a cor: 
           1 para Verde
           2 para Azul
           3 para Amarelo
           4 para Vermelho
          
""")
#processamento

match cor:
    case "1":
        print("Verde=R$ 10,00")
    case "2":
        print("Azul=R$ 20,00")
    case "3":
        print("Amarelo=R$ 30,00")
    case "4":
        print("Vermelho=R $40,00")
    case _:
        print("Cor inválida")
#saida
print(f"Cor: {cor}")

print("==FIM==")
