# blockchain_labs

This repository contains my blockchain labs, supervised by Prof. Ikram BENADBELOUAHAB, where I explore the fundamentals of blockchain technology, including implementations of Proof of Work, blocks, chains, and more. The labs aim to provide practical insights into how blockchain systems operate, with varying hash difficulty levels and performance analysis."

Feel free to adjust it to better suit your style!

## Table of Contents

- [Exercise 1: Introduction to Cryptography](#exercise-1-introduction-to-cryptography)
- [Exercise 2: Encryption/Decryption Algorithm Inspired by RSA](#exercise-2-encryptiondecryption-algorithm-inspired-by-rsa)

---

## Exercise 2: Encryption/Decryption Algorithm Inspired by RSA

This exercise proposes an encryption and decryption algorithm based on the principles of public-key cryptography, notably the famous RSA algorithm.

### Methodology:
- **Encryption**: The message is encrypted using the public key \( N \) and \( e \), according to the formula \( C = M^e \mod N \), with a slight modification to add a custom offset.
- **Decryption**: The encrypted message is decrypted using the private key \( d \), following a modified formula to retrieve the original message.


### Key Points:
- Dynamic generation of public and private keys.
- Use of prime numbers \( p \) and \( q \) to construct \( N \).
- Implementation of secure encryption and reversible decryption.

### Usage Example:
The file `exercise2.py` contains a complete example demonstrating this algorithm with a simple message `"Salam I am Loubna "`, which is encrypted and then decrypted.



