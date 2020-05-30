# Microserviço com Flask

* Tutorial básico de microserviço usando framework Flask (https://palletsprojects.com/p/flask/)

* O framework Flask permite criar servidores web seguindo a especificaçáo WSGI (Web Server Gateway Interface), que é
um padrão para o desenvolvimento de aplicações web em Python, a idéia desse padrão é permitir a portabilidade de uma aplicação web em python entre diferentes servidores web atuando como um middleware.

* Flask provê recursos para: 
  * Iniciar um servidor web
  * Capturar as chamadas para diferentes funcionalidades de acordo com as URLs passadas
  * processas as requisições em um script python
   
* O Primeiro passo para desenvolvermos aplicações com Flask é instalar o framework
  * Em ambiente conda a instalação pode ser feita usando pip:
  
```
pip install flask
```

* Uma aplicação mínima em Flask precisa importar a class Flask e criar uma instância da classe flask:
  * Para isso vamos salvar o código a seguir em um arquivo chamado flaskapp.py
  
  ```
  from flask import Flask
  app = Flask(__name__)
  ```

* Para colocarmos essa aplicação no ar é necessário executar dois passos:
  * 1) Criar a variável de ambiente FLASK_APP e atribuir como valor o nome do arquivo criado (flaskapp)
  
  ```
  export FLASK_APP=flaskapp
  ```
  
  * 2) Executar o ambiente flask:
  
  ```
  flask run
  ```
  
* Ao executar esses passos será apresentada a tela a seguir:

```
(MicroServices) Spraces-MacBook-Pro:MicroServicesSamples silvio$ flask run
 * Serving Flask app "flaskapp"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 
* Isso indica que o servidor está no ar no local host e respondendo na porta TCP 5000. Por ser um servidor web, podemos realizar chamadas a ele por meio do navegador
  * Essa aplicação não captura nenhuma chamada URL, dessa forma, ao chamar a aplicação pelo browser o usuário receberá um mensagem de página não encontrada

* Para tratar requisições devemos incluir um controle chamado routing
  * O Routing define um formato de URL que deve ser capturado e direciona a chamada para uma função escrita em python
  
* O Código a seguir mostra como tratar requisições web:

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
``` 
  * O parâmetro @app.route() define qual URL será tratada pelo servidor. Nesse caso /
  * Ao capturar essa URL o servidor direcionará a chamada a função declarada na próxima linhas após o @app.route que é a função hello_world()
  * Essa função tem como objetivo retornar uma string com o valor "Hello, World!"
  * Esse retorno é direcionado como resposta ao cliente (Nesse caso um navegador) que realizou a chamada ao servidor web, portanto vai mostrar na tela do navegador a mensagem : "Hello, World!"
  
* Esse servidor atenderá requisições provenientes apenas do computador onde o servidor está sendo executado, pois o ip por padrão é configurado como 127.0.0.1, a porta padrão é a 5000.

* Tais parâmetros podem ser modificados para permitir que o servidor seja acessado a partir de outros nós da rede e em outras portas
  * para isso podemos usar os parâmetros -h e -p do comando flask
 
  ```
  flask run -h 0.0.0.0 -p 4000
  ```

  * Dessa forma, qualquer nó na mesma rede pode acessar o servidor pela porta 4000
  
  O Código a seguir mostra como capturar outras chamadas URL:
  
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'indice'

@app.route('/projetos/')
def projects():
    return 'pagina de projetos'

@app.route('/sobre')
def about():
    return 'Pagina sobre'

```

* Dessa forma se colocarmos no navegador: http://127.0.0.1:4000/sobre retornará a mensagem "Pagina sobre

* Para ver a página rodando dessa forma crie o arquivo flaskapp2.py com o código acima
* Em seguida execute
```
export FLASK_APP=flaskapp2
flask run -h 0.0.0.0 -p 4000
```

* As páginas apresentadas são estátiscas, ou seja, o conteúdo já está completamente preparado antes de iniciar as requisições, mas o flask permite também executarmos páginas dinâmicas, cujo conteúdo é criado de acordo com a URL passada

* O exemplo a seguir mostra como fazer uma requisição passando um nome e página retornada é uma mensagem que inclue o nome passado. Salve o código a seguir no arquivo: flaskapp3.py

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'indice'

@app.route('/projetos/')
def projects():
    return 'pagina de projetos'

@app.route('/sobre')
def about():
    return 'Pagina sobre'
    
@app.route('/user/<username>')
def profile(username):
    return username
```

* Em seguida execute
```
export FLASK_APP=flaskapp3
flask run -h 0.0.0.0 -p 4000
```

* faça uma requisicao ao seguinte endereço pelo navegador: http://127.0.0.1:4000/user/user1 e depois http://127.0.0.1:4000/user/user2

* Veja que o conteúdo da página se altera de acordo com o parâmetro passado após a palavra user, isso ocorre porque no roteamento utilizamos os símbolos <> e um nome de parâmetro, esse mesmo nome de parâmetro foi passado como parâmetro para a função python profile logo abaixo do parâmetro de roteamento

* Podemos também realizar chamadas a um microserviço por meio de uma aplicação python.
  * Para realizar uma requisição web vamos utilizar a biblioteca urllib.request (https://docs.python.org/3/library/urllib.request.html)
  * Essa biblioteca permite realizar requisições a servidores web em python 
  
  * insira o código a seguir em um script chamado cliente.py
  
```
import urllib.request

contents = urllib.request.urlopen("http://localhost:4000/user/user2").read()

print(type(contents))
print(contents)
```

* Execute o script em outro terminal (diferente do que está executando o microserviço)

```
python cliente.py
```

* O seguinte retorno será visto no terminal

```
<class 'bytes'>
b'user2'
```
* Uma aplicação de exemplo para cadastro e busca de cliente está disponível em app.py
* A mesma aplicação nos moldes de microserviço está disponível em app2.py e flaskapp4.py
