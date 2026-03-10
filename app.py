from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.form["data"]

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        img.save("static/qrcode.png")

        return render_template("index.html", qr="static/qrcode.png")

    return render_template("index.html")

@app.route("/download")
def download():
    return send_file("static/qrcode.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
