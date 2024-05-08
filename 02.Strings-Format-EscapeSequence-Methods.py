#Formattings Strings with f

Name = "Daniel"
Lastname = "Perez"

FullName = f"{Name} {Lastname}"
print(FullName) #This will print on screen: Daniel Perez


#Modifying the sequence of a string
"""Modifiers

\" This will allow to have quotes in the following word
\\ This will allow to show a backslash in the string
\n This will allow to separate the following text on another line
"""


Course = "Course \nof \nPython \"Essentials\""
print(Course)

#String Methods

animal = "beware of dog"
print(animal.upper()) # BEWARE OF DOG
print(animal.lower()) # beware of dog
print(animal.strip().capitalize()) # Beware of dog
print(animal.title()) # Beware Of Dog
print(animal.strip()) # Removes blank spaces from both sides
print(animal.lstrip()) # Removes blank spaces from left side
print(animal.rstrip()) # Removes blank spaces from right side
print(animal.replace("dog", "cat")) # beware of cat
print("dog" in animal) # True
print("dog" not in animal) # False
