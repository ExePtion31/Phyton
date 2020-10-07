# -*- coding: utf-8 -*-

nombre = str(input("Digite su nombre: "));
apellido = str(input("Digite su apellido: "));
edad = int(input("¿Qué edad tienes?: "));

print(">----------------------<"+"\nNombre: "+nombre+"\nApellido: "+apellido+"\nEdad: "+str(edad)+"\n>----------------------<")


import turtle as chester #creamos la tortuga y le ponemos nombre

chester.setup(500, 500);#cambiar tamaño de la pantalla
chester.shape("turtle");#cambiar forma del personaje
chester.color("green");#cambiar color del personaje

#movimientos

contador = 20; #el largo de cada lado
suma = 5; #lo que suma en cada lado cuando termina el ciclo
mvto = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]; #cantidad de veces que se repite el ciclo

for item in mvto:
    chester.forward(contador);
    chester.left(90);
    chester.forward(contador);

    contador = contador + suma; 
    

    

chester.mainloop();#no cerrar la ventana



