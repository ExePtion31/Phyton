# -*- coding: utf-8 -*-
from turtle import *
import random;
import time;
import threading;
from concurrent.futures import ThreadPoolExecutor;
screen = Screen()
tortuga = Turtle();
timeremaining = Turtle();
losesignal = Turtle();
winsignal = Turtle();

preguntas = [
            "Resolver la siguiente integral:\n ∫tanx dx\n\nRespuetas:\nA.-ln senx + C\nB.-ln cosx + C\nC.ln cosx + C\nD.-ln tanx - C",
            "Resolver la siguiente derivada f(x) = 2x^4 + x^3 - x^2 + 4\n\nRespuetas:\nA.f(x) = 8x^3 + 3x^2 - 2x\nB.f(x) = 8x^2 + 4x^2 - x\nC.f(x) = 8x^3 - 3x^2 - 2x\nD.f(x) = 5x^3 - 3x^2 + 2x",
            "¿A qué velocidad debe circular un auto de carreras para recorrer 50km en un cuarto de hora?\n\nRespuestas:\nA.150km/h\nB.180km/h\nC.200km/h\nD.300km/h",
             "Se deja caer un objeto desde la azotea de un edificio que tiene una altura de 12m. ¿En que tiempo toca el piso?\n\nRespuestas:\nA.1,23s\nB.1,90s\nC.2,00s\nD.1,57s",
             "Un jugador de Fútbol Americano patea el balón con una velocidad de 30 m/s, y éste mismo lleva un ángulo de elevación de 48° respecto a la horizontal. Calcule el tiempo que permanece en el aire.\n\nRespuestas:\nA.3,57s\nB.4,55s\nC.6,78s\nD.5,67s"
            ]
respuestas = ["b","a","c","d","b"];

#--------funcion main--------
def main():
    create_screen();
#---------------------------

#------create screen--------
def create_screen():
    screen.title("Juego funciones matematicas")
    create_turtle();
    screen.mainloop();
#---------------------------

#------create turtle--------
def create_turtle():
    tortuga.shape("turtle");
    tortuga.color("green");
    tortuga.penup();
    time_signal();
#---------------------------

#------time remaining-------
def time_signal():
    timeremaining.speed(0);
    timeremaining.penup();
    timeremaining.hideturtle();
    positioning();
#---------------------------

#---------positioning-------
def positioning():
    winsignal.clear();
    losesignal.clear();
    winsignal.hideturtle();
    losesignal.hideturtle();
    tortuga.goto(random.randint(-230, 230), random.randint(-230, 230));
    timeremaining.goto(-200, 240);
    timeremaining.write("Tiempo: 0:00", align="center", font=("Courier", 24, "normal")); 
    instructions();
#---------------------------

#-------instructions-------
def instructions():
    instrucciones = screen.textinput("Instrucciones:","Las instrucciones para el juego son las siguientes:\n1.Debe responder correctamente el problema matematico para poder hacer un movimiento\n2.Si responde mal el problema, el juego finalizara\n\n¿Entendio las instrucciones?\n1.Si\n2.No");
    if instrucciones == "1":
        game_start();
    elif instrucciones == "si":
        executor = ThreadPoolExecutor(max_workers=1);
        executor.submit(time_remaining);
        
    else:
        exit();        
#--------------------------

#------game start----------
def game_start():
    contador = 0;

    while True:
        pregunta = screen.textinput("Pregunta",preguntas[contador]);
        if pregunta == respuestas[contador]:
            contador = contador + 1;
            move_turtle(); 
        else:
            lose_signal();
#-------------------------


#-------move turtle----------
def move_turtle():
    screen.onkeypress(forward_turtle,"Up");
    screen.onkeypress(backward_turtle,"Down");
    screen.onkeypress(left_turtle,"Left");
    screen.onkeypress(right_turtle,"Right");
    screen.listen();
#----------------------------

#-----forward turtle---------
def forward_turtle():
    tortuga.forward(10);
#----------------------------    

#-----backward turtle--------
def backward_turtle():
    tortuga.backward(10);
#----------------------------  

#--------left turtle---------
def left_turtle():
    tortuga.left(10);
#----------------------------  

#-------right turtle---------
def right_turtle():
    tortuga.right(10);
#----------------------------  

#-----------winner/lose signal----------
def win_signal():
    winsignal.speed(0);
    winsignal.shape("square");
    winsignal.color("black");
    winsignal.penup();
    winsignal.hideturtle() #volver la tortuga invisible.
    winsignal.write("¡WINNER!", align="center", font=("Courier", 30, "normal")) 
    restart_game();

def lose_signal():
    losesignal.speed(0);
    losesignal.shape("square");
    losesignal.color("black");
    losesignal.penup();
    losesignal.hideturtle() #volver la tortuga invisible.
    losesignal.write("¡LOSER!", align="center", font=("Courier", 30, "normal")) 
    restart_game();
#-------------------------------------

#--------------restart game----------------------------
def restart_game():
    respuesta = screen.textinput("Desea reiniciar:", "¿Desea reiniciar el juego?:\n1.Si\n2.No");

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
        positioning();
    elif respuesta == "si":
        positioning();
    elif respuesta == "Si":
        positioning();
    elif respuesta == "sI":
        positioning();
    elif respuesta == "SI":
        positioning();                  
#------------------------------------


#------------reloj----------------
def time_remaining():
    for m in range(0,60):
        for s in range(0,60):
            timeremaining.clear();
            timeremaining.write("Tiempo: {} : {}".format(m,s), align="center", font=("Courier", 24, "normal"));
            time.sleep(1); 
            if m==1 and s==0:
                lose_signal();

#--------------------------------


#-------main-------------
if __name__ == "__main__":
   main();
    
#------------------------    