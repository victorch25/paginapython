from flask import Flask, render_template

app = Flask(__name__)
'''
@app.route('/')
def principal():
    return "BIENVENIDOS A MI PAGINA DE PYTHON"

@app.route('/contacto')
def contacto():
  return "BIENVENIDOS A CONTACTOS"
'''
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/lenguajes')
def mostrarlenguajes():
    misLenguajes = ("PHP", "Python", "Java", "C#",
                    "JavaScript", "Perl", "Ruby", "Rust")
    return render_template('lenguajes.html',lenguajes=misLenguajes)   

@app.route('/temperatura')
def temperatura():
    return render_template('temperatura.html')

if __name__ == '__main__':
    app.run(debug=True, port=5025)
