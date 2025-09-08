# circuits/teleport.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def create_teleport_circuit():
    """
    Teleportation circuit without in-circuit conditional corrections.
    We'll measure Alice's qubits and apply corrections in Python post-processing.
    """
    q = QuantumRegister(3, "q")
    c = ClassicalRegister(3, "c")
    qc = QuantumCircuit(q, c)

    # STEP 1: Prepare an example state on q0 (to teleport)
    qc.h(q[0])  # |+> state

    # STEP 2: Create Bell pair between q1 (Alice) and q2 (Bob)
    qc.h(q[1])
    qc.cx(q[1], q[2])

    # STEP 3: Bell-basis measurement on Alice's side
    qc.cx(q[0], q[1])
    qc.h(q[0])

    # STEP 4: Measure Alice's two qubits (q0, q1) into c0, c1
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])

    # STEP 5: Also measure Bob's qubit (q2) into c2
    qc.measure(q[2], c[2])

    return qc
