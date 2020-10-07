# -*-coding: utf-8 -*-

from turtle import *
screen = Screen();
turtle = Turtle();

#---------metodo main----------
def main():
    config();
#------------------------------

#------config------------------
def config():
    screen.setup(500,500);
    screen.title("Juego con teclado");
    screen.bgcolor("green");
    configpj();
    screen.mainloop();
#------------------------------

#---------configpj-------------    
def configpj():
    turtle.shape("turtle");
    turtle.color("red");
    turtle.penup();
    turtle.goto(-200, -200);
    turtle.seth(90);
    turtle.pendown();
    move_turtle();
#-----------------------------


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
    turtle.forward(10);
#----------------------------    

#-----backward turtle--------
def backward_turtle():
    turtle.backward(10);
#----------------------------  

#--------left turtle---------
def left_turtle():
    turtle.left(10);
#----------------------------  

#-------right turtle---------
def right_turtle():
    turtle.right(10);
#----------------------------  


#-------main--------------
if __name__ == "__main__":
    main();
#-------------------------    