from qiskit import QuantumCircuit, execute, Aer

# Define a function to create a circuit with two qubits and a variable strength electromagnetic field
def entanglement_circuit(em_strength):
    # Create a quantum circuit with two qubits
    qc = QuantumCircuit(2, 2)

    # Apply a Hadamard gate to the first qubit to create a superposition
    qc.h(0)

    # Apply a phase shift to the second qubit depending on the electromagnetic field strength
    qc.rz(em_strength, 1)

    # Apply a CNOT gate to entangle the two qubits
    qc.cx(0, 1)

    # Measure the qubits to obtain the degree of entanglement
    qc.measure(0, 0)
    qc.measure(1, 1)

    return qc

# Define a range of electromagnetic field strengths to test
em_strengths = [0, 0.1, 0.2, 0.3, 0.4, 0.5]

# Create a dictionary to store the results for each electromagnetic field strength
results = {}

# Run the entanglement circuit for each electromagnetic field strength and store the results
for em_strength in em_strengths:
    qc = entanglement_circuit(em_strength)
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1000)
    result = job.result().get_counts(qc)
    results[em_strength] = result

# Print the results
for em_strength, result in results.items():
    print(f"Electromagnetic field strength: {em_strength}\nResults: {result}\n")
