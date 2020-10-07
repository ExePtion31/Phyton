#-*-coding: utf-8-*-

from turtle import *
import winsound
import random
import time

screen = Screen();
racket1 = Turtle();
racket2 = Turtle();
ball = Turtle()
winsignal = Turtle();
score = Turtle();
level = Turtle();
temporizador = Turtle()

#---------metodo main----------
def main():
    configGame();
#------------------------------

#------config------------------
def configGame  ():
    global ScoreP1, ScoreP2, Nlevel;
    ScoreP1 = 0
    ScoreP2 = 0
    Nlevel = 1;

    screen_settings()
    ShowScore();
    ShowLevel();
    racketplayer1();
    racketplayer2()
    timer();
    ballgame();
    
    #racket 1 keys
    screen.onkeypress(racket1_moveup,"w");
    screen.onkeypress(racket1_movedown,"s");
    #racket 2 keys
    screen.onkeypress(racket2_moveup,"Up");
    screen.onkeypress(racket2_movedown,"Down");
    screen.listen();
    
    while True:
        moveBall();

        #----collition up/down
        if ball.ycor() >= 181:
            ball.sety(181);
            ball.dy = ball.dy * (-1)
        elif ball.ycor() <= -181:
            ball.sety(-181);
            ball.dy = ball.dy * (-1)

        #-----collition left/right    
        elif ball.xcor() >= 281:
            ScoreP1 = ScoreP1 + 1;
            if ScoreP1 % 5 == 0:
                Nlevel = Nlevel + 1;
                changecolor();
                changelevel(Nlevel);
            score.clear();
            score.write("Score Player 1: {} - Score Player 2: {}".format(ScoreP1,ScoreP2), align="center", font=("comic sans",20,"normal"));
            ball.hideturtle();
            ball.goto(0,0);
            ball.showturtle();
        elif ball.xcor() <= -281:  
            ScoreP2 = ScoreP2 + 1;
            if ScoreP2 % 5 == 0:
                Nlevel = Nlevel + 1;
                changecolor();
                changelevel(Nlevel);
            score.clear();
            score.write("Score Player 1: {} - Score Player 2: {}".format(ScoreP1,ScoreP2), align="center", font=("comic sans",20,"normal"));
            ball.hideturtle();
            ball.goto(0,0);
            ball.showturtle();   

        collition_racket_sound();
        racket_collition();
        Game_Winner(ScoreP1,ScoreP2,Nlevel);
        
    
    screen.mainloop();
#--------------------------------

#-------screen settings---------
def screen_settings():
    screen.setup(600,400);
    screen.title("Game Pong 2020");
    screen.bgcolor("black");
    respuesta = screen.textinput("Inicio","¡Bienvenido al juego de Pong 2020!\n\nA continuación, las instrucciones del juego:\n1. Existiran dos jugadores\n2. Si la pelota pasa la raqueta, habrá punto para el jugador contrario.\n3. A los 5 puntos anotados, se subira de nivel.\n4. Cada nivel los colores cambiarán y la pelota va mas rapido.\n5. Al nivel 10, el juego terminará y ganará el jugador con mas puntos.\n\nTECLAS:\nPlayer 1: W(Arriba) S(Abajo)\nPlayer 2: ↑(Arriba) ↓(Abajo)\n\nSi entendio las reglas, escriba 'Ok' y si quiere salir, pulse 'Cancelar'.");
    
    if respuesta == None:
        exit();
    elif respuesta != "ok":
        exit();        
#------------------------------

#-------show score-------------
def ShowScore():
    score.clear();
    score.color("white");
    score.penup();
    score.hideturtle();
    score.shape("square");
    score.goto(0, 160)
    score.write("Score Player 1: 0 - Score Player 2: 0", align="center", font=("comic sans",20,"normal"));

#------------------------------

#-------show level-------------
def ShowLevel():
    level.clear();
    level.color("white");
    level.penup();
    level.hideturtle();
    level.shape("square");
    level.goto(0, -190)
    level.write("Nivel: 1", align="center", font=("comic sans",20,"normal"));

#------------------------------

#------racketplayer1------------------
def racketplayer1():
    racket1.shape("square");
    racket1.color("red");
    racket1.shapesize(7, 1)
    racket1.penup();
    racket1.goto(-270,0);
#------------------------------

#------racketplayer2------------------
def racketplayer2():
    racket2.shape("square");
    racket2.color("red");
    racket2.shapesize(7, 1)
    racket2.penup();
    racket2.goto(270,0);
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
        temporizador.write("El juego inicia en: {}".format(3-i), align="center", font=("comic sans",20,"normal"));
        time.sleep(1); 
#----------------------------

#------ball------------------
def ballgame():
    temporizador.clear();
    ball.shape("circle");
    ball.color("red");
    ball.goto(0,0);
    ball.penup();
    ball.dx = 2
    ball.dy = 2
#------------------------------

#--------racket1_moveUp--------
def racket1_moveup():
    positionracketp1_y = racket1.ycor();
    positionracketp1_y = positionracketp1_y + 5;
    racket1.sety(positionracketp1_y);
#------------------------------

#--------racket1_moveDown--------
def racket1_movedown():
    positionracketp1_y = racket1.ycor();
    positionracketp1_y = positionracketp1_y - 5;
    racket1.sety(positionracketp1_y);
#------------------------------

#--------racket2_moveUp--------
def racket2_moveup():
    positionracketp2_y = racket2.ycor();
    positionracketp2_y = positionracketp2_y + 5;
    racket2.sety(positionracketp2_y);
#------------------------------

#--------racket2_moveDown--------
def racket2_movedown():
    positionracketp2_y = racket2.ycor();
    positionracketp2_y = positionracketp2_y - 5;
    racket2.sety(positionracketp2_y);
#------------------------------

#--------sound ball---------
def collition_racket_sound():
    if ball.xcor() > 250 and (ball.ycor() < racket2.ycor() + 60 and ball.ycor() > racket2.ycor() -60):
        winsound.PlaySound("sound.MP3", winsound.SND_ASYNC)
        ball.dx *= -1;
    elif ball.xcor() < -250 and (ball.ycor() < racket1.ycor() + 60 and ball.ycor() > racket1.ycor() -60):
        winsound.PlaySound("sound", winsound.SND_ASYNC)
        ball.dx *= -1;
#---------------------------

#-----racket collition------
def racket_collition():
    if racket1.ycor() >= 122:         #racket 1 collition Top
        racket1.sety(122)
    elif racket1.ycor() <= -125:       #racket 1 collition Button
        racket1.sety(-122)
    if racket2.ycor() >= 122:          #racket 2 collition Top
        racket2.sety(122)
    elif racket2.ycor() <= -125:       #racket 2 collition Button
        racket2.sety(-122)
#---------------------------

#-----move ball--------------
def moveBall():
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() - ball.dy )
#----------------------------

#--------changecolor--------
def changecolor():
    coloreso = ["red","green","purple"];
    racket1.color(coloreso[random.randint(0, 2)]);
    racket2.color(coloreso[random.randint(0, 2)]);
    ball.color(coloreso[random.randint(0, 2)]);
#--------------------------    

#-------changelevel-------
def changelevel(Nlevel):
    level.clear();
    level.write("Nivel: {}".format(Nlevel), align="center", font=("comic sans",20,"normal"));
    ball.dx = ball.dx + 1;
    ball.dy = ball.dy + 1;
#-------------------------


#---------game winner------
def Game_Winner(ScoreP1,ScoreP2,Nlevel):
    if Nlevel == 10:
        if(ScoreP1 > ScoreP2):
            winner = "Player 1";
            win_signal(winner)
        else:
            winner = "Player 2";
            win_signal(winner);
#--------------------------


#-----------winner signal----------
def win_signal(winner):
    winsignal.clear();
    winsignal.speed(0);
    winsignal.shape("square");
    winsignal.color("black");
    winsignal.penup();
    winsignal.hideturtle() 
    winsignal.write("Ganador: {}".format(winner), align="center", font=("comic sans",20,"normal"));
    continue_game();
#---------------------------------


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
        main();
    elif respuesta == "si":
        main();
    elif respuesta == "Si":
        main();
    elif respuesta == "sI":
        main();
    elif respuesta == "SI":
        main();                    
#------------------------------------


#-------main--------------
if __name__ == "__main__":
    main();
#-------------------------    