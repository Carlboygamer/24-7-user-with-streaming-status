from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Made by カズマ斉藤#4179and enjoy the 24/7 user with streaming"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
