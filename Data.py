import json
class Data:


    def salvar(self, data):
        dados_serializados = {}
        for chave, emails in data.items():
            if emails and hasattr(emails[0],
                                  'to_dict'):  # Verifica se há elementos e se o primeiro tem o método to_dict()
                lista_emails_serializados = [email.to_dict() for email in emails]
            else:
                lista_emails_serializados = emails  # Assume que os emails já são dicionários

            dados_serializados[chave] = lista_emails_serializados

        with open("Departamentos.json", 'w') as json_file:
            json.dump(dados_serializados, json_file, indent=4)


    def carregar(self):
        try:
            with open("Departamentos.json", 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return None

    '''
    def salvar_txt(self, hashTable):
        with open("teste.txt", 'w') as file:
            for chave, valor in hashTable.items():
                file.write(f"{chave}: {valor}\n")
    '''


    def salvar2(self,data):
        with open("Departamentos.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

            json_file.close()