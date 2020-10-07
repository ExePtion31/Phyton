# -*- coding: utf-8 -*-

#Mensaje de Bienvenida
print(">----------Bienvenido----------<"+"\nSeleccione la figura que desea crear:\n1.Cuadrado.\n2.Triangulo.\n3.Rectangulo.\n4.Circulo.");
figura = int(input("\n*Digite el número de la figura: "));
print(">------------------------------<");

import turtle as tortuga #creamos la tortuga y le ponemos nombre

tortuga.setup(500, 500);#cambiar tamaño de la pantalla
tortuga.shape("turtle");#cambiamos diseño del personaje
tortuga.color("blue");#cambiamos color personaje

# Número 1 = Cuadrado 
# Número 2 = Triangulo
# Número 3 = Rectángulo
# Número 4 = Circulo


if figura == 1: #Condición dependiendo del Número
    mvtos = [1,2,3,4]; #Cantidad de movimientos que usaremos para el for

    print("-- SELECCIONÓ EL CUADRADO --");
    lados = int(input("\n-Digíte el tamaño de los lados: "));#Guardamos el número que nos digita el usuario

    for item in mvtos: #for para hacer el mismo recorrido 
        tortuga.forward(lados) #el tamaño de cada lado depende de lo que haya ingresado el usuario
        tortuga.left(90); 

    tortuga.mainloop();    
    
elif figura == 2:
    print("-- SELECCIONÓ EL TRIÁNGULO --");
    lados = int(input("\n-Digíte el tamaño de los vértices: "));

    tortuga.forward(lados);
    tortuga.left(120);
    tortuga.forward(lados);
    tortuga.left(120);
    tortuga.forward(lados);

    tortuga.mainloop(); 
elif figura == 3:
    mvtos = [1,2];

    print("-- SELECCIONÓ EL RECTÁNGULO --");
    lado1 = int(input("\n-Digíte el tamaño de los lados horizontales: "));
    lado2 = int(input("\n-Digíte el tamaño de los lados verticales: "));

    
    for item in mvtos:
        tortuga.forward(lado1);
        tortuga.left(90);
        tortuga.forward(lado2);
        tortuga.left(90);

    tortuga.mainloop(); 

elif figura == 4:
    print("-- SELECCIONÓ EL CÍRCULO --");

    i=2;
    for item in range(180):
        tortuga.forward(i);
        tortuga.left(i);

    tortuga.mainloop(); 





