# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect
from Rota import requisicao

app = Flask("projeto") 
app.register_blueprint(requisicao.bp_requisicao)

@app.route("/")
def login():
    return render_template("login.html"), 200
    
@app.route("/1")
def form_descricao():
	return render_template("arquivo.html"), 200

if __name__ == "__main__":
    app.run(debug=True)