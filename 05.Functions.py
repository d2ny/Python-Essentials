#1.Creation and definition of a basic function that prints the sentence: "Hello World!"
def hello():
    print("Hello World!")

#We can call the function in the following line:
hello()

#Parameter name set for function "helloParameter"
name = " Rajada "

#2.Creation and definition of a function using variables
def helloParameter(name, place):

    print(f"Wave of the ocean of the beach {name}, located at {place} ")

# Optional parameters

#We call the function "helloParameter"

helloParameter(name, place=" Guanacaste")
helloParameter(name, " Guanacaste")
helloParameter("Tambor", " Puntarenas")

#3.Creation and definition of a function to replace some specific words using a "for" and put them in lower case
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("?", ""),
        ("¿", ""),
        (",", ""),
        (".", ""),
        (":", ""),
        ("", ""),
        ("*", ""),
        (" ", ""),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
    s = s.lower()
    return s

#We call the function "normalize"
print(normalize("?sd vgsadv s?,?sd fsd ag***"))

#4.Creation and definition of a function that uses the arithmetic operation for sum.
def suma(num1, num2):
    return num1+num2

#We call and show on terminal the results of the function "suma" using it's two parameters.
print(suma(56, 56))
#end