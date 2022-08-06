from curses import window
import turtle # importo modulo turtle

def make_window(bgk_color, title):
    '''
    Crea una finestra con background e titolo e ritorna la nuova finestra
    '''
    window = turtle.Screen() # creo una finestra dove lavorare
    window.bgcolor(bgk_color) # cambio il colore della finestra in verde
    window.title(title)
    return window

def make_turtle(pen_color, pen_size):
    '''
    Create a turtle with the given color and pensize. Returns the new turtle
    '''
    my_turtle = turtle.Turtle() # creo la tartaruga
    my_turtle.color(pen_color) # definisco il colore
    my_turtle.pensize(pen_size) # e lo spessore
    return my_turtle

def draw_square(my_turtle, steps):
    '''
    Faccio disegnare alla mia tartaruga un quadrato di lato steps
    '''
    for i in range(4): # occhio che il 4 è escluso!! i sarà 0,1,2,3  utilizzo di range(start, stop_escluso, step)
         
        my_turtle.forward(steps) # dico a raffaello di andare avanti di 50 passi
        my_turtle.left(90) # gira a sinsitra di 90 gradi

def draw_triangle(my_turtle):
    '''
    Faccio disegnare alla mia tartaruga un triangolo
    '''
    for i in range(3): # occhio che il 4 è escluso!! i sarà 0,1,2 
    # utilizzo di range(start, stop_escluso, step)
        my_turtle.forward(80)
        my_turtle.left(120)

def koch(my_turtle, order, size):
    '''
    La tartaruga disegna il frattale di kch di order e size. 
    '''
    if order == 0 :
        my_turtle.forward(size)
    else:
        for angle in [60,-120, 60, 0]:
            koch(my_turtle , order-1, size/3)
            my_turtle.left(angle)


#### MAIN ####

window = make_window('green','Raffaello & Donatello')
raffaello = make_turtle('red', 5)
donatello = make_turtle('violet', 2)

#draw_square(raffaello,50)
#draw_triangle(donatello)
koch(raffaello, 3, 100)


window.mainloop() # attende che utente chiuda la finestra di gioco

