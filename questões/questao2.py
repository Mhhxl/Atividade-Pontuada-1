import os 
os.system('clear')

#entrada 
nome=input("Digite seu nome: ")
genero=input("""Digite seu Gênero:
             F para Feminino
             M para Masculino
 """)
estado_civil=input("""Digite seu estado civil: 
                   S para Solteiro(a)
                   C para Casado(a)
""")

 
#processamento
match genero:
    case "F" | "f":
        print("Feminino")
    case "M" | "m":
        print("Masculino")
    case _:
        print("Gênero inválido")


match estado_civil:
    case "C"| "c":
        print("Casado(a)")
    case "S" | "s":
        print("Solteiro(a)")
    case _:
        print("Não identificado")

if genero == "F" | "f" and estado_civil == "C" | "c" :
    anos_de_casamento=input("a quantos anos vc é casada?")
  #saida
print(f"Seu gênero: {genero}\n")
print(f"Seu estado civil é: {estado_civil}\n")
print(f"Vc está casada a: {anos_de_casamento}\n")
print("==FIM==")

#rapaz tem alguma coisa q eu n consegui fazer direito, pq n é possivel
  
