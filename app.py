from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modulos_windows')
def modulos_windows():
    return render_template('modulos_windows.html')

@app.route('/modulos_linux')
def modulos_linux():
    return render_template('modulos_linux.html')

@app.route('/modulos_janelas')
def modulos_janelas():
    return render_template('modulos_janelas.html')

if __name__ == "__main__":
    app.run(debug=True)
