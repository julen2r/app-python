from flask import Flask, render_template, request

app = Flask(__name__)

def convertir_euros_a_pesos(euros, tasa_cambio):
    pesos_colombianos = euros * tasa_cambio
    return pesos_colombianos

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            euros_input = float(request.form['euros'])
            tasa_cambio_actual = 4300.0  # Puedes ajustar esto según tus necesidades
            pesos_resultantes = convertir_euros_a_pesos(euros_input, tasa_cambio_actual)
            return render_template('index.html', resultado=f"{euros_input} euros son {pesos_resultantes:.2f} pesos colombianos.")
        except ValueError:
            return render_template('index.html', error="Por favor, ingrese valores numéricos.")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
