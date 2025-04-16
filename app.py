from flet import *
import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///projectCadProduct.db'
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    """page é a variável que representa a página do aplicativo
    #Você pode adicionar widgets e definir propriedades aqui
    # ft.Page é uma classe que representa uma página em um aplicativo Flet"""
    
    lista_produtos = ft.ListView()

    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=float(preco.value)) 
            session.add(novo_produto)  # Adiciona o novo produto à sessão
            session.commit()  # Salva as alterações no banco de dados
            lista_produtos.controls.append(
                ft.Container(
                        ft.Text(produto.value),
                        bgcolor=ft.colors.BLACK12,
                        padding=10,
                        margin=3,
                        border_radius=10,
                        width=100,
                        alignment=ft.alignment.center
                    )
            )
            txt_erro.visible = False  # Torna o texto de erro invisível
            txt_salvo.visible = True  # Torna o texto de sucesso visível
            txt_salvo.update()  # Atualiza o texto de sucesso
            produto.value = ""  # Limpa o campo de texto do produto
            preco.value = ""
        except:
            txt_erro.visible = True
            txt_salvo.visible = False  # Torna o texto de sucesso invisível
        page.update()
        print("Produto cadastrado!")

    

    txt_erro = ft.Container(ft.Text("Erro ao cadastrar produto!"), visible=False, bgcolor=ft.colors.RED, padding=10, border_radius=10) # Mensagem de erro ao cadastrar produto
    txt_salvo = ft.Container(ft.Text("Produto Cadastrado!"), visible=False, bgcolor=ft.colors.GREEN, padding=10, border_radius=10) # Mensagem de erro ao cadastrar produto
    
    txt_titulo = ft.Text('Título do produto:', size=20, weight='bold') # Campo de texto para título do produto
    produto = ft.TextField(label='Digite o nome do produto..', width=300) # TextField para o usuário inserir o nome do produto
    txt_preco = ft.Text('Preço do produto:', size=20, weight='bold') # Campo de texto para preço do produto
    preco = ft.TextField(value="0",label='Digite o preço do produto..', width=300) # TextField para o usuário inserir o preço do produto
    btn_produto = ft.ElevatedButton(text='Cadastrar', icon=ft.icons.ADD, width=200, height=50, on_click=cadastrar) # Botão para cadastro do produto
    page.add(
        txt_erro,
        txt_salvo,
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto,
    )

    for p in session.query(Produto).all():
        lista_produtos.controls.append(
                ft.Container(
                    ft.Text(p.titulo),
                    bgcolor=ft.colors.BLACK12,
                    padding=10,
                    margin=3,
                    border_radius=10,
                    width=100,
                    alignment=ft.alignment.center
                )
            )  # Exibe os produtos cadastrados no console
        page.add(lista_produtos)


ft.app(target=main)