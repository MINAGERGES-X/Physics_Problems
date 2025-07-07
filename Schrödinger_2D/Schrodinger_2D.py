import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.sparse import diags, kron, eye

# Parameters that represents the length of the well(L), the number grid points (N) and the grid spacing
L = 1.0               
N = 50                
dx = L / (N + 1)      
x = np.linspace(dx, L - dx, N)
y = np.linspace(dx, L - dx, N)

# In this step we construct 1D Laplacian operator (tridiagonal)
main_diag = 2.0 / dx**2 * np.ones(N)
off_diag = -1.0 / dx**2 * np.ones(N - 1)

# In this step we construct 1D Laplacian matrix
T = diags([off_diag, main_diag, off_diag], [-1, 0, 1], shape=(N, N)).toarray()

# Constructing a 2D Laplacian via Kronecker sum: H = T ⊗ I + I ⊗ T
I = np.eye(N)
H = np.kron(T, I) + np.kron(I, T)

# Then we proceed to solve the eigenvalue problem
num_eigenstates = 9
energies, wavefuncs = eigh(H)

# Extracting and reforming the lowest energy eigenstates via a colour map
for i in range(num_eigenstates):
    psi = wavefuncs[:, i].reshape((N, N))
    prob_density = psi**2

    plt.subplot(3, 3, i+1)
    plt.imshow(prob_density, extent=(0, L, 0, L), origin='lower', cmap='viridis')
    plt.title(f'n={i+1}, E={energies[i]:.3f}')
    plt.colorbar(label='|ψ(x,y)|²')

plt.suptitle('Probability Densities of First 9 Quantum States in 2D Infinite Well')
plt.tight_layout()
plt.show()
