"""
Challenge 1: Build a Reusable Circuit

Question: 
Write a PennyLane circuit with 2 qubits running on default.qubit.
Start from |00>. Create a subcircuit that puts the 1st qubit in superposition 
then entangles it with the 2nd. Use this inside a QNode.
Return: probs of the 4 states, and expectation value of PauliZ on the 1st qubit.
Test with numeric wires (0, 1) and string wires ("A", "B").
"""

import pennylane as qp
from pennylane import numpy as np

# Testing with numeric wires
dev1 = qp.device("default.qubit", wires=2)

def subcircuit(w1, w2):
    qp.H(wires=w1)
    qp.CNOT(wires=[w1, w2])

@qp.qnode(dev1)
def circuit1():
    subcircuit(0, 1)
    return qp.probs(), qp.expval(qp.Z(0))

print("With numbers:")
print(circuit1())

# Testing with string wires
dev2 = qp.device("default.qubit", wires=['A', 'B'])

@qp.qnode(dev2)
def circuit2():
    subcircuit('A', 'B')
    # Specified the wires here to avoid measurement errors
    return qp.probs(wires=['A', 'B']), qp.expval(qp.Z('A'))

print("\nWith letters:")
print(circuit2())

"""
My Answers:

1.1: Because it shows that the two qubits are connected and affect each other. If the first is 0, the second stays 0, and if the first becomes 1, the second becomes 1 too. This is one of the 4 Bell states.

1.2: I didn't fully understand the question, but these are two different things. The subcircuit is a ready-to-use circuit with gates, while wires are just the qubits where we apply the gates or actions.

1.3: I expect 0 because the ratio is equal (50 to 50). If we multiply the ratios by 1 and -1 and sum them up, the result will be 0. This is because the arrow is right in the middle and doesn't lean to any pole.
"""