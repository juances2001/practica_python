codigo_producto1 = (input("Escribe código del producto1: "))
nombre_producto1 = (input("Escribe nombre del producto1: "))
precio_producto1 = float(input("Escribe el precio del producto1: $"))

codigo_producto2 = (input("Escribe código del producto2: "))
nombre_producto2 = (input("Escribe nombre del producto2: "))
precio_producto2 = float(input("Escribe el precio del producto2: $"))

codigo_producto3 = (input("Escribe código del producto3: "))
nombre_producto3 = (input("Escribe nombre del producto3: "))
precio_producto3 = float(input("Escribe el precio del producto3: $"))

sub_total = precio_producto1 + precio_producto2 + precio_producto3

iva = sub_total * 0.32

total = sub_total + iva


print(f"...............................................................")
print(f"...............................................................")
print(f"---------------------Factura de venta--------------------------")
print(f"---------------------------------------------------------------")
print(f"Fecha                28/10/2025 20:40")
print(f"---------------------------------------------------------------")
print(f"Articulos                               Valores del producto") 
print(f"---------------------------------------------------------------")          
print(f" {nombre_producto1}                                            ${precio_producto1:0.0f}")
print(f" {codigo_producto1}") 
print(f"---------------------------------------------------------------")                        
print(f" {nombre_producto2}                                            ${precio_producto2:0.0f}")
print(f" {codigo_producto2}")
print(f"---------------------------------------------------------------")           
print(f" {nombre_producto3}                                            ${precio_producto3:0.0f}")
print(f" {codigo_producto3}")
print(f"---------------------------------------------------------------")
print(f"        Sub total:                 ${sub_total:0.0f}                  ")
print(f"        IVA:                       ${iva:0.0f}               ")
print(f"        Total:                     ${total:0.0f}           ")
print(f"...............................................................")
print(f"...............................................................")