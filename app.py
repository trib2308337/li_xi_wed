from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Tạo mới mỗi lần reload trang
    prizes = [20000, 20000, 20000, 50000]
    random.shuffle(prizes)

    # Lưu vào session tạm (hoặc biến global tạm thời)
    app.config["CURRENT_PRIZES"] = prizes

    return render_template("index.html")

@app.route("/open/<int:index>")
def open_lixi(index):
    prizes = app.config.get("CURRENT_PRIZES", [20000,20000,20000,50000])
    return jsonify({"prize": prizes[index]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
