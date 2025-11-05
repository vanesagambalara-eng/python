import math  # Para usar la función sqrt (raíz cuadrada)

cat1 = float(input("Escribe el primer cateto: "))
cat2 = float(input("Escribe el segundo cateto: "))

hipotenusa = math.sqrt(cat1 ** 2 + cat2 ** 2)

print("La hipotenusa de tu triángulo es:", hipotenusa)
