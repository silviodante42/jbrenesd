#Tarea $2
#Crear app que imprima numeros primos de 1 a 100

for i in range (0,100):
    if i > 2:
        for x in range(2,i):
            if (i%x)==0:
                break
        else:
            print(i)