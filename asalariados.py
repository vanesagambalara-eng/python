
salarioBase = float(input("Ingrese el salario base: "))


porcentajeP = salarioBase * 0.04  # Aporte a pensión
porcentajeS = salarioBase * 0.04  # Aporte a salud

salarioN = salarioBase - (porcentajeP + porcentajeS)

print(f"Su aporte a la salud es: {porcentajeS:.2f}")
print(f"Su aporte a la pensión es: {porcentajeP:.2f}")
print(f"Su salario neto es de: {salarioN:.2f}")
