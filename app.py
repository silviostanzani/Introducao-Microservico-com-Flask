# funcoes de manipulação de dados

def salvarcliente(nome,idade):
	file = open('clientes.txt', 'a+')
	file.write(nome+ ';'+ idade + '\n')
	file.close()

def buscarcliente(nome):
	idade=0
	with open('clientes.txt') as f:
		for line in f: 
			l=line.split(';')
			if (l[0] == nome):
				idade=l[1]
	return(idade)

# funcoes de interação com usuario
def cadastrarCliente():
	nome = input("Digite o nome ")
	idade = input("Digite a idade ")
	salvarcliente(nome,idade)

def buscarCliente():
	nome = input("Digite o nome do cliente que deseja buscar: ")
	idade = buscarcliente(nome)
	print('idade ', idade)

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
