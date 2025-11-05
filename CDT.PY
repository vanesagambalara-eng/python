
invertido = float(input("Ingrese el valor invertido: "))
porcentajeI = float(input("Ingrese el porcentaje de interés: "))
periodo = float(input("Ingrese el período en días: "))

valorIn = (invertido * (porcentajeI / 100) * periodo) / 360
descuentoRF = valorIn * 0.07
nPagar = invertido + (valorIn - descuentoRF)

print(f"Sus intereses generados fueron de: {valorIn:.2f}")
print(f"Su descuento por retención en la fuente es de: {descuentoRF:.2f}")
print(f"Su invertido neto son de: {nPagar:.2f}")
