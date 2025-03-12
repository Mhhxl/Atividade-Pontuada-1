import os
os.system('clear')

#entrada
renda_mensal= float(input("Digite a sua renda mensal: "))
valor_do_emprestimo= float(input("Digite o valor do empréstimo: "))
parcelas= int(input("Digite a quantidade de parcelas: "))
#processamento
valor_max_emprestimo = renda_mensal * 10
valor_max_parcelas = renda_mensal * 0.3
valor_prestacao= valor_do_emprestimo / parcelas
if valor_do_emprestimo > valor_max_emprestimo:
    print("Empréstimo não concedido")
elif parcelas > valor_max_parcelas:
    print("Empréstimo não concedido")
elif valor_prestacao > renda_mensal * 0.3:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
    print(f"Valor da prestação: R${valor_prestacao:.2f}")
#saida
print("==FIM==")



#Anotaçoes:
#Revisar essa questão também, acho que falta alguma coisa