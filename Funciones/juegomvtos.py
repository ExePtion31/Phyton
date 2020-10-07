# -*- coding: utf-8 -*-
import random;
from turtle import *

tortuga = Turtle();
objeto = Turtle();
winsiganal = Turtle();
losesignal = Turtle();
nmovimientos = Turtle();
screen = Screen();


#------------funcion main-----------------
def main():
    create_screen();

#----------------------------------------



#---------------screen-------------------
def create_screen():
    screen.title("Juego Tortuga");
    screen.bgcolor("#ffffff");
    edit_pj();
    screen.mainloop();
#---------------------------------------



#-----------Seleccionar figura-----------
def edit_pj():
        figura = screen.textinput("Seleccion de personaje." , "Seleccione el personaje que desea usar:\n1.Flecha\n2.Tortuga\n3.Triangulo\n4.Clasico");
        if figura == "1":
            figura = "arrow";
        elif figura == "2":  
            figura = "turtle";
        elif figura == "3":  
            figura = "triangle";  
        elif figura == "4":  
            figura = "classic";

        color = screen.textinput("Seleccion de color." , "Seleccione el color del personaje que desea usar:\n1.Amarillo\n2.Azul\n3.Rojo\n4.Verde\n5.Negro\n6.Purpura");
        if color == "1":
            color = "yellow";
        elif color == "2":  
            color = "blue";
        elif color == "3":  
            color = "red";  
        elif color == "4":  
            color = "green";  
        elif color == "5":  
            color = "black";  
        elif color == "6":  
            color = "purple";                        
        creartortuga(figura, color);
#---------------------------------------



#--------crear tortuga------------------
def creartortuga(figura,color):
    tortuga.shape(figura);
    tortuga.color(color);
    tortuga.penup();
    crearobjeto();
    
#--------------------------------------



#--------crear objeto------------------
def crearobjeto():
    objeto.shape("circle");
    objeto.color("red");
    objeto.speed(0);
    objeto.penup();
    movimientos_restantes();
    
#--------------------------------------



#-------------Numero de movimientos---------------
def movimientos_restantes():
    nmovimientos.clear();
    nmovimientos.speed(0);
    nmovimientos.shape("square");
    nmovimientos.color("black");
    nmovimientos.penup();
    nmovimientos.goto(0, 250);
    winsiganal.hideturtle();
    losesignal.hideturtle();
    nmovimientos.hideturtle() #volver la tortuga invisible.
    nmovimientos.write("Movimientos: 5", align="center", font=("Courier", 24, "normal")) 
    posicionamiento();

#-------------------------------------------------



#--------Posicionar objetos aleatoriamente en el mapa------------------
def posicionamiento():
    tortugaX = random.randint(0, 250);
    tortugaY = random.randint(0, 250);
    objetoX = random.randint(-250, 0);
    objetoY = random.randint(-250, 0);
    tortuga.goto(tortugaX, tortugaY);
    objeto.goto(objetoX, objetoY);  
    winsiganal.goto(0, 0);
    losesignal.goto(0, 0);
    turtle_move();
#---------------------------------------------------------------------


#----------mvtos tortuga---------------
def turtle_move():
    winsiganal.clear();
    losesignal.clear();
    resta = 5;

    while True:
        movimiento = int(screen.textinput("Menú de opciones:", "1.Adelante\n2.Atras\n3.Giro izquierda\n4.Giro derecha\n5.Editar personaje."));
        
        if movimiento == 1:
            turtle_up();
        elif movimiento == 2:
            turtle_down();
        elif movimiento == 3:
            turtle_left();
        elif movimiento == 4:
            turtle_right();
        elif movimiento == 5:
            edit_pj();    
        elif movimiento >5:
            turtle_move();    

        turtle_moves_remaining(resta);
        resta = turtle_moves_remaining(resta);
        turtle_collision();                 
#-------------------------------------



#----------direcciones----------------
def turtle_up():
    distancia = int(screen.textinput("Distancia tortuga:", "Cuanta es la distancia la cual desea que recorra la tortuga."));
    tortuga.forward(distancia);

def turtle_down():
    distancia = int(screen.textinput("Distancia tortuga:", "Cuanta es la distancia la cual desea que recorra la tortuga."));
    tortuga.backward(distancia);

def turtle_left():
    distancia = int(screen.textinput("Radio del giro:", "Cuantos grados desea que gire la tortuga."));
    tortuga.left(distancia); 

def turtle_right():
    distancia = int(screen.textinput("Radio del giro:", "Cuantos grados desea que gire la tortuga."));
    tortuga.right(distancia);
#-------------------------------------




#------------cantidad de mvtos-------------
def turtle_moves_remaining(resta):
    resta = resta -1;
    nmovimientos.clear();
    nmovimientos.write("Movimientos: {}".format(resta), align="center", font=("Courier", 24, "normal")); 
    if resta <=0:
        if tortuga.distance(objeto) <20:
            win_signal();
        else:
            lose_signal();
    return resta;
#-----------------------------------------



#-----------señales de winner/lose----------
def win_signal():
    winsiganal.speed(0);
    winsiganal.shape("square");
    winsiganal.color("black");
    winsiganal.penup();
    winsiganal.hideturtle() #volver la tortuga invisible.
    winsiganal.write("¡WINNER!", align="center", font=("Courier", 30, "normal")) 
    continue_game();

def lose_signal():
    losesignal.speed(0);
    losesignal.shape("square");
    losesignal.color("black");
    losesignal.penup();
    losesignal.hideturtle() #volver la tortuga invisible.
    losesignal.write("¡LOSER!", align="center", font=("Courier", 30, "normal")) 
    continue_game();
#-------------------------------------



#-----------continuar juego-----------
def continue_game():
    respuesta = screen.textinput("Desea continua:", "¿Desea continuar con el juego?:\n1.Si\n2.No");

    if respuesta == "no":
        exit();
    elif respuesta == "No":
        exit();
    elif respuesta == "NO":
        exit();
    elif respuesta == "nO":
        exit();      
    elif respuesta == "2":
        exit();
    elif respuesta == "1":
        movimientos_restantes();
    elif respuesta == "si":
        movimientos_restantes();
    elif respuesta == "Si":
        movimientos_restantes();
    elif respuesta == "sI":
        movimientos_restantes();
    elif respuesta == "SI":
        movimientos_restantes();                    
#------------------------------------



#---------Colision objeto-------------
def turtle_collision():
    if tortuga.distance(objeto) <20:
        win_signal()
    elif tortuga.xcor()>250 or tortuga.xcor()<-250 or tortuga.ycor()>250 or tortuga.ycor()<-250:
        lose_signal();   
        
#------------------------------------


#---------main-----------
if __name__ == "__main__":
    main();
#------------------------    