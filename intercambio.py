#Intercambio de valores entre dos palabras
A = input("Escribe la primera palabra (A): ")
B = input("Escribe la segunda palabra (B): ")


A, B = B, A

print("Despuus del intercambio ")
print("A =", A)
print("B =", B)