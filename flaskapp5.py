from flask import jsonify

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
	return jsonify(cliente= username,
                   idade= idade)
	
	#return(str(idade))

@app.route('/compra/<nomecliente>/<produto>/<quantidade>')
def salvarCompra(nomecliente, produto, quantidade):
	#return(nomecliente)
	#return('nomecliente')

	idade=0
	with open('clientes.txt') as f:
		for line in f: 
			l=line.split(';')
			if (l[0] == nomecliente):
				idade=l[1]

	file = open('compras.txt', 'a+')
	file.write(nomecliente + ';'+ produto+ ';'+ quantidade+ ';'+ idade + '\n')
	file.close()

	return(nomecliente)