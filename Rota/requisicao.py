from cgitb import html
from flask import Blueprint, redirect, url_for, request
import dataset
import js2py

bp_requisicao = Blueprint('bp_requisicao1', __name__)

@bp_requisicao.route("/2/", methods=['GET','POST'])
def operacao_banco():
	if request.method == "POST":
		with dataset.connect("sqlite:///descricao.db") as db:
			# Como inserir dados [CREATE]
			titulo 	 = format(request.form["titulo"])
			pergunta = format(request.form["pergunta"])
			db['descricao'].insert(dict(titulo=titulo,pergunta=pergunta))

			return redirect(url_for("bp_requisicao1.listar_banco"))

@bp_requisicao.route("/banco/")
def listar_banco():
	with dataset.connect("sqlite:///descricao.db") as db:
		lista = db['descricao'].all()
        

	html = "<ul>"
	for item in lista:
		html += "<li>{id} - {titulo} - {pergunta}</li>".format(id=item['id'],titulo=item['titulo'],pergunta=item['pergunta'])
	html += "</ul>"

	return u"Estou no banco !<Br>Lista: <br>{} {}".format(html,lista), 200

#testando js2py
# js1 = '''import detectEthereumProvider from '@metamask/detect-provider';

# 		const provider = await detectEthereumProvider();

# 		if (provider) {
# 		// From now on, this should always be true:
# 		// provider === window.ethereum
# 		startApp(provider); // initialize your app
# 		} else {
# 		console.log('Please install MetaMask!');
# }'''

# res1 = js2py.eval_js(js1)

