#Samuel Pimentel @samuelpszz
a = "alo"
a1 = " Mundo !."
b = 2022
c = -2022
d = 20.22
e = -20.22
f = True 
g = False

a2 = type(a)
print(a2)
print("Para saber que tipo que dato almacena una variable escribimos: type(variable)")

#suma
a=100 
b=100
print(a+b)     
c=a+(b+100)    
print(c)    
#resta
c = 300
d = c-(a+200) #300-300
print(d)
#division /
a = 115
b = a/5
print("Division de 115 entre 5: "+ str(b))
#division entera //
b = 115//5
print("Parte entera de 115 // 5: "+ str(b))
#resto de la division % EJ: SABER SI UN N° ES PAR 
a = 22
a=a%2
print("22 es multiplo de x2 su Resto es: " + str(a))

a = "Alo"
b = "Mundo"
e = a+" "+b
f = ". yO Soy Samuel !"
print(e+f)
        #saber el la longitd de la cadena len(x)
a = "Programando en Python"
a = len(a)
print("la logitd del string es: " + str(a))


#STRINGS OBS
var = "Programación en python"
var2 = var[-2]
print("-1 de una cadena es: " + str(var2))

var2 = var[0:6]
print("[0:5] de la cadena es: " +var2)

var2 = var[::3]
print("[::2] de la cadena es: " +var2)
    



        #buscar un indice var(x)
c1 = "Hola Mundo"
c2=c1[3]
print("Determinando el indice [1] obtenemos el caracter: " +c2)

d =  "Programacion"
h = d[1+2]
print("Indice con operaciones d[1+2]: " +h)

#operaciones con resultados bool
x = 5 
y = 10
z = 20

a = x > y   #False
print("5 > 10: " + str(a))
a = y > x   #True
print("10 > 5: " + str(a))
a = x>y>z   #False
print("5>10>20: "+ str(a))
a = x<y<z   #True 
print("5<10<20: " + str(a))
#obs: si al convertir un resultado bool a str(+var) el resoltado se trasnforma en int 0 u 1
a = x > y
print("5 > 10:  " + str(+a))
a = y > x  
print("10 > 5:  " + str(+a))
a = x>y>z 
print("5>10>20: " + str(+a))
a = x<y<z 

#tabla ascii: python analiza el peso de cada caracyer de derc a iz 
a = "hola" == "adios"
print("hola = adios: " + str(a))
a = "hola" == "chau"
print("hola = chau: " + str(a))
a = "chau" == "chau"
print("chau = chau: " + str(a))

a = 10 > 5
print("10>5: " + str(a))
a = 10 >= 10
print("10 mayor o igual a 10: " + str(a))

#calcular la edad
    #caso1
edad_user = 15
edad_min = 18 
mostrar_edad = edad_user > edad_min
print("El usuario (15y) es mayor de edad: " + str(mostrar_edad))
    #caso2
edad_user = 19
mostrar_edad = edad_user > edad_min
print("El usuario (19y) es mayor de edad: " + str(mostrar_edad))

        #p.logicas
edad = 17
mostrar = edad>18 and edad<20
print(mostrar)
mostrar = edad>16 and edad<20
print(mostrar)

mostrar = edad>18 or edad<20
print("false true or: " + str(mostrar))
mostrar = edad>18 or edad<16
print("false false or: " + str(mostrar))

esta_presente = True
mostrar = not(esta_presente)
print("el alumno está?: "+str(mostrar))
esta_presente = False
mostrar = not(esta_presente)
print("el alumno está?: "+str(mostrar))

