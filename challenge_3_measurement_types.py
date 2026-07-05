"""
Challenge 3: Compare Measurement Types

Question: 
Write a circuit that makes superposition/entanglement.
Use 3 measurement types: probs, sample (shots=10), counts (shots=1000).
Then add an expectation value measurement using: PauliZ and custom Hermitian.
"""

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def circuit_probs():
    qp.H(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.probs()

# Device for samples with low shots
dev_sample = qp.device("default.qubit", wires=2, shots=10)
@qp.qnode(dev_sample)
def circuit_sample():
    qp.H(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.sample()

# Device for counts with high shots
dev_counts = qp.device("default.qubit", wires=2, shots=1000)
@qp.qnode(dev_counts)
def circuit_counts():
    qp.H(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.counts()

# Hermitian part
U = np.array([[1, 0], [0, -1]])

@qp.qnode(dev)
def circuit_pauli():
    qp.H(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.expval(qp.Z(0))

@qp.qnode(dev)
def circuit_hermitian():
    qp.H(wires=0)
    qp.CNOT(wires=[0, 1])
    return qp.expval(qp.Hermitian(U, 0))

print("Probs:\n", circuit_probs())
print("\nSample (10 shots):\n", circuit_sample())
print("\nCounts (1000 shots):\n", circuit_counts())
print("\nPauliZ Expval:", circuit_pauli())
print("Hermitian Expval:", circuit_hermitian())

"""
My Answers:

3.1: 'sample' is like taking real samples, but they are random based on the probability ratio of the result.

3.2: Because probabilities don't have to appear exactly in order every time. It could be 50%, but shows up 7 out of 10 times. That doesn't make it 70%. So we increase the shots to make the ratio more accurate. If we raise it to 100, it might become 60 out of 100. As shots increase, it gets more accurate.

3.3: Because 'probs' is the ratio of how results appear in 'counts'. The same applies here: the more shots we add, the more accurate and closer to probs this ratio gets.

3.4: Yes, as the last experiment showed. The reason is that PauliZ is ultimately just a matrix, so using a similar matrix will give the same result. Hermitian just converts it from an applied matrix to a measurement matrix like PauliZ.
"""
