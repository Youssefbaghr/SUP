n = 20
U_0 = 2
U_1 = 1
U = [U_0, U_1]
for i in range(2, n + 1):
    U.append(U[i - 1] +  U[i - 2])

for i, val in enumerate(U):
    print(f"U_{i} = {val}")
