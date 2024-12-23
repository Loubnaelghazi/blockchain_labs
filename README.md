# blockchain_labs

This repository contains my blockchain labs, supervised by Prof. Ikram BENADBELOUAHAB, where I explore the fundamentals of blockchain technology, including implementations of Proof of Work, blocks, chains, and more. The labs aim to provide practical insights into how blockchain systems operate, with varying hash difficulty levels and performance analysis."

Feel free to adjust it to better suit your style!

## Table of Contents

- [Lab 1: Cryptography and Blockchain Concepts](#Lab-1-cryptography-and-blockchain-concepts)
- [Lab 2: Encryption/Decryption Algorithm Inspired by RSA](#Lab-2-encryptiondecryption-algorithm-inspired-by-rsa)
- [Lab 3: Custom Hash Function in Python](#Lab-3-custom-hash-function-in-python)
- [Lab 4: MiniSocial Contract](#Lab-4-minisocial-contract)

---
## Lab 1: Cryptography and Blockchain Concepts
This workshop covers fundamental topics in cryptography and blockchain, including the implementation of a Merkle Tree and Proof of Work.

## Exercise 1: Merkle Tree
- **File**: atelier1.cpp
- **Objective**: Implement a basic Merkle Tree from scratch using C++.

---

## Exercise 2: Proof of Work
- **File**: ex2atlier1.py
- **Objective**: Implement Proof of Work in Python.
- **Details**:
  - Implement blocks and chains.
  - Vary the hashing difficulty and calculate the execution time for each difficulty level.
  - Verify the correct functionality by providing execution examples.

---
## Exercise 3: Proof of State

This exercise **ex3ATelier1.py** demonstrates and compares two popular consensus mechanisms used in blockchain technology: **Proof of Work (PoW)** and **Proof of Stake (PoS)**. 
The code provides implementations of both mechanisms and measures the execution time required for each to add a new block to the blockchain.

## Overview

### Proof of Work (PoW)

In PoW, miners compete to solve a computationally intensive puzzle to add a new block to the blockchain. The difficulty of this puzzle (adjustable via a parameter) determines how hard it is to find a hash that starts with a certain number of leading zeros. Higher difficulty leads to longer execution times.

### Proof of Stake (PoS)

In PoS, validators are chosen to add a new block based on the stake (amount of cryptocurrency) they hold. The higher the stake, the greater the chance of being selected as a validator. PoS does not involve intensive computational work, so it is typically faster than PoW. Here, we simulate the PoS process with a small time delay to represent validation tasks.

I already implemented the PoW algorithme in Exercise 2, so we can compare it with PoS algorithm.

The code will execute the following steps:
   - Create a PoW blockchain and add a block, displaying the time taken.
   - Create a PoS blockchain, add validators, and add a block using the PoS method, also displaying the time taken.
   - Print the execution times for each mechanism.


## Code Structure

### `PoWBlock` and `PoWBlockchain`

The `PoWBlock` class represents a block in the PoW blockchain. The `mine_block()` method performs the PoW hashing by incrementing the nonce until a hash with the required number of leading zeros is found.

The `PoWBlockchain` class initializes the blockchain and allows adding new blocks with a specified difficulty.

### `PoSBlock` and `PoSBlockchain`

The `PoSBlock` class represents a block in the PoS blockchain. It requires only a hash computation without nonce iteration since no computational puzzle is involved.

The `PoSBlockchain` class initializes the blockchain, allows adding validators, and selects a validator for each new block based on their stake.

### Code Execution

![Screenshot (436)](https://github.com/user-attachments/assets/c73b5157-5553-44b1-aa89-5a330a0fbf30)


---
### Results

The code will output the time taken for each block addition. Generally, PoS is faster than PoW due to the lack of computational work in PoS



















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


---
## Lab 3: Custom Hash Function in Python




Concept Behind the Custom Hash Function

The hachage() function in **challenge3.py**  operates on a sequence of characters in a string and uses custom bitwise operations and a dynamic accumulator to disperse the bits of each character, ultimately generating a unique hash output. The function is structured as follows:

### Initialization:
  hachage: This variable starts with a unique base value (1037), which will be transformed iteratively.<br/>
  accumulateur: An initial accumulator value (11) helps add entropy by adjusting the effects of each character in the string.

### Character Processing:
  For each character in the input string, the function computes its ASCII value. The ASCII value is then modified by the current position in the string to add variability between strings with similar content.

### Dynamic Bitwise Operations:
  Dynamic Bit Shifting: Each character's ASCII value affects a bitwise left shift on hachage, modulated by the accumulator. This process redistributes the bits of hachage in a way that makes the hash values sensitive to even small changes in the input.
  
  Conditional Bit Inversion: If the ASCII value of the character is even, the bits in hachage are inverted. This introduces non-linear changes to the hash value, increasing the difference between similar inputs.

### Updating the Accumulator:
  The accumulator changes with each character using a custom formula. This alteration further ensures that each character impacts the hash differently based on its position and previous values, adding layers of uniqueness and minimizing potential collisions.

### Final Hash Value:
  After processing all characters, the function returns hachage, limited to 32 bits, providing a consistent hash size.

  You can use the hachage function to generate hash values for strings. Example usage:

  ![Screenshot (435)](https://github.com/user-attachments/assets/a33a539e-b3be-4103-be8e-a93efaf9837d)

---
## Lab 4: MiniSocial Contract

The **MiniSocial**  smart contract on the Ethereum blockchain, allows users to post, view, and delete messages . This contract is written in Solidity, the programming language used to write smart contracts on the Ethereum blockchain.

## Key Features

1. **Publish a Post**: Users can publish a message to the blockchain. Each message is associated with the address of the author (the user who posted the message).
2. **View a Post**: Users can view a message by specifying the index of the post in the list of posts.
3. **Delete a Post** (which I added): Users can delete their own posts by specifying the post index. The deletion is performed by replacing the deleted post with the last post in the list, and then removing the last post.

## Functions

### `publishPosts(string memory message)`
- **Description**: Allows a user to publish a post with a given message.
- **Parameters**: 
  - `message` (string): The message content to be published.
- **Visibility**: Public.

### `getPost(uint index) public view returns (string memory, address)`
- **Description**: Returns the message and the author's address of the post at a given index.
- **Parameters**: 
  - `index` (uint): The index of the post to be retrieved.
- **Visibility**: Public.

### `deletePost(uint index)`
- **Description**: Deletes the post at the specified index, but only if the sender is the author of the post.
- **Parameters**: 
  - `index` (uint): The index of the post to be deleted.
- **Visibility**: Public.

### `getTotalPosts() public view returns (uint)`
- **Description**: Returns the total number of posts.
- **Visibility**: Public.

## How it Works

1. When a user calls the `publishPosts` function, the message is added to the `posts` array, along with the sender's address.
2. The `getPost` function allows users to retrieve any post by specifying the index.
3. The `deletePost` function allows the user to delete their own posts by replacing the deleted post with the last post in the array and removing it.
4. The `getTotalPosts` function provides the total number of posts currently stored in the contract.


## Deployment 

An exemple showing how to post 
![Screenshot (449)](https://github.com/user-attachments/assets/2e70575a-59ee-4f77-837a-03e8d49be855)


An exemple of deleting post 1 
![Screenshot (450)](https://github.com/user-attachments/assets/d347c0ed-44b0-41ec-bc6a-d09c3964b429)



   




