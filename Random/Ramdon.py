import random
print("======================================================")

print("random.random() = ",random.random())
print("random.uniform(1,10) = ",random.uniform(1,10))

print("======================================================")
for i in range(20):
    print("random.randrange('{}') = ".format(10),random.randrange(10))
print("======================================================")
print("random.randrange('{}','{}') = ".format(0,20),random.randrange(0,20))

# Random multiplo de 2
print("random.randrange('{}','{}','{}') = ".format(0,20,2),random.randrange(0,20,2))

# Collections
c = "Hola mundo"
print(random.choice(c))

l = [1,2,3,4,5,6]
print(random.choice(l))

random.shuffle(l) #Desordenar aleatoriamente
print(l)

#Tomar n = 3 muestra aleatoria de una lista
print(random.sample(l,3))