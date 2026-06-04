import numpy as np

tab_zero = np.zeros(5)
print("1.")
print(tab_zero)

mat_un = np.ones((3, 3))
print("\n2.")
print(mat_un)

tab_float = np.arange(1.5, 11.5, 0.5)
print("\n3.")
print(tab_float)

tab_lin = np.linspace(0, 10, 20)
print("\n4.")
print(tab_lin)

tab_4x5 = np.reshape(tab_lin, (4, 5))
print("\n5.")
print(tab_4x5)

colonnes_impaires = tab_4x5[:, 1::2]
print("\n6.")
print(colonnes_impaires)

lignes_depuis_2 = tab_4x5[2:, :]
print("\n7.")
print(lignes_depuis_2)