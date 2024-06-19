class Email:

    def __init__(self,email_address:str, passwords :str, nome:str, department:str):
        self.email_address = email_address
        self.passwords = passwords
        self.nome = nome
        self.department = department

    def to_dict(self):
        return {
            'email_address': self.email_address,
            'password': self.passwords,
            'nome': self.nome,
            'department': self.department
        }





