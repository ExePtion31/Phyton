# -*-coding: utf-8 -*-

from turtle import *
import winsound

screen = Screen();
turtle = Turtle();
racket1 = Turtle();
racket2 = Turtle();
ball = Turtle()
score = Turtle();

#---------metodo main----------
def main():
    configScreen();
#------------------------------

#------config------------------
def configScreen():
    screen.setup(600,400);
    screen.title("Game Pong 2020");
    screen.bgcolor("black");

    global ScoreP1, ScoreP2, ColicionP2;
    ScoreP1 = 0
    ScoreP2 = 0
    ColicionP2 = ball.xcor()-1

    ShowScore();
    racketplayer1();
    racketplayer2()
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
            score.clear();
            score.write("Score Player 1: {} - Score Player 2: {}".format(ScoreP1,ScoreP2), align="center", font=("comic sans",20,"normal"));
            ball.hideturtle();
            ball.goto(0,0);
            ball.showturtle();
        elif ball.xcor() <= -281:
            ball.setx(-281);   
            ScoreP2 = ScoreP2 + 1;
            score.clear();
            score.write("Score Player 1: {} - Score Player 2: {}".format(ScoreP1,ScoreP2), align="center", font=("comic sans",20,"normal"));
            ball.hideturtle();
            ball.goto(0,0);
            ball.showturtle();   

        collition_racket_sound();
        racket_collition();
   
    screen.mainloop();
#--------------------------------

#-------show score------------
def ShowScore():
    score.color("white");
    score.penup();
    score.hideturtle();
    score.shape("square");
    score.goto(0, 160)
    score.write("Score Player 1: 0 - Score Player 2: 0", align="center", font=("comic sans",20,"normal"));

#----------------------------

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

#------ball------------------
def ballgame():
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
        winsound.PlaySound("sonido.mp3",winsound.SND_ASYNC)
        ball.dx *= -1;
    elif ball.xcor() < -250 and (ball.ycor() < racket1.ycor() + 60 and ball.ycor() > racket1.ycor() -60):
        winsound.PlaySound("sonido.mp3",winsound.SND_ASYNC)
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
        
#-------main--------------
if __name__ == "__main__":
    main();
#-------------------------    