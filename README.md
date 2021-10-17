# Simulation-implementing-quantum-cryptography

This is a project submitted for the Ahmedabad University campaign at Qiskit Fall Fest 2021. The team consists of:

* Arya Parekh

* Amogh Madan

* Aniruddha Sharma


# Quantum Cryptography Implementation

We are trying to make a simulation that successfully implements either the BB84 or the E91 protocols of quantum cryptography.

The BB84 Protocol

* The BB84 protocol mainly depends of the unreliability of qubits when measured from different basis states.
* The user is provided a bunch of qubits by the server and then they are measured in different basis states by both the user and the server.
* Then the user shares the basis states used by them to the server. All the basis states are compared and then sent back to user.
* The basis states that do not match are thrown away, and the states that did match are the key that can be used to encrypt and decrypt the messages.

The E91 Protocol

* The E91 protocol depends on quantum entanglement of qubits to maintain a secure channel.
* A trusted third-party provides quantum entangled qubits to both the server and the user.
* After that, qubits are measured in three different basis states.
* The basis states used are shared and then the qubits with same basis states are used as key and the qubits with different basis states are used to check bell's inequality.

# Why opt for quantum cryptography?

* Our current cryptography standards use one way functions to encrypt and decrypt the messages.
* Quantum computers which might become mainstream in upcoming years make it very easy to get the answers to these one way functions using Shor's algorithm.
* Due to this, we must fight quantum with quantum... in a sense. 
