
#This is the "for" structure using a range of numbers (it starsc counting in 0)
for numero in range(6):
    print(numero*3)

#Example 2, Concatenates the number selected in range and adds the multiplication of the number and the string
for numero in range(6):
    print(numero, numero * ' hola mundo ')

# While example, 
numero = 2
while numero < 1024:
    print(numero)
    numero *= 3


# While example, it ends until user command equals to the word "salir"
while True:
    comando = str(input("$ "))
    if comando.lower() == "salir":
        break

# Nested for (loop) structure, it creates an index structure with the variable i and the variable j according to its range
for i in range(1):
    for j in range(3):
        print(f"{i},{j}")
