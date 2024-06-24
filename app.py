from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Remote Rasa server URL
RASA_API_URL = 'http://128.140.58.181:5005/webhooks/rest/webhook'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/webhook", methods=['POST'])
def webhook():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': "No message received"}), 400

    print("User message:", user_message)

    # Send user message to the bot and get the bot message
    try:
        rasa_response = requests.post(url=RASA_API_URL, json={"message": user_message})
        rasa_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Rasa: {e}")
        return jsonify({'response': "Error communicating with Rasa server"}), 500

    rasa_response_json = rasa_response.json()
    print("Rasa response:", rasa_response_json)

    bot_response = rasa_response_json[0].get('text', "Sorry, I didn't understand that.") if rasa_response_json else "Sorry, I didn't understand that."

    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
