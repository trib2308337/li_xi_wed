from flask import Flask, render_template
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    money = random.randint(10000, 100000)
    return render_template("index.html", money=money)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
