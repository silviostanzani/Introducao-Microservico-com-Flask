import urllib.request

# funcoes de interação com usuario
def cadastrarCliente():
	nome = input("Digite o nome ")
	idade = input("Digite a idade ")
	contents = urllib.request.urlopen("http://127.0.0.1:4000/user/"+nome+"/"+idade).read()

def buscarCliente():
	nome = input("Digite o nome do cliente que deseja buscar: ")
	
	contents = urllib.request.urlopen("http://127.0.0.1:4000/user/"+nome).read()

	print(contents)

	#idade = buscarcliente(nome)
	#print('idade ', idade)

def menu():
	print('Opções:')
	print('1 cadastrar cliente')
	print('2 buscar cliente')
	print('3 sair')

	x=input('Escolha a opção:')
	x=int(x)
	return(x)

op=0

while (op != 3):
	if (op == 1):
		cadastrarCliente()
	if (op == 2):
		buscarCliente()

	op=menu()
