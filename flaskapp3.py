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
