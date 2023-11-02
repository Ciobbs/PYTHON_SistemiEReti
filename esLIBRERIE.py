import turtle

def disegna_poligono(n, lunghezza_lato):
    angolo = 360 / n
    turtle.pencolor("blue")  # Imposta il colore della linea a blu
    for _ in range(n):
        turtle.forward(lunghezza_lato)
        turtle.right(angolo)

def sposta_a_destra(spazio):
    turtle.penup()
    turtle.forward(spazio)
    turtle.pendown()

turtle.speed(1)
turtle.penup()
turtle.setpos(-600, 0)  # Imposta la posizione al centro dello schermo
turtle.pendown()

spazio_tra_poligoni = 200  # Modifica lo spazio tra i poligoni se necessario

for lati in range(3, 13):
    disegna_poligono(lati, 50)
    sposta_a_destra(spazio_tra_poligoni)

turtle.exitonclick()
