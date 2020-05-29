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
 
 * Isso indica que o servidor está no ar no local host e respondendo na porta TCP 5000
 
