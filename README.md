# blockchain_labs

This repository contains my blockchain labs, supervised by Prof. Ikram BENADBELOUAHAB, where I explore the fundamentals of blockchain technology, including implementations of Proof of Work, blocks, chains, and more. The labs aim to provide practical insights into how blockchain systems operate, with varying hash difficulty levels and performance analysis."

Feel free to adjust it to better suit your style!

## Table of Contents

- [Lab 1: Cryptography and Blockchain Concepts](#cryptographie-and-blockchain-concepts)
- [Lab 2: Encryption/Decryption Algorithm Inspired by RSA](#Lab-2-encryptiondecryption-algorithm-inspired-by-rsa)

---
## Lab 1:
This workshop covers fundamental topics in cryptography and blockchain, including the implementation of a Merkle Tree and Proof of Work.

## Exercise 1: Merkle Tree

- **Objective**: Implement a basic Merkle Tree from scratch using C++.

---

## Exercise 2: Proof of Work

- **Objective**: Implement Proof of Work in Python.
- **Details**:
  - Implement blocks and chains.
  - Vary the hashing difficulty and calculate the execution time for each difficulty level.
  - Verify the correct functionality by providing execution examples.

---
## Lab 2: Encryption/Decryption Algorithm Inspired by RSA

This exercise proposes an encryption and decryption algorithm based on the principles of public-key cryptography, notably the famous RSA algorithm.

### Methodology:
- **Encryption**: The message is encrypted using the public key \( N \) and \( e \), according to the formula \( C = M^e \mod N \), with a slight modification to add a custom offset.
- **Decryption**: The encrypted message is decrypted using the private key \( d \), following a modified formula to retrieve the original message.


### Key Points:
- Dynamic generation of public and private keys.
- Use of prime numbers \( p \) and \( q \) to construct \( N \).
- Implementation of secure encryption and reversible decryption.

### Usage Example:
The file `challenge.py` contains a complete example demonstrating this algorithm with a simple message `"Salam I am Loubna "`, which is encrypted and then decrypted.
![Encryption exp](https://github.com/user-attachments/assets/37b5397a-9168-4c21-888f-694dced75dd6)

And here is an example with the message :8493
![Ecryption exp 2)](https://github.com/user-attachments/assets/dec83475-00dd-4fda-aba1-8ee56dbc8907)





