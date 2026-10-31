from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def read_root():
    return jsonify({"status": "Flask server is live and running!"})


@app.route("/interact", methods=["POST"])
def handle_interaction():
    data = request.json
    user_name = data.get("user_name", "Guest")
    message = data.get("message", "")

    return jsonify(
        {
            "status": "success",
            "greeting": f"Hello {user_name}!",
            "processed_message": f"Flask processed your message: '{message}'",
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
