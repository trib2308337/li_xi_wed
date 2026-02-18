from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"   # BẮT BUỘC để dùng session

@app.route("/")
def index():
    # Tạo mới mỗi lần reload trang
    prizes = [20000, 20000, 20000, 50000]
    random.shuffle(prizes)

    # Lưu vào session
    session["CURRENT_PRIZES"] = prizes

    return render_template("index.html")

@app.route("/open/<int:index>")
def open_lixi(index):
    prizes = session.get("CURRENT_PRIZES", [20000, 20000, 20000, 50000])

    # Kiểm tra index hợp lệ
    if 0 <= index < len(prizes):
        return jsonify({"prize": prizes[index]})
    else:
        return jsonify({"error": "Invalid index"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
