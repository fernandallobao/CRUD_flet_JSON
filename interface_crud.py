import json
import flet as ft
from manipulador import * 

def main(page: ft.Page):
    manipulador = Manipulador()

    def criar_arquivo(e):
        nome_arquivo = nome_arquivo_input.value
        resultado = manipulador.criar_arquivo(nome_arquivo)
        resultado_text.value = resultado
        page.update()

    def abrir_arquivo(e):
        nome_arquivo = nome_arquivo_input.value
        dados = manipulador.abrir_arquivo(nome_arquivo)
        resultado_text.value = json.dumps(dados, indent=4)
        page.update()

    def cadastro_usuario(e):
       
        try:
            nome_arquivo = nome_arquivo_input.value
            usuarios = Manipulador.abrir_arquivo(nome_arquivo)
            p_codigo = len(usuarios)

            #cria os inputs
            p_nome = ft.TextField(label="Informe o nome:")
            p_cpf = ft.TextField(label="Informe o CPF:")
            p_email = ft.TextField(label="Informe o e-mail:")
            p_profissao = ft.TextField(label="Informe a profissão:")

            def salvar_usuario(e):
                usuario = {
                    "codigo": p_codigo,
                    "nome": p_nome.value,
                    "cpf": p_cpf.value,
                    "email": p_email.value,
                    "profissao": p_profissao.value
                }
                usuarios.append(usuario)
                print(f'Usuário salvo: {usuario}')
                # Aqui você pode adicionar a lógica para salvar os dados    no arquivo
                # print(m.salvar_dados(usuarios, abrir_arquivo))

            salvar_button = ft.ElevatedButton(text="Salvar",    on_click=salvar_usuario)

            page.add(p_nome, p_cpf, p_email, p_profissao, salvar_button)

        except Exception as e:
            print(f'Não foi possível realizar a operação. {e}.')

  
    def alterar_dados_usuario(e):
        try:
            nome_arquivo = nome_arquivo_input.value
            usuarios = manipulador.abrir_arquivo(abrir_arquivo)    

            codigo = int(codigo_input.value)
            
            if codigo < len(usuarios):
                for campo in ["nome", "cpf", "email", "profissao"]:
                    novo_dado = ft.TextField(label=f'Novo {campo}:', value=usuarios[codigo].get(campo))
                    page.add(novo_dado)

                    def salvar_alteracao(e):
                        usuarios[codigo][campo] = novo_dado.value
                        manipulador.salvar_dados(usuarios, nome_arquivo)
                        resultado_text.value = f"Dados do usuário {codigo} alterados."
                        page.update()

                    salvar_button = ft.ElevatedButton(text="Salvar Alteração", on_click=salvar_alteracao)
                    page.add(salvar_button)
            else:
                resultado_text.value = f"Usuário com código {codigo} não encontrado."
            page.update()
            
        
        except Exception as e:
            print('Não foi possível alterar os dados.')
        
        finally:
            pass

    def deletar_usuario(e):
        nome_arquivo = nome_arquivo_input.value
        codigo = int(codigo_input.value)
        resultado = manipulador.deletar_usuario(nome_arquivo, codigo)
        resultado_text.value = resultado
        page.update()



    nome_arquivo_input = ft.TextField(label="Nome do Arquivo")
    codigo_input = ft.TextField(label="Código do Usuário")
    resultado_text = ft.Text()
    

    page.add(
        nome_arquivo_input,
        ft.Row([
            ft.ElevatedButton("Criar Arquivo", on_click=criar_arquivo),
            ft.ElevatedButton("Abrir Arquivo", on_click=abrir_arquivo),
            ft.ElevatedButton("Criar usuario", on_click=abrir_arquivo),
            ft.ElevatedButton("Salvar Dados", on_click=cadastro_usuario),
            ft.ElevatedButton("Alterar Usuário", on_click=alterar_dados_usuario),
            ft.ElevatedButton("Deletar Usuário", on_click=deletar_usuario)
        ]),
        codigo_input,
        resultado_text
    )

ft.app(target=main)