# variable 

variable = "Bonjour le monde !"

# snake_case = maniére d'ecrire en python /= camelCase des autres langages

nbr_of_wheels = 4 # nombre de roues (test comm. droite)

# print(variable, nbr_of_wheels)

#int = nombre entier 
a = 1 

#float = nombre decimal 
b = 2.5

#str = string 
c = "hello world !"

#bool = vrai/faux 
d = True

#list = liste --> []
e = [1, 'hello', True]

#tuple = n'est pas modifiable à partir du moment qu'il est assigné --> ()
f = (2, "hello moon", False)

#set = une liste mais on ne peut pas avoir de doublon --> {}
g = {3,"good night", -2.2}

#dict association clé valeur --> {}
h = {
    'bonjour' : 'world',
    3 : True,
    True : '4'
}

#none
i = None

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))

a = 1
b = a + 2
b +=4  # --> valeur de b + 4 = nouvelle valeur de b 

print(b) # 3 of course / c'est des tests petit coquin

#convertion 

a = 1 
b = '2'
c = a + int(b) # = convertion de la chaine de caractére en entier
print(c)


#convertion implicite d'un float 

a = 1
b = 2.5
c = a + b
print(c) #resultat en float même si b = 2.0 --> convertit au type le plus précis
print(type(c)) #affiche la class "float"

a = 1
b = True #True est "1" / False est "0"
c = a + b 
print(c)
print(type(c))

#object immuable --> a = 1 --> a = 2 : la valeur sera 2 parce que la valeur de a est remplacer dans le heap
#object muable ex : list 
a = [1]
a.append(2) #ajout du 2 int à la liste
print(a) # = [1,2]