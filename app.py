from flask import Flask, jsonify, request

# Using __name__ we give a unique name to our Flask app
app = Flask(__name__)

payers = []


@app.route('/payer', methods=['GET'])
def get_payers():
    return jsonify(payers)


@app.route('/payer/<int:payer_id>', methods=['GET'])
def validate_payer(payer_id):
    for payer in payers:
        if payer['payer_id'] == payer_id:
            return jsonify(payer)
        else:
            return f'Payer {payer_id} not found'


@app.route('/payer', methods=['POST'])
def add_payer():
    payers.append(request.get_json())
    return f'Payer added {request.get_json()}'


@app.route('/payer', methods=['DELETE'])
def remove_payer():
    payer_id = request.get_json()['payer_id']
    for payer in payers:
        if payer['payer_id'] == payer_id:
            payers.remove(payer)
            return f'Payer {payer_id} removed'
        else:
            return f'Payer {payer_id} not found'


app.run(port=5000)
