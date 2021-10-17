#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from numpy.random import randint
import numpy as np


# In[2]:


nBits = int(input("Please enter the number of bits you want to send to the user(Upper Limit: 100): "))
bits = ""
arr = randint(2, size = nBits)
for i in arr:
    bits += str(i)

basesServer = ""
arr = randint(2, size = nBits)
for i in arr:
    if i == 0:
        basesServer += 'X'
    else:
        basesServer += 'Z'
        
print("The randomly generates bit sequence is:", bits)


# In[3]:


def bitsToQubits(bits, bases):
    qubitsSent = []
    for i in range(nBits):
        qc = QuantumCircuit(1, 1)
        if bases[i] == 'Z':
            if bits[i] == 0:
                pass
            else:
                qc.x(0)
        else:
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qubitsSent.append(qc)
    return qubitsSent


# In[4]:


print("Please Wait! Converting Bits to Qubits")
qubitsSent = bitsToQubits(bits, basesServer)

basesUser = ""
arr = randint(2, size = nBits)
for i in arr:
    if i == 0:
        basesUser += 'X'
    else:
        basesUser += 'Z'
print("User Computer has randomly generated bases sequence!")


# In[5]:


def qubitsToBits(qubits, bases):
    backend = Aer.get_backend('aer_simulator')
    bitsUser = []
    for i in range(nBits):
        if bases[i] == 'Z':
            qubits[i].measure(0, 0)
        else:
            qubits[i].measure(0, 0)
        aer_sim = Aer.get_backend('aer_simulator')
        qobj = assemble(qubits[i], shots=1, memory=True)
        result = aer_sim.run(qobj).result()
        measured_bit = int(result.get_memory()[0])
        bitsUser.append(measured_bit)
    return bitsUser


# In[6]:


print("Please Wait! Converting Qubits to bits")
bitsUser = qubitsToBits(qubitsSent, basesUser)


# In[7]:


common = []
for i in range(nBits):
    if basesUser[i] == basesServer[i]:
        common.append(str(bitsUser[i]))
    else:
        pass
    
print("KEY GENERATED!!")
print("ALL THE FOLLOWING MESSAGES WILL BE ENCRYPTED BY KEY:", ''.join(common))

