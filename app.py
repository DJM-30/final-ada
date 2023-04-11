from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home-banking.html', saludo = persona1.saludo())

@app.route('/proceso')
def homeland():
    return render_template('proceso.html', saludo = persona1.saludo())

if __name__=='__main__':
    from persona import Persona
    persona1 = Persona(38655402, 'Debora Jael M')
    app.run(debug=True)