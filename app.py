from flask import Flask, request, render_template, send_file, jsonify
from blockchain import Blockchain
from generate_qr import generate_qr
from datetime import datetime
import os

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr_web():
    buyer = request.form.get('buyer')
    seller = request.form.get('seller')
    amount = request.form.get('amount')

    if not buyer or not seller or not amount:
        return 'Missing required fields', 400

    tx_hash = blockchain.new_transaction(buyer, seller, amount)
    blockchain.new_block(proof=12345)
    qr_filename = generate_qr(tx_hash)
    return render_template('qr_result.html', transaction_hash=tx_hash, qr_filename=qr_filename)

@app.route('/qr/<filename>')
def get_qr(filename):
    return send_file(filename, mimetype='image/png')

@app.route('/verify')
def verify():
    return render_template('verify.html')

@app.route('/verify_hash', methods=['POST'])
def verify_hash():
    hash_to_verify = request.form.get('transaction_hash')
    found = False
    transaction_details = None

    for block in blockchain.chain:
        for transaction in block['transactions']:
            if blockchain.hash(transaction) == hash_to_verify:
                found = True
                transaction_details = transaction
                break
        if found:
            break

    if transaction_details:
        # Konversi timestamp UNIX ke datetime string
        timestamp = float(transaction_details['timestamp'])
        transaction_details['formatted_timestamp'] = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return render_template(
        'verify_result.html',
        hash_to_verify=hash_to_verify,
        found=found,
        transaction=transaction_details
    )


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True)
