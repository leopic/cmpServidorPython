from flask import Flask
from flask import jsonify
import random

app = Flask(__name__)

marcas = ['Volkswagen', 'Nissan', 'Toyota', 'Honda', 'Hyundai', 'Lexus', 'Mitsubishi']
modelos = ['Crossfox', 'Tida', 'Corolla', 'Accord', 'Accent', 'Yaris', 'Beetle', 'Amarok', 'Lancer']
carros = []


def fake_db():
    for marca in marcas:
        carros.append({
            'id': len(carros) + 1,
            'modelo': modelos[random.randrange(0, len(modelos))],
            'marca': marca
        })

for _ in range(5):
    fake_db()


@app.route('/api/carros')
def lista():
    app.logger.debug('[P] lista')
    return jsonify({'carros': carros})


@app.route('/api/carros/<int:carro_id>')
def detalle(carro_id):
    app.logger.debug('[P] detalle')
    for carro in carros:
        if carro['id'] == carro_id:
            return jsonify(carro)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3001, debug=True)
