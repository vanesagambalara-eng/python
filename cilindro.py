import math 


altura = float(input("Ingresa la altura de tu cilindro: "))
radio = float(input("Ingresa el radio de tu cilindro: "))


volumen = math.pi * (radio ** 2) * altura


print("El volumen de tu cilindro es:", volumen)
