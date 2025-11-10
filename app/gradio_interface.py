import gradio as gr
from app.agent import initialize_agents

agents = initialize_agents()
history = [{"role": "system", "content": "SYSTEM_MESSAGE"}]  # inicializa con sistema


def chat_with_agent(user_input):
    global history
    history, image = agents["chat"](history)
    # history debe tener el formato adecuado:
    # [{"role": "user", "content": "..."} , {"role": "assistant", "content": "..."}]
    return history, history  # Devuelve la historia para actualizar el chatbot y su estado


# def chat_with_agent(user_input):
#     global history
#     # Añadir mensaje del usuario al historial antes de pasar a chat()
#     history.append({"role": "user", "content": user_input})
    
#     history, image = agents["chat"](history)
    
#     # Preparar para Gradio: crear lista de pares (usuario, asistente)
#     history_display = []
#     for i in range(1, len(history), 2):
#         user_msg = history[i]["content"] if i < len(history) else ""
#         assistant_msg = history[i+1]["content"] if (i+1) < len(history) else ""
#         history_display.append((user_msg, assistant_msg))
    
#     return history_display

def create_interface():
    with gr.Blocks() as app_interface:
        chatbot = gr.Chatbot(type="messages")
        txt = gr.Textbox(show_label=False, placeholder="Escribe tu mensaje...")

        txt.submit(chat_with_agent, inputs=txt, outputs=chatbot)

    return app_interface
