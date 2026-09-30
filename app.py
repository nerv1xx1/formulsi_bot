import os
import threading
from flask import Flask

# Импортируем код твоего бота
import bot

app = Flask(__name__)

@app.route('/')
def index():
    return "Бот работает!"

@app.route('/health')
def health():
    return "OK"

def run_bot():
    # Запускаем бота из твоего файла bot.py
    # (или через exec, если там просто код)
    pass

if __name__ == "__main__":
    # Запускаем бота в фоновом потоке
    thread = threading.Thread(target=run_bot)
    thread.daemon = True
    thread.start()
    
    # Запускаем веб-сервер, чтобы Render видел, что бот работает
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
