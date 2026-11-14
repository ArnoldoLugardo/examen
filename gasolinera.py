print("bienvenido!!!")                             # inicio

print("seleccione el tipo de gasolina:")   # elegir el tipo de gasolina
gasolina = input("regular, magna o dissel:")       

if gasolina == "r": precio_por_litro = 24 # variables de precios
elif gasolina =="m": precio_por_litro = 32

litros=int(input("ingrese litros:"))         # cantidad de litros

subtotal = litros*precio_por_litro           # subtotal
if litros >= 50: 
    total = subtotal*0.90
    print("descuento: 10%")
else:
    litros<50 
    total = subtotal
    print("descuento: no aplica")

print(f"total:${total:f}")                 # total
print("vuelva pronto!!!")                     # fin