# -*- coding: utf-8 -*-

import threading;
import time;
import random;
from turtle import *;


screen = Screen();
snake = Turtle();
fruit = Turtle();
winsignal = Turtle();
losesignal = Turtle();
signaltime = Turtle();
mvtosignal = Turtle();
segments = [];
segments2 = [];

#----------metodo main---------
def main():
   createscreen();
#------------------------------



#----------screen--------------
def createscreen():
    screen.title("Parcial Snake");   
    creation_snake();
    screen.mainloop(); 
#------------------------------



#-------creacion del snake--------
def creation_snake():
    snake.shape("triangle");
    snake.color("green");
    snake.penup();
    create_fruit();
#--------------------------------    


#-----creacion fruta--------------
def create_fruit():
    fruit.shape("square");
    fruit.color("red");
    #fruit.shapesize(5,5,20)
    fruit.penup();
    time_signal();
#---------------------------------



#------señal tiempo----------------
def time_signal():
    signaltime.clear();
    signaltime.speed(0);
    signaltime.color("black");
    signaltime.penup();
    signaltime.goto(-130, 250); 
    signaltime.write("Tiempo restante: 3:00", align="center", font=("Courier", 24, "normal")) 
    mvtos_signal();
#----------------------------------


#------señal de mvtos-------------
def mvtos_signal():
    mvtosignal.clear();
    mvtosignal.speed(0);
    mvtosignal.shape("square");
    mvtosignal.color("black");
    mvtosignal.penup();
    mvtosignal.goto(-195, 220);
    mvtosignal.write("Movimientos: 0", align="center", font=("Courier", 24, "normal")) 
    winsignal.hideturtle();
    losesignal.hideturtle();
    signaltime.hideturtle();
    mvtosignal.hideturtle();
    objects_position();
#---------------------------------



#-----posicionamiento--------------
def objects_position():
    snakeX = random.randint(0, 250);
    snakeY = random.randint(0, 250);
    fruitX = random.randint(-250, 0);
    fruitY = random.randint(-250, 0);
    snake.goto(snakeX, snakeY);
    fruit.goto(fruitX, fruitY); 
    winsignal.goto(0, 0);
    losesignal.goto(0, 0);
    instructions(); 
#-----------------------------------



#----------instrucciones------------
def instructions():
    instrucciones = screen.textinput("Instrucciones:","Las instrucciones para el juego son las siguientes:\n1.Debe coger las frutas de color rojo para poder agrandar de tamaño\n2.No puede tocar los bordes de la ventana ni tocar los obstaculos que van saliendo con el tiempo.\n3.Si completalos 3 minutos dejuego, automaticamente gana.\n\nEntendio las instrucciones:\n1.Si\n2.No");
    if instrucciones == "1":
        snake_move()
    elif instrucciones == "si":
        threading.Thread(target=time_remaining).start()
        threading.Thread(target=snake_move).start()
    elif instrucciones == "2":
        exit();
    elif instrucciones == "no":
        exit();            
#-----------------------------------



#---------movimiento snake----------
def snake_move():
    suma = 0;
    x = 1;
    winsignal.clear();
    losesignal.clear();
    while True:
        movimiento = int(screen.textinput("Menú de opciones:", "1.Adelante\n2.Atras\n3.Giro izquierda\n4.Giro derecha"));
        
        if movimiento == 1:
            snake_up();
        elif movimiento == 2:
            snake_down();
        elif movimiento == 3:
            snake_left();
        elif movimiento == 4:
            snake_right();   
        elif movimiento >4:
            snake_move();
        suma = snake_moves_remaining(suma);   
        x = border_colicion(x);
        
#----------------------------------



#----------direcciones----------------
def snake_up():
    distancia = int(screen.textinput("Distancia snake:", "Cuanta es la distancia la cual desea que recorra la snake."));
    snake.forward(distancia);

def snake_down():
    distancia = int(screen.textinput("Distancia snake:", "Cuanta es la distancia la cual desea que recorra la snake."));
    snake.backward(distancia);

def snake_left():
    distancia = int(screen.textinput("Radio del giro:", "Cuantos grados desea que gire la snake."));
    snake.left(distancia); 

def snake_right():
    distancia = int(screen.textinput("Radio del giro:", "Cuantos grados desea que gire la snake."));
    snake.right(distancia);
#-------------------------------------


#--------------reiniciar juego----------------------------
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
        time_signal();
    elif respuesta == "si":
        time_signal();
    elif respuesta == "Si":
        time_signal();
    elif respuesta == "sI":
        time_signal();
    elif respuesta == "SI":
        time_signal();                    
#------------------------------------


#-----------señales de winner/lose----------
def win_signal():
    winsignal.speed(0);
    winsignal.shape("square");
    winsignal.color("black");
    winsignal.penup();
    winsignal.hideturtle() #volver la tortuga invisible.
    winsignal.write("¡WINNER!", align="center", font=("Courier", 30, "normal")) 
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



#---------sumade mvtos---------------
def snake_moves_remaining(suma):
    suma = suma +1;
    mvtosignal.clear();
    mvtosignal.write("Movimientos: {}".format(suma), align="center", font=("Courier", 24, "normal")); 
    if suma % 7 == 0:
        changecolor();
        create_object();
    return suma;
#-----------------------------------


#---------changecolor---------------
def changecolor():
    coloresf = ["yellow","white", "#3DF5F8"];
    coloreso = ["red","blue","green","purple","orange"];
    screen.bgcolor(coloresf[random.randint(0, 2)]);
    snake.color(coloreso[random.randint(0, 3)]);
    fruit.color(coloreso[random.randint(0, 3)]);
#-----------------------------------



#--------crear objeto--------------
def create_object():
    new_segment = Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("red")
    new_segment.penup()
    objectX = random.randint(-250, 250);
    objectY = random.randint(-250, 250);
    new_segment.goto(objectX, objectY); 
    segments2.append(new_segment)
#---------------------------------



#---------colision con bordes-----------
def border_colicion(x):
    if snake.distance(fruit) <20:
        x = x + 8;
        snake.shapesize(1,1,x);
        fruitX = random.randint(-250, 250);
        fruitY = random.randint(-250, 250);
        fruit.goto(fruitX, fruitY);   
        print(x);
    elif snake.xcor()>300 or snake.xcor()<-300 or snake.ycor()>300 or snake.ycor()<-300:
        lose_signal();

    return x;      
#--------------------------------------


#------------reloj----------------
def time_remaining():
    for m in range(0,60):
        for s in range(0,60):
            signaltime.clear();
            signaltime.write("Tiempo restante: {} : {}".format(m,s), align="center", font=("Courier", 24, "normal"));
            time.sleep(1); 

#--------------------------------


#------------main---------------
if __name__ == "__main__":
    main();
#------------------------------    