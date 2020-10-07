# -*- coding: utf-8 -*-
from turtle import *
import random
import winsound
import time

screen = Screen();
frog = Turtle();
car1 = Turtle();
car2 = Turtle();
car3 = Turtle();
tronco1 = Turtle();
tronco2 = Turtle();
tronco3 = Turtle();
winsignal = Turtle();
losesignal = Turtle();
level = Turtle();
carretera = Turtle();
waterlevel = Turtle();
casa1 = Turtle();
casa2 = Turtle();
casa3 = Turtle();
temporizador = Turtle();
#---------metodo main----------
def main():
    configGame();
#------------------------------

#---------config game----------
def configGame():
    global Nlevel;
    Nlevel = 1;
    winsignal.clear();
    losesignal.clear();

    picture_files = ['rana.gif','coche.gif','carretera.gif','fondo2.gif','tronco.gif', 'casa.gif']
    for i in picture_files:
        screen.register_shape(i) 

    screen_settings();
    ShowHigway();
    ShowWater();
    ShowHouse();
    car_settings();
    wood_settings();
    frog_setting();
    ShowLevel();
    timer();
    

    #frog keys
    screen.onkeypress(frog_moveup,"Up");
    screen.onkeypress(frog_movedown,"Down");
    screen.onkeypress(frog_moveleft,"Left");
    screen.onkeypress(frog_moveright,"Right");
    screen.listen();
    while True:

        if frog.distance(casa1) < 40:
            Nlevel = Nlevel + 1;
            next_level(Nlevel);
            
        elif frog.distance(casa2) < 40:
            Nlevel = Nlevel + 1;
            next_level(Nlevel);
            
        elif frog.distance(casa3) < 40:
            Nlevel = Nlevel + 1;
            next_level(Nlevel);

        moveCars();
        collitions_cars();
        moveWood();     
    
    screen.mainloop();
#------------------------------

#-------screen settings---------
def screen_settings():
    screen.setup(800,600);
    screen.title("Game Pong 2020");
    screen.bgpic("fondo.gif")
    respuesta = screen.textinput("Inicio","¡Bienvenido al juego de Rana Frogger!\n\nA continuación, las instrucciones del juego:\n1. Tenga cuidado con los coches, si es atropeyado por uno, perderá\n2. Cada vez que llegue a la meta, subira de nivel.\n3. Por cada nivel superado, los obstacular tendran mas velocidad.\n\nTECLAS:\nPlayer 1: W(Arriba) S(Abajo)\n\nSi entendio las reglas, escriba 'Ok' y si quiere salir, pulse 'Cancelar'.");
    
    if respuesta == None:
        exit();
    elif respuesta != "ok":
        exit();        
#------------------------------

#-----------timer-------------
def timer():
    temporizador.clear();
    temporizador.speed(0);
    temporizador.shape("square");
    temporizador.color("white");
    temporizador.penup();
    temporizador.hideturtle() 
    for i in range(4):
        temporizador.clear();
        temporizador.write("El juego inicia en: {}".format(3-i), align="center", font=("comic sans",40,"bold"));
        time.sleep(1); 
    temporizador.clear();    
#----------------------------


#-------frog settings---------
def frog_setting():
    frog.s = 'rana.gif'
    frog.shape(frog.s)
    frog.up()
    frog.speed(0)
    frog.goto(0, -250)
    frog.jump = 'ready'
#------------------------------

#-------car settings---------
def car_settings():
    #coche 1
    car1.s = 'coche.gif'
    car1.shape(car1.s)
    car1.up()
    car1.speed(0)
    car1.goto(-360, -150)
    car1.jump = 'ready'
    car1.dx = 2;

    #coche2
    car2.shape(car1.s)
    car2.up()
    car2.speed(0)
    car2.goto(360, -100)
    car2.dx = 2;
    car2.jump = 'ready'

    #coche3
    car3.shape(car1.s)
    car3.up()
    car3.speed(0)
    car3.goto(-360, -50)
    car3.dx = 2;
    car3.jump = 'ready'
#------------------------------

#-------show highway----------
def ShowHigway():
    carretera.s = 'carretera.gif'
    carretera.shape(carretera.s)
    carretera.up()
    carretera.speed(0)
    carretera.goto(0, -100)
    carretera.jump = 'ready'
#-----------------------------

#-------show water----------
def ShowWater():
    waterlevel.s = 'fondo2.gif'
    waterlevel.shape(waterlevel.s)
    waterlevel.up()
    waterlevel.speed(0)
    waterlevel.goto(0, 150)
    waterlevel.jump = 'ready'
#-----------------------------

#-------show house----------
def ShowHouse():
    #casa 1
    casa1.s = 'casa.gif';
    casa1.shape(casa1.s)
    casa1.up()
    casa1.speed(0)
    casa1.goto(-360, 275)
    casa1.jump = 'ready'

    #casa 2
    casa2.shape(casa1.s)
    casa2.up()
    casa2.speed(0)
    casa2.goto(0, 275)
    casa2.jump = 'ready'

    #casa 3
    casa3.shape(casa1.s)
    casa3.up()
    casa3.speed(0)
    casa3.goto(360, 275)
    casa3.jump = 'ready'
#-----------------------------

#--------showlevel---------
def ShowLevel():
    level.clear();
    level.color("white");
    level.penup();
    level.hideturtle();
    level.shape("square");
    level.goto(0, 250)
    level.write("Nivel: 1", align="center", font=("comic sans",30,"bold"));

#------------------------------

#----------wood settings-------
def wood_settings():
    #tronco 1
    tronco1.s = 'tronco.gif'
    tronco1.shape(tronco1.s)
    tronco1.up()
    tronco1.speed(0)
    tronco1.goto(360, 70)
    tronco1.jump = 'ready'
    tronco1.dx = 2;

    #tronco 2
    tronco2.shape(tronco1.s)
    tronco2.up()
    tronco2.speed(0)
    tronco2.goto(-360, 150)
    tronco2.dx = 2;
    tronco2.jump = 'ready'

    #tronco 3
    tronco3.shape(tronco1.s)
    tronco3.up()
    tronco3.speed(0)
    tronco3.goto(360, 230)
    tronco3.dx = 2;
    tronco3.jump = 'ready'
#-----------------------------
#-----move cars--------------
def moveCars():
    car1.setx(car1.xcor() + car1.dx)
    if car1.xcor() >= 380:
        car1.dx *= -1;
    elif car1.xcor() <= -380:
        car1.dx *= -1;    

    car2.setx(car2.xcor() + car2.dx)
    if car2.xcor() >= 380:
        car2.dx *= -1;
    elif car2.xcor() <= -380:
        car2.dx *= -1;    

    car3.setx(car3.xcor() + car3.dx)
    if car3.xcor() >= 380:
        car3.dx *= -1;
    elif car3.xcor() <= -380:
        car3.dx *= -1;         
        
#----------------------------

#--------Collitions cars------
def collitions_cars():
    if frog.distance(car1) < 40:
        lose_signal();
    elif frog.distance(car2) < 40:
        lose_signal();  
    elif frog.distance(car3) < 40:
        lose_signal();        
#----------------------------

#--------move wood-----------
def moveWood():
    tronco1.setx(tronco1.xcor() + tronco1.dx)
    if tronco1.xcor() >= 380:
        tronco1.dx *= -1;
    elif tronco1.xcor() <= -380:
        tronco1.dx *= -1;    

    tronco2.setx(tronco2.xcor() + tronco2.dx)
    if tronco2.xcor() >= 380:
        tronco2.dx *= -1;
    elif tronco2.xcor() <= -380:
        tronco2.dx *= -1;    

    tronco3.setx(tronco3.xcor() + tronco3.dx)
    if tronco3.xcor() >= 380:
        tronco3.dx *= -1;
    elif tronco3.xcor() <= -380:
        tronco3.dx *= -1;         
#----------------------------


#-----------señale lose----------
def lose_signal():
    losesignal.speed(0);
    losesignal.color("white");
    losesignal.penup();
    losesignal.hideturtle() #volver la tortuga invisible.
    losesignal.write("¡GAME OVER!", align="center", font=("Courier", 30, "bold")) 
    continue_game();
#-------------------------------------


#---------next level-------------
def next_level(Nlevel):
    level.clear();
    level.write("Nivel: {}".format(Nlevel), align="center", font=("comic sans",30,"bold"));
    winsignal.clear();
    changelevel();
    frog.hideturtle();
    frog.goto(0,-250);
    frog.showturtle(); 
#-------------------------------
    
#-------changelevel-------
def changelevel():
    car1.dx = car1.dx + 1;
    car2.dx = car2.dx - 1;
    car3.dx = car3.dx + 1;
    tronco1.dx = tronco1.dx - 1;
    tronco2.dx = tronco2.dx + 1;
    tronco3.dx = tronco3.dx - 1;
#-------------------------

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
        configGame();
    elif respuesta == "si":
        configGame();
    elif respuesta == "Si":
        configGame();
    elif respuesta == "sI":
        configGame();
    elif respuesta == "SI":
        configGame();                   
#------------------------------------


#--------frog_moveUp--------
def frog_moveup():
    positionracketp1_y = frog.ycor();
    positionracketp1_y = positionracketp1_y + 5;
    frog.sety(positionracketp1_y);
#------------------------------

#--------frog_moveDown--------
def frog_movedown():
    positionracketp1_y = frog.ycor();
    positionracketp1_y = positionracketp1_y - 5;
    frog.sety(positionracketp1_y);
#------------------------------

#--------frog_moveLeft--------
def frog_moveleft():
    positionracketp1_y = frog.xcor();
    positionracketp1_y = positionracketp1_y - 5;
    frog.setx(positionracketp1_y);
#------------------------------

#--------frog_moveRight--------
def frog_moveright():
    positionracketp1_y = frog.xcor();
    positionracketp1_y = positionracketp1_y + 5;
    frog.setx(positionracketp1_y);
#------------------------------


#-------main--------------
if __name__ == "__main__":
    main();
#-------------------------    