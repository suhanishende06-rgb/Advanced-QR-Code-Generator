from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr = None
    
    if request.method == "POST":
        data = request.form.get("data")

        if data:
            img = qrcode.make(data)
            img.save("static/qrcode.png")
            qr = "static/qrcode.png"

    return render_template("index.html", qr=qr)

if __name__ == "__main__":
    app.run(debug=True)
