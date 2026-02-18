from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    prizes = [10000, 20000]  # chỉ 2 bao
    random.shuffle(prizes)
    app.config["CURRENT_PRIZES"] = prizes
    return render_template("index.html")

@app.route("/open/<int:index>")
def open_lixi(index):
    prizes = app.config.get("CURRENT_PRIZES", [20000, 50000])
    return jsonify({"prize": prizes[index]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
