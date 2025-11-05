import math  

num = float(input("Ingrese un número: "))

seno = math.sin(num)
coseno = math.cos(num)
tangente = math.tan(num)
raizN = math.sqrt(num)
logaritmoN = math.log(num)  

print(f"\nDel número {num}:")
print(f"Su seno es: {seno:.4f}")
print(f"Su coseno es: {coseno:.4f}")
print(f"Su tangente es: {tangente:.4f}")
print(f"Su raíz cuadrada es: {raizN:.4f}")
print(f"Su logaritmo natural es: {logaritmoN:.4f}")
