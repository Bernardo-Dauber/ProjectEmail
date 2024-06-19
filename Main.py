from Email import Email
from SystemEmail import System


sistema = System()

sistema.generateEmail("Anderson","Financeiro")
sistema.generateEmail("Bernardo","Development")

'''
def menu():

    print("Email System: ")
    print("1- Criar Email: ")
    print("2- Trocar Senha: ")
    print("3- Lista dos Email por Departamentos: ")
    choice = int(input("Selecione uma das opções"))

    while True:


        if choice == 1:
            print("Criar Email")

        elif choice == 2:
            print("Trocar Senha")

        elif choice == 3:
            print("Lista Email por Deparmentos")

        elif choice == 0:
            print("Saindo")
            break

        choice = int(input("Selecione uma das opções"))

        print("Email System: ")
        print("1- Criar Email: ")
        print("2- Trocar Senha: ")
        print("3- Lista dos Email por Departamentos: ")
'''

