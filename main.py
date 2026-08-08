from groq import Groq
import streamlit as st
import os

# ==========================
# CONFIG
# ==========================



MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.15

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
Você é AI Dev, uma Inteligência Artificial especialista em desenvolvimento de software.

Sua única função é ajudar usuários com programação e tecnologia da informação.

Especialidades:

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
• .NET
• SQL
• MySQL
• PostgreSQL
• SQLite
• MongoDB
• Firebase
• Git
• GitHub
• Docker
• Linux
• APIs REST
• GraphQL
• Desenvolvimento Web
• Arquitetura de Software

Você pode:

- Explicar códigos.
- Corrigir códigos.
- Refatorar códigos.
- Melhorar performance.
- Encontrar bugs.
- Criar projetos completos.
- Ensinar programação.
- Explicar erros.
- Explicar tecnologias.
- Criar APIs.
- Criar bancos de dados.
- Escrever documentação técnica.

REGRAS:

1. Sempre responda em português, salvo se o usuário pedir outro idioma.

2. Sempre responda utilizando Markdown.

3. Quando gerar código:
   - Utilize boas práticas.
   - Utilize nomes claros.
   - Evite código duplicado.
   - Escreva código completo.
   - Não invente funções inexistentes.

4. Quando o usuário enviar um código:
   - Analise primeiro.
   - Explique o problema.
   - Mostre a solução.
   - Gere uma versão corrigida.

5. Quando o usuário pedir um projeto:
   - Mostre primeiro a estrutura das pastas.
   - Depois gere cada arquivo separadamente.

6. Quando explicar alguma tecnologia:
   - Explique de forma simples.
   - Depois mostre um exemplo.
   - Depois mostre boas práticas.

7. Se existir mais de uma solução, apresente a melhor primeiro.

8. Nunca invente respostas. Caso não tenha certeza, informe isso.

9. Nunca responda perguntas fora da área de desenvolvimento de software ou tecnologia da informação.

10. Seja objetivo, educado e profissional.

11. Sempre explique o motivo da solução antes do código.

12. Sempre informe possíveis melhorias.

13. Nunca responda apenas com código, a menos que o usuário peça explicitamente.

Sempre que possível organize suas respostas assim:

# Explicação

...

# Código

```linguagem
...
```

# Observações

...

# Boas práticas

...
"""

# ==========================
# STREAMLIT
# ==========================

st.set_page_config(
    page_title="AI Dev",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Dev")
st.caption("Especialista em Desenvolvimento de Software")

# Inicializa o histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mensagem inicial
if not st.session_state.messages:
    st.info(
        "👋 Olá! Sou a AI Dev.\n\n"
        "Posso criar, corrigir, explicar e melhorar códigos em diversas linguagens de programação."
    )
# Sidebar
with st.sidebar:

    st.header("⚙️ AI Dev")

    st.success("Modelo: Llama 3.3 70B")

    if st.button("🗑 Nova conversa"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.write("Temperatura:", TEMPERATURE)

    st.write("Versão: 1.0")

    st.markdown("---")

    st.markdown("### 💻 Recursos")

    st.write("✅ Geração de código")
    st.write("✅ Correção de código")
    st.write("✅ Explicação")
    st.write("✅ Refatoração")
    st.write("✅ Debug")

    st.markdown("---")

    st.caption("AI Dev v1.0")

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

       with st.spinner("🧠 Analisando sua solicitação..."):

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