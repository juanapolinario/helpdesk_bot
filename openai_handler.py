from openai import OpenAI

# Configurações da OpenAI
API_KEY = "KEY"
client = OpenAI(api_key=API_KEY)

class Openai:
    # Função para enviar mensagem para a OpenAI e obter a resposta
    def send_message_to_openai( message, history ):

        with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()


        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=100,
            temperature=0.1,
            messages=[
                {"role": "system","content": f"Você é um otaku que ama animes e irá indicar amigos para quem conversar com você.  use essas inforações para responder o usuário: {conteudo}. historico de conversa {history}"},
                {"role": "user", "content": message},
            ],
        )
        print(f"resposta : {response.choices[0].message.content} ")
        return  response.choices[0].message.content




