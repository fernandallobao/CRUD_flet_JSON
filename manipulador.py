#import biblioteca especifica para arquivos JSON
import json 

class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [
                {
                    'codigo:': 0,
                    'nome': 'Admin',
                    'cpf': '000.000.000-00',
                    'email': 'admin@gmail.com',
                    'profissao': 'Administrador'
                }
            ]
        
            #serializando objeto python como json. Pega o dicionario e conveter ele pro JSON, depois de convertido é possivel gravar ele JSON
            #gravação dos dados inicio
            json_dados = json.dumps(usuarios) # .dumps converte o objeto py para um objeto json
            #with open - abrir arquivo
            with open(f'{nome_arquivo}.json', 'w', encoding="utf-8") as f: #w=write escreve o arquivo / encoding = "utf-8" o formato da idioma que ele deve escrever os aquitvos
                f.write(json_dados)
            return f'{nome_arquivo}.json criado com sucesso.'
            #gravação dos dados fim

        except Exception as e:
            return f'Não foi possivel criar o arquivo. {e}.'
        
        
    def abrir_arquivo(self, nome_arquivo):
        #deserializando objeto json em py
        with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f: # r read para ler o arquivo
            dados = json.load(f)
        return dados

    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f) #dumps != dump, ele acrescenta dados
            return f'Dados gravados com sucesso'
        except Exception as e:
            return f'Não foi possivel salvar os dados. {e}.'
        
    def __del__(self):
        return 'Manipulador destruído!'
    
