#We ask the user for the 2 numbers the calculator will use

numero1 = int(input("Ingresa Primer Número: "))
numero2 = int(input("Ingresa Segundo Número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division= numero1 / numero2

mensaje = f"""
Para los números {numero1} y {numero2},

El resultado de la suma es : {suma}.
El resultado de la resta es : {resta}.
El resultado de la multiplicacion es : {multiplicacion}.
El resultado de la división es: {division}.


"""
print(mensaje)