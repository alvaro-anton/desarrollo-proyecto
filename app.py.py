from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/monofasica')
def monofasica():
    return render_template('monofasica.html')

@app.route('/trifasica')
def trifasica():
    return render_template('trifasica.html')

@app.route('/trifasica_neutro')
def trifasica_neutro():
    return render_template('trifasica_neutro.html')

@app.route('/corriente_continua')
def corriente_continua():
    return render_template('corriente_continua.html')

if __name__ == '__main__':
    app.run(debug=True)
