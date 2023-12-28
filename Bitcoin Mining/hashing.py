from hashlib import sha256

MAX_NONCE = 10000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    
    prefix_str = "0" * prefix_zeros
    
    for nonce in range(MAX_NONCE):
        
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        
        if new_hash.startswith(prefix_str):
            print(f"Succesfully mined Bitcoins with nonce Value :  {nonce}")
            return new_hash
        
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

if __name__=='__main__':
    transactions = input("Enter Transactionns : ")
    difficulty = int(input("Enter difficulty level : "))
    
    import time
    start = time.time()
    print("Start mining")
    
    previous_hash = input("Enter previous hash value : ")
    new_hash = mine(5, transactions, previous_hash, difficulty)
    
    total_time = str((time.time() - start))
    print(f"end mining, Mining took : {total_time} seconds ")
    print(new_hash)
        