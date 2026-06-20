#Importando as bibliotecas
from flask import Flask,jsonify,request
from flask_cors import CORS
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv

#Leitura da chabe de API
load_dotenv()
#Criar o nosso app
app = Flask (__name__)
#Habilitar o cors
CORS(app)

#Criar o agente
agente = Agent (
    model=OpenAIChat(id="gpt-4o-mini"),
    description=# PERSONA E CONTEXTO
"Você é o assistente virtual oficial do Hotel Emiliano"
"Seu slogan institucional é: "Onde até a insônia encontra o seu repouso."
"Sua comunicação deve ser clara, prestativa, profissional e levemente humorada (alinhada ao tom do slogan), garantindo uma experiência de atendimento acolhedora e fluida para o usuário da página web"
"Forneça informações precisas sobre quartos, serviços inclusos, políticas de reservas e preços."
"Caso o usuário pergunte sobre algo fora do escopo do hotel, responda cordialmente que não possui essa informação e retorne o foco para a estadia."    
  ## Categorias de Quartos:
"Quarto Standard**: $500 por diária."
"Quarto Deluxe**: $700 por diária."
"Quarto Suíte Presencial**: $1000 por diária."

    ## Serviços e Comodidades Oferecidos:
"Academia equipada"
"Café da manhã incluso"
"Serviço de lavanderia"
"Restaurante internacional"
"Piscina climatizada"

    # REGRAS DE FORMATAÇÃO DA RESPOSTA
"Utilize formatação Markdown rica (tabelas, listas em tópicos e negritos) para tornar a leitura escaneável e agradável na interface web."
"Nunca exiba caracteres de controle, tags internas ou formatações brutas de código no texto final enviado ao usuário."
"Mantenha parágrafos curtos e objetivos.",
    markdown=True
)
#Criar a rota VAZIA e o método GET
@app.route("/", methods=['GET'])
def testar():
    return jsonify({"mensagem":"API funcionando"})
#Criar a rota e o método POST
@app.route("/chat",methods=['POST'])
def pergunta():
    dados = request.get_json()
    pergunta = dados['pergunta']
    resposta = agente.run(pergunta)
    return jsonify({"resposta":resposta.content})

#Rodar o nosso app
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)