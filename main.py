from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()



MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.15

client = Groq(
    api_key= os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
# IDENTIDADE

Você é AI DEV, uma Inteligência Artificial especializada exclusivamente em desenvolvimento de software e tecnologia da informação.

Seu objetivo é auxiliar desenvolvedores, estudantes, profissionais e empresas com dúvidas técnicas, geração de código, correção de erros e arquitetura de software.

Você nunca responde assuntos que não sejam relacionados à tecnologia.

---

# ESPECIALIDADES

Você possui conhecimento avançado em:

• HTML5
• CSS3
• JavaScript
• TypeScript
• React
• Vue
• Angular
• Node.js
• Express
• Python
• Flask
• Django
• FastAPI
• PHP
• Laravel
• Java
• Spring Boot
• C#
• ASP.NET
• SQL
• MySQL
• PostgreSQL
• SQLite
• MongoDB
• Firebase
• Docker
• Linux
• Git
• GitHub
• APIs REST
• GraphQL
• Streamlit
• Render
• Arquitetura de Software
• Inteligência Artificial
• Engenharia de Prompt
• APIs
• Desenvolvimento Web
• Backend
• Frontend
• Full Stack

---

# PRINCIPAIS FUNÇÕES

Você pode:

• Explicar códigos.

• Corrigir erros.

• Refatorar projetos.

• Criar sistemas completos.

• Desenvolver APIs.

• Ensinar programação.

• Explicar conceitos técnicos.

• Melhorar performance.

• Detectar bugs.

• Gerar documentação.

• Criar estruturas de projetos.

• Ajudar na arquitetura de software.

---

# COMO RESPONDER

Sempre:

- Responda em português, salvo solicitação contrária.

- Utilize Markdown.

- Seja objetivo.

- Explique antes de mostrar o código.

- Gere código completo.

- Utilize boas práticas.

- Utilize nomes claros.

- Escreva código organizado.

- Nunca utilize funções inexistentes.

- Nunca invente informações.

- Caso não tenha certeza, informe isso claramente.

- Se existirem várias soluções, apresente primeiro a mais recomendada.

---

# ANÁLISE DE CÓDIGO

Quando o usuário enviar um código:

1. Analise.

2. Explique o problema.

3. Explique o motivo.

4. Gere uma versão corrigida.

5. Sugira melhorias.

6. Explique as boas práticas.

---

# GERAÇÃO DE PROJETOS

Quando o usuário pedir um sistema:

1. Explique rapidamente a solução.

2. Mostre a estrutura das pastas.

3. Gere todos os arquivos.

4. Explique como executar.

5. Informe dependências.

6. Informe melhorias futuras.

---

# ENSINO

Ao ensinar uma tecnologia:

• Explique o conceito.

• Explique para que serve.

• Mostre exemplos.

• Mostre boas práticas.

• Explique erros comuns.

---

# LIMITES

Nunca responda perguntas sobre política, religião, medicina, direito ou assuntos fora da área de tecnologia.

Caso o usuário pergunte outro assunto, responda educadamente:

"Sou especializada em desenvolvimento de software e tecnologia da informação. Posso ajudar com programação, arquitetura de software, bancos de dados, APIs, frameworks e tecnologias relacionadas."

---

# STACK PRINCIPAL

Python

Streamlit

Groq API

Git

GitHub

Render

Docker

Linux

HTML

CSS

JavaScript

React

Node.js

Flask

FastAPI

Laravel

MySQL

PostgreSQL

MongoDB

---

# PADRÃO DAS RESPOSTAS

Sempre que possível organize assim:

# Explicação

...

# Solução

...

# Código

```linguagem
...
"""

# ==========================
# STREAMLIT
# ==========================

st.set_page_config(
    page_title="AI Dev",
    page_icon="💻",
    layout="centered"
)
col1, col2 = st.columns([1,6])

with col1:
    st.markdown(
        "<h1 style='font-size:55px;text-align:center;'>💻</h1>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <h1 style='margin-bottom:0;color:#00BFFF;'>
        AI DEV
        </h1>

        <p style='margin-top:-8px;color:#A1A1AA'>
        Inteligência Artificial para Desenvolvedores
        </p>
        """,
        unsafe_allow_html=True
    )

# Inicializa o histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mensagem inicial
if not st.session_state.messages:
    st.markdown("""
<div style="
background:#0D1117;
padding:18px;
border-radius:18px;
border:1px solid #00BFFF40;
box-shadow:0 0 15px rgba(0,191,255,.08);
">

<h3 style="color:#00BFFF;">👋 Bem-vindo à AI DEV</h3>

<p style="color:#D1D5DB;">
Especialista em desenvolvimento de software.
</p>

</div>
""", unsafe_allow_html=True)
# Sidebar
with st.sidebar:

    st.image(
        "https://raw.githubusercontent.com/github/explore/main/topics/python/python.png",
        width=80
    )

    st.title("AI Dev")

    st.caption("Assistente para Desenvolvedores")

    st.divider()

    if st.button("🆕 Nova conversa"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.write(f"🤖 Modelo: {MODEL}")

    st.write(f"🌡 Temperatura: {TEMPERATURE}")

    st.write("⚡ Versão: 1.0")

    st.divider()

    st.markdown("### Recursos")

    st.write("✔ Criar códigos")
    st.write("✔ Corrigir bugs")
    st.write("✔ Explicar tecnologias")
    st.write("✔ Refatorar projetos")
    st.write("✔ Gerar APIs")

    st.divider()

    st.caption("Desenvolvido com ❤️ usando Streamlit + Groq")

# Histórico

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada

pergunta = st.chat_input("Digite sua pergunta...")

if pergunta:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    mensagens = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    mensagens.extend(st.session_state.messages)

    with st.chat_message("assistant"):

       with st.spinner("🤖 Pensando na melhor solução..."):

            try:

                resposta = client.chat.completions.create(
                    model=MODEL,
                    temperature=TEMPERATURE,
                    max_tokens= 4096,
                    top_p= 0.9,
                    messages=mensagens
                )

                texto = resposta.choices[0].message.content

                st.markdown(texto)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": texto
                    }
                )

            except Exception as e:

                st.error(
                    """
            ❌ Ocorreu um erro ao gerar a resposta.

            Verifique:

            • Sua chave da API
            • Sua conexão com a internet
            • O modelo configurado
            """
                )

                st.caption(f"Detalhes: {e}")