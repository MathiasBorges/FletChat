#Título talking
#Botão = iniciar o chat
#Popup
    #Welcome
    #Seu nome
    #Entrar no chat
#Chat
    #Seu nome entrou no chat
    #Mensagens do user
#Campo enviar mensagem
#Botão =enviar

import flet as ft

def main(pagina):
    texto=ft.Text('Talking')
    campo_nome=ft.TextField(label='Insira seu nome')
    chat_container=ft.Column()

    def enviar_mensagem_real_time(info):
        chat_container.controls.append(ft.Text(info))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_real_time) 

    def close_popUp(e):
        popUpName.open=False
    
    def enviarMensagem(e):
        texto_campo_mensagem=f"{campo_nome.value}: {campo_mensagem.value}"
        
        pagina.pubsub.send_all(texto_campo_mensagem)

        campo_mensagem.value=""
        pagina.update()

    campo_mensagem=ft.TextField(label="Escreva a mensagem aqui ✔️",on_submit=enviarMensagem)
    botao_enviar=ft.ElevatedButton("Enviar",on_click=enviarMensagem)
    
    pagina.add(chat_container)
    container_mensagem=ft.Row([campo_mensagem,botao_enviar])

    def entrar_chat(e):

        if not campo_nome.value or campo_nome.value=="":
            popUp.open=False
            popUpName.open=True
        else:
            popUp.open=False
            pagina.remove(botao)
            print("Chat iniciado")
            print(campo_nome.value)
            pagina.add(container_mensagem)
            pagina.update()

    popUp=ft.AlertDialog(
        open=False, modal=True,title=ft.Text("Bem-vindo!"),
        content=ft.Column([campo_nome],tight=True), actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    popUpName=ft.AlertDialog(
        open=False, modal=True,title=ft.Text("O campo não pode ser vazio"),actions=[ft.ElevatedButton("Entrar", on_click=close_popUp)])
    
    def comecar_chat(e):
        pagina.dialog=popUp
        popUp.open=True
        pagina.update()

    botao=ft.ElevatedButton('Entrar no chat', on_click=comecar_chat,bgcolor='#fafafa')

    pagina.add(texto)
    pagina.add(botao)

ft.app(main)

