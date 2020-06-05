import urllib.request

import json

# funcoes de interação com usuario
def cadastrarCliente():
	nome = input("Digite o nome ")
	idade = input("Digite a idade ")
	contents = urllib.request.urlopen("http://127.0.0.1:5000/user/"+nome+"/"+idade).read()

def buscarCliente():
	nome = input("Digite o nome do cliente que deseja buscar: ")
	
	contents = urllib.request.urlopen("http://127.0.0.1:5000/busca/"+nome).read()

	print(contents)
	cliente_idade = json.loads(contents)
	print(cliente_idade['cliente'])
	print(cliente_idade['idade'])

def cadastrarCompra():
	nomecliente = input("Digite o nome do cliente ")
	produto = input("Digite o nome do produto ")
	quantidade = input("Digite a quantidade comprada ")
	str="http://127.0.0.1:5000/compra/"+ nomecliente +"/"+ produto +"/"+ quantidade
	print(str)
	contents = urllib.request.urlopen("http://192.168.1.109:5000/compra/"+ nomecliente +"/"+ produto +"/"+ quantidade).read()

	print(contents)
def menu():
	print('Opções:')
	print('1 cadastrar cliente')
	print('2 buscar cliente')
	print('3 cadastrar compra')
	print('4 sair')

	x=input('Escolha a opção:')
	x=int(x)
	return(x)

op=0

while (op != 4):
	if (op == 1):
		cadastrarCliente()
	if (op == 2):
		buscarCliente()
	if (op == 3):
		cadastrarCompra()

	op=menu()
