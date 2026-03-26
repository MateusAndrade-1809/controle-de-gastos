from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

gastos = []

@app.route('/')
def index():
    total = sum(float(gasto['valor']) for gasto in gastos)
    return render_template('index.html', gastos=gastos, total=total)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    valor = request.form['valor']

    if nome and valor:
        gastos.append({
            'nome': nome,
            'valor': valor
        })

    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def excluir(id):
    if 0 <= id < len(gastos):
        gastos.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)