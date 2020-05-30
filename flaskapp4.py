from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>/<idade>')
def adduser(username,idade):

	file = open('clientes.txt', 'a+')
	file.write(username + ';'+ idade + '\n')
	file.close()
	return username + " " + idade

@app.route('/user/<username>')
def searchuser(username):
	idade=0
	with open('clientes.txt') as f:
		for line in f: 
			l=line.split(';')
			if (l[0] == username):
				idade=l[1]
	return(str(idade))
