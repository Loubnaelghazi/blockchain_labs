import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, difficulty):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self):
        target = "0" * self.difficulty  #bch ibda b 0
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block(difficulty)]  
        self.difficulty = difficulty  

    def create_genesis_block(self, difficulty):
        return Block(0, "0", "Genesis Block", difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, new_data, self.difficulty)
        print(f"Mining block {new_block.index} avec la difficulte {self.difficulty}...")
        start_time = time.time()
        new_block.mine_block()
        end_time = time.time()
        self.chain.append(new_block)
        print(f"Block {new_block.index} mined: {new_block.hash}")
        print(f"Le temps ecoule : {end_time - start_time:.2f} secondes\n")

for difficulty in range(1, 5):  # Difficulte croissante : exp
    blockchain = Blockchain(difficulty)
    blockchain.add_block(f"Block data pour la difficulte : {difficulty}")
