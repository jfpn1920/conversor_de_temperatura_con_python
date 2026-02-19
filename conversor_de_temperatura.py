print("#--------------------------------#")
print("#--| conversor  de temperatura|--#")
print("#--------------------------------#")
print("#--| 1) celsius a fahrenheit |---#")
print("#--| 2) fahrenheit a celsius |---#")
print("#--------------------------------#")
opcion = input("seleccione una opcion: ")
if opcion == "1":
    celsius = float(input("ingrese la temperatura en celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("resultado:", int(fahrenheit) if fahrenheit.is_integer() else fahrenheit)
elif opcion == "2":
    fahrenheit = float(input("ingrese la temperatura en fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("resultado:", int(celsius) if celsius.is_integer() else celsius)
else:
    print("opcion no valida")