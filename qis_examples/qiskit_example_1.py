import numpy as np
import qiskit as qk

ket0 = np.array([1, 0])
ket1 = np.array([0, 1])

print(f'ket0 / 2 + ket1 / 2 = {ket0 / 2 + ket1 / 2})')

M1 = np.array([[1, 1], [0, 0]])
M2 = np.array([[1, 1], [1, 0]])

print(f'M1 / 2 + M2 / 2 = {M1 / 2 + M2 / 2})')

# Matrices multiplication
print(f'M1 * ket0 = {np.matmul(M1, ket0)})')
print(f'M1 * ket1 = {np.matmul(M2, ket1)})')
print(f'M2 * ket0 = {np.matmul(M2, ket0)})')
print(f'M2 * ket1 = {np.matmul(M2, ket1)})')
print(f'M1 * M2 = {np.matmul(M1, M2)})')
print(f'M2 * M1 = {np.matmul(M2, M1)})')

# Quantum Statevectors
u = qk.quantum_info.Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
v = qk.quantum_info.Statevector([(1 + 2.0j) / 3, -2 / 3])
w = qk.quantum_info.Statevector([1 / 3, 2 / 3])

# Check if quantum state is valid

print(f'u is valid: {u.is_valid()}')
print(f'v is valid: {v.is_valid()}')
print(f'w is valid: {w.is_valid()}')

# new vector
v2 = qk.quantum_info.Statevector([(1 + 2.0j) / 3, -2 / 3])
print(v2.measure())

# Operators
X = qk.quantum_info.Operator([[0, 1], [1, 0]])
Y = qk.quantum_info.Operator([[0, -1.0j], [1.0j, 0]])
Z = qk.quantum_info.Operator([[1, 0], [0, -1]])
H = qk.quantum_info.Operator([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
S = qk.quantum_info.Operator([[1, 0], [0, 1.0j]])
T = qk.quantum_info.Operator([[1, 0], [0, (1 + 1.0j) / np.sqrt(2)]])

v = qk.quantum_info.Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(Z)

print(f'new vector v = {v.draw('text')}')

# Circuits

circuit = qk.QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

ket0 = qk.quantum_info.Statevector([1, 0])
v = ket0.evolve(circuit)

