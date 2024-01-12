import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(botao_iniciar)

        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )

        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        modal=True, 
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.TextButton("Entrar", on_click=entrar_chat)],
        actions_alignment=ft.MainAxisAlignment.END
    )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(chat)
    pagina.add(botao_iniciar)

# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)