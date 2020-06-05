from flask import jsonify

import json

from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>/<idade>')
def adduser(username,idade):

	file = open('clientes.txt', 'a+')
	file.write(username + ';'+ idade + '\n')
	file.close()
	return username + " " + idade

@app.route('/busca/<username>')
def searchuser(username):
	idade=0
	with open('clientes.txt') as f:
		for line in f: 
			l=line.split(';')
			if (l[0] == username):
				idade=l[1]	
	return jsonify(cliente= username, idade= idade)


@app.route('/compra/<nomecliente>/<produto>/<quantidade>')
def salvarCompra(nomecliente, produto, quantidade):

	contents = urllib.request.urlopen("http://127.0.0.1:5000/busca/"+ nomecliente).read()
	cliente_idade = json.loads(contents)
	
	#print(cliente_idade['cliente'])
	#print(cliente_idade['idade'])

	idade=cliente_idade['idade']
	with open('clientes.txt') as f:
		for line in f: 
			l=line.split(';')
			if (l[0] == nomecliente):
				idade=l[1]

	file = open('compras.txt', 'a+')
	file.write(nomecliente + ';'+ produto+ ';'+ quantidade+ ';'+ idade + '\n')
	file.close()

	return(nomecliente)