from bottle import Bottle, run

app = Bottle()

msg = '''
<center><h1>Minha página web</h1></center>
<p>Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.</p>
<center><a href="/curso_python">Clique aqui para acessa o curso</a></center>
'''

@app.route('/')
def index():
    return msg

@app.route('/curso_python')
def curso():
    return '<center><h1>Bem vindo(a) ao Curso de Python</h1></center>\
            <center><a href="/">Voltar a página principal</a></center>'

run(app, host='localhost', port=8080)