from transformers import pipeline
# from transformers import Conversation


chatbot = pipeline(task="conversational", model="facebook/blenderbot-400M-distill")


chat_history = [
    {"role": "system", "content": "You are a helpful AI assistant."}, # Optional system message
    {"role": "user", "content": "Hey, can you tell me about the weather today?"}
]

response = chatbot(chat_history, max_new_tokens=50)

