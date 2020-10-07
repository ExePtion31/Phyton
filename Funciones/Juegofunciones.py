#-*- coding: utf-8 -*-

import turtle as tortuga
import math;

#---------------------FUNCION MAIN----------------------------
def main():
    respuesta = True;
    while respuesta == True:
        tortuga.setup(500,500);
        tortuga.title("La tortuga y sus figuras");
        tortuga.shape("turtle");
        tortuga.color("blue");

        print("\t>---------------Bienvenido---------------<\nPor favor, seleccione una opcion dependiendo de la figura:\n1.Cuadrado\n2.Triangulo\n3.Rectangulo\n4.Circulo\n");
        opcion = int(input("Digite su respuesta: "));
            
        if opcion == 1:
            crearcuadrado();
        elif opcion == 2:
            creartriangulo(); 
        elif opcion == 3:
            crearrectangulo();  
        elif opcion == 4:
            crearcirculo();      

        respuesta = envio_reinicio();
        tortuga.mainloop();
        
            
              
        
#--------------------------------------------------------------




#-----------------------REINICIO-------------------------------    
def envio_reinicio():
    print("\n>-----------------------------<\n¿Desea continuar?\n1.Si\n2.No");
    respuesta = int(input("\nDigite su respuesta: "));
    h = respuesta_reinicio(respuesta);
    return h;


def respuesta_reinicio(respuesta):
    continuar = True;
    if respuesta != 1:
        continuar = False;     

    return continuar;    
#--------------------------------------------------------------




#-----------------------CUADRADO-------------------------------    
def crearcuadrado():
    print("\t>---------------CUADRADO---------------<\n");
    lados = int(input("Digite el valor de los lados del cuadrado: "));

    for i in range(4):
        recorrer_cuadrado(lados)


def recorrer_cuadrado(lados):
    tortuga.forward(lados)
    tortuga.left(90);

#-------------------------------------------------------------




#-------------------------TRIANGULO---------------------------
def creartriangulo():
    print("\t>---------------TRIANGULO---------------<\n");
    lados = int(input("Digite el valor de los catetos del triangulo: "));

    for i in range(2):
        recorrer_triangulo(lados);

    tortuga.left(45);
    tortuga.forward(recorrer_hipotenusa(lados));


def recorrer_triangulo(lados):
    tortuga.forward(lados);
    tortuga.left(90);

def recorrer_hipotenusa(lados):
    hipotenusa = math.sqrt((lados**2)+(lados**2));
    return hipotenusa;    
#-------------------------------------------------------------




#-------------------------RECTANGULO---------------------------
def crearrectangulo():
    print("\t>---------------RECTANGULO---------------<\n");
    ladosh = int(input("Digite el valor de los lados horizontales: "));
    ladosv = int(input("Digite el valor de los lados verticales: "));

    for i in range(2):
        recorrer_rectangulo(ladosh, ladosv);

def recorrer_rectangulo(ladosh, ladosv):
    tortuga.forward(ladosh);
    tortuga.left(90);
    tortuga.forward(ladosv);
    tortuga.left(90);
#-------------------------------------------------------------



#-------------------------CIRCULO---------------------------
def crearcirculo():
    print("\t>---------------CIRCULO---------------<\n");
    ladosh = int(input("Digite el valor del radio del circulo: "));
    recorrer_circulo(ladosh);


def recorrer_circulo(ladosh):
    tortuga.circle(ladosh);

#-------------------------------------------------------------



#-----------------------MAIN----------------------------------
if __name__ == "__main__":
    main();
#-------------------------------------------------------------