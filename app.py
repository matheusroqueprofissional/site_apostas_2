from flask import Flask,render_template,request, redirect, url_for, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("/inicio.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/registro")
def registro():
    return render_template("/registro.html")
@app.route("/recuperar")
def recuperar():
    return render_template("/recuperar.html")





if __name__ == '__main__':
    app.run(debug=True)