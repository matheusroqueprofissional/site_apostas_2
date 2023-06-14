from flask import Flask,render_template,request, redirect, url_for, jsonify
from flask_mail import Mail, Message


app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("/paginainicial.html")

@app.route("/jogos")
def jogo():
    return render_template("/paginajogo.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route("/registro")
def registro():
    return render_template("/registro.html")
@app.route("/recuperar")
def recuperar():
    return render_template("/recuperar.html")


import mysql.connector
conn = mysql.connector.connect(
host='localhost',
database='si',
user='root',
password=''
)


@app.route('/enviar',methods=['POST'])
def palpite_confirmado():
    valor = request.form['bt']
    import mysql.connector
    conn = mysql.connector.connect(
    host='localhost',
    database='si',
    user='root',
    password=''
    )
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO `palpite`(`username`, `palpite`) VALUES ('matheus roque','"+valor+"')")

    conn.commit()
    cursor.close()
    return redirect("/")




if __name__ == '__main__':
    app.run(debug=True)