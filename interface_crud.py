import json
import flet as ft
from manipulador import Manipulador

def main(page: ft.Page):
    page.title = 'CRUD'
    page.scroll = 'adaptive'
    page.theme_mode = ft.ThemeMode.LIGHT

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

    def cadastrar_usuario(e):
        nome_arquivo = nome_arquivo_input.value
        usuarios = manipulador.abrir_arquivo(nome_arquivo)
        p_codigo = len(usuarios)

        usuario = {
            "codigo": p_codigo,
            "nome": p_nome.value,
            "cpf": p_cpf.value,
            "email": p_email.value,
            "profissao": p_profissao.value
        }
        usuarios.append(usuario)
        manipulador.salvar_dados(usuarios, nome_arquivo)
        resultado_text.value = f'Usuário {usuario["nome"]} cadastrado com sucesso!'
        
        # Limpar campos
        p_nome.value = ""
        p_cpf.value = ""
        p_email.value = ""
        p_profissao.value = ""
        
        page.update()

    def alterar_dados_usuario(e):
        try:
            nome_arquivo = nome_arquivo_input.value
            usuarios = manipulador.abrir_arquivo(nome_arquivo)    

            codigo = int(codigo_input.value)
            
            if codigo < len(usuarios):
                usuario = usuarios[codigo]
                
                # Exibir campos com valores atuais para edição
                for campo in ["nome", "cpf", "email", "profissao"]:
                    novo_dado = ft.TextField(label=f'Novo {campo}:', value=usuario.get(campo))
                    page.add(novo_dado)

                    def salvar_alteracao(e):
                        usuario[campo] = novo_dado.value
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
            resultado_text.value = "Erro ao alterar os dados."
        
        finally:
            page.update()

    def deletar_usuario(e):
        nome_arquivo = nome_arquivo_input.value
        codigo = int(codigo_input.value)
        resultado = manipulador.deletar_usuario(nome_arquivo, codigo)
        resultado_text.value = resultado
        page.update()

    nome_arquivo_input = ft.TextField(label="Nome do Arquivo")
    codigo_input = ft.TextField(label="Código do Usuário")
    resultado_text = ft.Text() # Utilize um Row para um melhor controle do layout
    p_nome = ft.TextField(label="Informe o nome:")
    p_cpf = ft.TextField(label="Informe o CPF:")
    p_email = ft.TextField(label="Informe o e-mail:")
    p_profissao = ft.TextField(label="Informe a profissão:")

    
    
    page.add(
        ft.Row([ft.Text('CRUD', size=50)],
                alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([nome_arquivo_input,
                ft.ElevatedButton("Abrir Arquivo", on_click=abrir_arquivo),
                ft.ElevatedButton("Criar Arquivo", on_click=criar_arquivo)]),
        ft.Row([p_nome, p_cpf, p_email, p_profissao]),
        ft.Row([ft.ElevatedButton("Cadastrar usuário", on_click=cadastrar_usuario)]),
        ft.Row([codigo_input]),
        ft.Row([ft.ElevatedButton("Alterar Usuário", on_click=alterar_dados_usuario),
                ft.ElevatedButton("Deletar Usuário", on_click=deletar_usuario)]),
        resultado_text
    )

ft.app(target=main)
