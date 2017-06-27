# -*- coding: utf-8 -*-

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""Quick program to test the cost function for different basis functions.
"""
import numpy as np
from scipy import linalg as la
import sys
sys.path.append("../..")
from tools.optimizationtools import Energy_Estimate, make_Hamiltonian, Hamiltonian_from_file
from tools.pauli import Pauli

# printing an example from a H2 file
print(make_Hamiltonian(Hamiltonian_from_file("H2Equilibrium.txt")))

# printing an example from a graph input
n = 3
v0 = np.zeros(n)
v0[2] = 1
v1 = np.zeros(n)
v1[0] = 1
v1[1] = 1
v2 = np.zeros(n)
v2[0] = 1
v2[2] = 1
v3 = np.zeros(n)
v3[1] = 1
v3[2] = 1

pauli_list = [(1, Pauli(v0, np.zeros(n))), (1, Pauli(v1, np.zeros(n))), (1, Pauli(v2, np.zeros(n))), (1, Pauli(v3, np.zeros(n)))]
a = make_Hamiltonian(pauli_list)
print(a)

w, v = la.eigh(a, eigvals=(0, 0))
print(w)
print(v)

data = {'000': 10}
print(Energy_Estimate(data, pauli_list))
data = {'001': 10}
print(Energy_Estimate(data, pauli_list))
data = {'010': 10}
print(Energy_Estimate(data, pauli_list))
data = {'011': 10}
print(Energy_Estimate(data, pauli_list))
data = {'100': 10}
print(Energy_Estimate(data, pauli_list))
data = {'101': 10}
print(Energy_Estimate(data, pauli_list))
data = {'110': 10}
print(Energy_Estimate(data, pauli_list))
data = {'111': 10}
print(Energy_Estimate(data, pauli_list))
