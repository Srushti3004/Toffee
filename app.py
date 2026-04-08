from flask import Flask, request, jsonify

app = Flask(__name__)

toffee_sales = []

@app.route('/sales', methods=['GET'])
def get_sales():
    return jsonify(toffee_sales)

@app.route('/sales', methods=['POST'])
def add_sale():
    sale = request.json
    toffee_sales.append(sale)
    return jsonify(sale), 201

@app.route('/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = request.json
    if sale_id < len(toffee_sales):
        toffee_sales[sale_id] = sale
        return jsonify(sale)
    return jsonify({'error': 'Sale not found'}), 404

@app.route('/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    if sale_id < len(toffee_sales):
        sale = toffee_sales.pop(sale_id)
        return jsonify(sale)
    return jsonify({'error': 'Sale not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)