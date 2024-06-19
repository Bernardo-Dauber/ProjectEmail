'''

           IDEIAS
            Pegar a lista de email e ir verificando qual departemento é (Comercial, Marketing,Financeiro, Dev)
            No hash o value seria o objeto email.
            A função iria servir de filtro para pegar apenas o departmento que eu gostaraia.
            Será util para a atualização da implementação de  trocar senha.
        '''





from Email import Email
from Data import Data
import json
import random
import string

class System:

    def __init__(self):

        self.data = {
            "Marketing": [],
            "Comercial": [],
            "Financeiro": [],
            "Development": [],
            "HumanResources": []
        }


    def random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        return password

    def generateEmail(self, nome:str, department):
        #Problema de salvamento senha
        address = "{}@VSO.{}.com".format(nome.replace(" ", ""),department)
        password = self.random_password()
        email = Email(address,password,nome,department)# Funcionando

        self.armazenar_dados(email)

    def mudar_senha(self, departamento_atua:str,address:str ):
        self.data = Data().carregar()

        if departamento_atua in self.data:
            emails = self.data[departamento_atua]
            for email in emails:
                endereco_email = email['email_address']

                if endereco_email == address:
                    nova_senha = "1234567891011"
                    email['password'] = nova_senha


        d = Data()
        d.salvar(self.data)












        '''        with open('listEmail.txt', 'r') as file_read:
            emails = []
            for line in file_read:
                parts = line.strip().split(' |') #Funcionando
                if len(parts) == 3:
                    nome = parts[0].split(': ')[1]
                    email = parts[1].split(': ')[1]
                    senha = parts[2].split(': ')[1]
                    emails.append(Email(email, senha, nome))#Funcionando


        email_found = False
        for email in emails:
            if email.email_address == email_address:
                email.passwords = password
                email_found = True
                break

        if not email_found:
            print(f'Email {email_address} não encontrado.')
            return

        self.armazenar_dados(emails=emails)

        print("Senha Alterada")'''


    def armazenar_dados(self, email:Email):

        data_save = Data()
        if email.department == "Financeiro":
            self.data["Financeiro"].append(email)

        elif email.department == "Marketing":
            self.data["Marketing"].append(email)

        elif email.department == "Comercial":
            self.data["Comercial"].append(email)

        elif email.department == "Development":
            self.data["Development"].append(email)


        data_save.salvar(self.data)












    def lista_email(self):
        with open('listEmail.txt', 'r') as file_read:
            for line in  file_read:
                print(line)