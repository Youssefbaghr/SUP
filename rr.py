
A=int(input("Entrer un entier: "))

b50= A // 50
print(b50)
A=A%50
print(A)
b20= A // 20
A=A%20
b10= A // 10
A=A%10
b2= A // 2
A=A%2
b1= A // 1
A=A%1
print("Billets de 50: ",b50)
print("Billets de 20: ",b20)
print("Billets de 10: ",b10)
print("Pieces de 2: ",b2)
print("Pieces de 1: ",b1)