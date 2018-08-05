# %%
%load_ext autoreload
%autoreload 2

import numpy

# %%

t = [[0.0, 0.9, 0.1, 0.0],
     [0.8, 0.1, 0.0, 0.1],
     [0.0, 0.5, 0.3, 0.2],
     [0.1, 0.0, 0.0, 0.9]]
p = numpy.matrix(t)

# %%

eigenvalues, eigenvectors = numpy.linalg.eig(p)
eigenvalues
eigenvectors
Λ = numpy.diag(eigenvalues)
V = numpy.matrix(eigenvectors)
V_inv = numpy.linalg.inv(V)

Λ_t = Λ**100
V * Λ_t

V * Λ_t * V_inv

p**100

# %%
V_inv[2]/numpy.sum(V_inv[2])
