print("Hola Mundo [upper()]".upper())
print("------------------------")
print("Hola Mundo [lower()]".lower())
print("------------------------")
print("Hola Mundo [capitalize()]".capitalize())
print("------------------------")
print("HOLA MUNDO [casefold()]".casefold())
print("------------------------")
print("Hola Mundo [title()]".title())
print("------------------------")
print("Hola Mundo [count(\"o\")]".count("o"))
print("------------------------")
print("Hola mundo [find()]".find("mundo")) #Ultima
print("Hola mundo mundo mundo [find()]".rfind("mundo")) #Ultima aparicion


c = "100"
print(c.isdigit())
print("------------------------")
c2 = "ABC10002"
print(c2.isalnum())
print("------------------------")
print(c2.isalpha())
print("------------------------")
print("isaffdsf".islower())
print("isaffdsf".isupper())
print("isaffdsf".istitle())
print("isaffdsf".isspace())
print("isaffdsf".startswith("isa"))
print("isaffdsf".endswith("ffdsf"))

print("Hola mundo mundo".split())
print("Hola mundo mundo".split()[-1])
print("Otra, palabra, revisada".split(","))
textoLista = "Otra, palabra, revisada".split(",")
textoUnido = ",".join("Hola Munda")
print(textoUnido)

print("    HOLA MUNDO    ".strip())

print("HOLA MUNDO".replace('O','1'))
print("HOLA MUNDO MUNDO MUNDO".replace('O','1',3))

