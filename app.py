from flask import Flask, render_template

# Criar a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de módulos do Windows
@app.route('/modulos_windows')
def modulos_windows():
    return render_template('modulos_windows.html')

# Rota para a página de módulos do Linux
@app.route('/modulos_linux')
def modulos_linux():
    return render_template('modulos_linux.html')

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
