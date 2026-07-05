"""
Challenge 2: Test the Effect of Quantum Operations

Question: 
Write a QNode with a parameter 'theta'.
Inside the circuit: apply a rotation on one qubit, apply a phase gate like RZ, 
apply a controlled operation between 2 qubits, add a gate then cancel it using adjoint.
Run for 0, pi/2, pi and return the final probabilities.
"""

import pennylane as qp
from pennylane import numpy as np

dev = qp.device("default.qubit", wires=2)

@qp.qnode(dev)
def circuit(theta):
    qp.RX(theta, wires=0)
    qp.RZ(theta, wires=0)
    
    qp.X(0)
    qp.adjoint(qp.X)(0)
    
    qp.ctrl(qp.X, control=0, control_values=1)(wires=1)
    
    return qp.probs()

# Used np.pi because PennyLane takes radians, not degrees
print("Angle 0:")
print(circuit(0))

print("\nAngle 90 (pi/2):")
print(circuit(np.pi / 2))

print("\nAngle 180 (pi):")
print(circuit(np.pi))

"""
My Answers:

2.1: The one that changes probabilities when the angle changes is RX. I tried deleting RZ in all angles and it didn't change the probabilities in any of them.

2.2: No, and I mentioned the reason in 2.1.

2.3: When applying a gate directly to a qubit, it is applied right away without any condition. But the control gate depends on the state of the control qubit. If the condition is to be 1 and it is 1, it applies. If it's 0, it doesn't.

2.4: Because I put an X gate before the control. If the gate was applied (at angle 0), the control would be affected and give a probability of 1 for '11'. If not applied, it gives 1 for '00'. This is exactly what happened in the experiment.
"""