# -*- coding utf-8 -*-
import turtle as tortuga #creamos la tortuga y le ponemos nombre   
import math;

def main(): 
    tortuga.setup(500, 500);#cambiar tamaño de la pantalla
    tortuga.shape("turtle");#cambiamos diseño del personaje
    tortuga.title("Juego creado por Giovanni Baquero");
    tortuga.color("blue");
    tortuga.bgcolor("black")
    tortuga.penup(); #Quitar la linea
    tortuga.goto(-100, 50); #Posicionar la tortuga
    #tortuga.pendown(); #Poner la linea

    #make_square();
    make_triangle();
    tortuga.mainloop();


def make_square():
    tamaño = int(input("Digite el tamaño de los lados: "));
    for i in range(4):
        make_line_and_turn(tamaño);


def make_line_and_turn(tamaño):
    tortuga.forward(tamaño);
    tortuga.left(90);


def make_triangle():
    catetos = int(input("Digite el valor de los catetos: "));
    for i in range(2):
        make_line_and_turn(catetos);
    tortuga.left(45);    
    tortuga.forward(make_hipotenusa(catetos));   

def make_hipotenusa(catetos):
    h = math.sqrt((catetos**2)+(catetos**2));
    return h;

#Metodo main
if __name__ == "__main__":
    main();