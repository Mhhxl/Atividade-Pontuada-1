import os
os.system('clear')

#entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma=nota1+nota2
media=soma/2

#processamento
if media >= 6:
    print("PARABÉNS! VOCÊ FOI APROVADO")
elif media < 6 and media >= 4:
    print("Recuperação")
else:
    print("Reprovado")


#saida
print(f"A média do aluno é: {media}")

#anotações:
#ao que parece, utilizar o Match nessa situação iria ser mais demorado

