from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def get_bot_response(user_message):
    user_message = user_message.lower()

    if "hello" in user_message:
        return "Hi! How can I help you?"
    elif "how are you" in user_message:
        return "I'm just a bot, but I'm doing great!"
    elif "name" in user_message:
        return "I'm your simple chatbot backend."
    elif "bye" in user_message:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    response = get_bot_response(message)

    return jsonify({
        "user_message": message,
        "bot_response": response
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)