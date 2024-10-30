import hashlib
import time
import random


#on va integrer le code de pow deja implemente avec l algorithme de pos pour comparer entrer les deux :


#pow

class PoWBlock:
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
        target = "0" * self.difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain pour PoW
class PoWBlockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block(difficulty)]  
        self.difficulty = difficulty  

    def create_genesis_block(self, difficulty):
        return PoWBlock(0, "0", "Genesis Block", difficulty)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_block = PoWBlock(len(self.chain), previous_block.hash, new_data, self.difficulty)
        print(f"\nMining PoW block {new_block.index} avec la difficulté {self.difficulty}...")
        
        start_time = time.time()
        new_block.mine_block()
        end_time = time.time()
        
        self.chain.append(new_block)
        execution_time = end_time - start_time
        print(f"PoW Block {new_block.index} mined: {new_block.hash}")
        print(f"Temps d'exécution (PoW) : {execution_time:.2f} secondes")
        return execution_time

#  PoS
class PoSBlock:
    def __init__(self, index, transactions, previous_hash, validator, difficulty):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.validator = validator
        self.difficulty = difficulty
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = f"{self.index}{self.transactions}{self.previous_hash}{self.validator}".encode()
        return hashlib.sha256(hash_data).hexdigest()

# Blockchain pour PoS
class PoSBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.validators = {}

    def create_genesis_block(self):
        
        return PoSBlock(0, "Genesis Block", "0", "Network", 1)

    def add_validator(self, name, stake):
        self.validators[name] = stake

    def select_validator(self):
        total_stake = sum(self.validators.values())
        choice = random.uniform(0, total_stake)
        cumulative = 0

        
        time.sleep(0.01)  # 10ms pour simuler une vérification de transactions

        for validator, stake in self.validators.items():
            cumulative += stake
            if cumulative >= choice:
                return validator
        return None

    def add_block(self, transactions):
        start_time = time.time()
        
        validator = self.select_validator()
        previous_hash = self.chain[-1].hash
        new_block = PoSBlock(len(self.chain), transactions, previous_hash, validator, 1)
        
        end_time = time.time()
        execution_time = end_time - start_time

        # Append the block
        self.chain.append(new_block)
        print(f"PoS Block {new_block.index} added by validator '{validator}'")
        print(f"Temps d'exécution (PoS) : {execution_time:.4f} secondes")
        return execution_time

# Comparaison entre PoW et PoS
if __name__ == "__main__":
    

    pow_difficulty = 4
    pow_blockchain = PoWBlockchain(pow_difficulty)
    pow_execution_time = pow_blockchain.add_block("Transaction data for PoW")

    # Comparaison PoS
    pos_blockchain = PoSBlockchain()
    pos_blockchain.add_validator("Lubna", 100)
    pos_blockchain.add_validator("hhhh", 50)
    pos_blockchain.add_validator("luna", 150)
    pos_execution_time = pos_blockchain.add_block("Transaction data for PoS")

 