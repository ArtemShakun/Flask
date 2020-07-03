from flask import Flask
from flask import request, jsonify
from flask_sslify import SSLify
from parse import get_date
import requests
import json

app = Flask(__name__)
sslify = SSLify(app)

URL = 'https://api.telegram.org/bot1....................dI/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def send_message(chat_id, text='bla-bla-bla'):
    # sendMessage два обязательных параметра chat_id и text
    url = URL + 'sendMessage'
    answer = {'chat_id':chat_id, 'text':text}
    r = requests.post(url, json=answer)
    return r.json()



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message'] ['text']

        if 'hi' in message:
            result = get_date()

            send_message(chat_id, text=result)

        return jsonify(r)
    return '<h1>Bot welcomes you</h1>'


if __name__ == '__main__':
    app.run(debug=True)
