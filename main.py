from flask import Flask, request, send_from_directory
from quetion import dict_bot
import os

app = Flask(__name__)

@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("question", "")
    answer = dict_bot(question)
    return answer  # Ensure the answer is returned as plain text

@app.route("/")
def index():
    # Main.htmlを返す
    return send_from_directory(os.path.dirname(__file__), "Main.html")

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), 'css'), filename)

# 実行例
def main():
    print("Web server running at http://127.0.0.1:5000")
    app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    main()
