from Email import Email
import random
import string

class System:
    def random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        return password

    def generateEmail(self, nome:str, department:str):

        address = "{}@{}.com".format(nome.replace(" ", ""),department)
        password = self.random_password()
        email = Email(address,password,nome)

        self.armazenar_dados(email)

    def mudar_senha(self, email_address:str, password:str ):
        with open('listEmail.txt', 'r') as file_read:
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

        print("Senha Alterada")

    def armazenar_dados(self, email: Email = None, emails: list = None):

        mode = 'a' if email else 'w'
        with open('listEmail.txt', mode) as file_write:
            if email:
                file_write.writelines(f'Nome: {email.nome} | Email: {email.email_address} | Senhas: {email.passwords}')
            elif emails: #Por conta do mudar Senha
                for email in emails:
                    file_write.writelines(
                        f'Nome: {email.nome} | Email: {email.email_address} | Senhas: {email.passwords}')

    def lista_email(self):
        with open('listEmail.txt', 'r') as file_read:
            for line in  file_read:
                print(line)