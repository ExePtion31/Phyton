# -*- coding: utf-8 -*-

import turtle as tortuga; #Creamos la tortuga


#-----------------FUNCION MAIN-----------------------
def main():
    tortuga.setup(500,500); #Tamaño de la ventana
    tortuga.title("Juego de espiral"); #Nombre de la ventana
    tortuga.shape("turtle"); #Objeto = tortuga
    tortuga.color("purple");#Color objeto = purpura
    crearespiral(); #Lo mandamos a realizar la función
    tortuga.mainloop(); #No cerrar ventana
#----------------------------------------------------



#---------------------ESPIRAL------------------------
def crearespiral():
    contador = 20; #Largo de las lineas
    for a in range(20): #For para que me repita los 4 pasos del espiral
        for item in range(3): #For para realizar las tres lineas visibles
                tortuga.forward(contador);
                tortuga.left(90);
                contador = contador + 5; #Contador para que cada vez las lineas sean mas largas

        linea_invisible(contador); #Realizamos la funcion de la linea invisible
        contador = contador + 5;

def linea_invisible(contador): 
    contador = contador + 1;
    tortuga.penup();
    tortuga.forward(contador);
    tortuga.left(90);
    tortuga.pendown();           
#----------------------------------------------------



#---------------------MAIN---------------------------
if __name__ == "__main__":
    main(); #Realizamos el metodo main 
#----------------------------------------------------