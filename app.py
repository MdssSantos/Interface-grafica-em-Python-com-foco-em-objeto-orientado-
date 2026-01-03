# . configuraçõ - aparenciaa
import customtkinter as ctk
#Criação de fucionalidades função
def validar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == "admin" and senha == "1234":
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")
#criação da janela principal
ctk.set_appearance_mode("dark")
#criação dos campos
app = ctk.CTk()
app.title('sitema de login')
app.geometry('400x300')
#criações das funções
#label
campo_usuario = ctk.CTkLabel(app,text="Usuario")
campo_usuario.pack(pady=100)
#entry
entrada_usuario = ctk.CTkEntry(app,placeholder_text="Digite seu usuario")
entrada_usuario.pack(pady=10)
#label
campo_senha = ctk.CTkLabel(app,text="Senha")
campo_senha.pack(pady=10)
#entry
entrada_senha = ctk.CTkEntry(app,placeholder_text="Digite sua senha")
entrada_senha.pack(pady=10)
#button
botao_login = ctk.CTkButton(app, text="Login", command=validar_login)
botao_login.pack(pady=10)
#iniciar a aplicação
app.mainloop()