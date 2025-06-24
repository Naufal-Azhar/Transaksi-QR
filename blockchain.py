import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, buyer, seller, amount):
        transaction = {
            'buyer': buyer,
            'seller': seller,
            'amount': amount,
            'timestamp': time()
        }
        self.current_transactions.append(transaction)
        tx_hash = self.hash(transaction)
        return tx_hash

    @staticmethod
    def hash(data):
        if isinstance(data, dict):
            data_string = json.dumps(data, sort_keys=True).encode()
        else:
            data_string = str(data).encode()
        return hashlib.sha256(data_string).hexdigest()
