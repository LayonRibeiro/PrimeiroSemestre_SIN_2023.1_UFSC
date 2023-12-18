import turtle
import math

baga = turtle.Turtle()
baga.speed(100)

baga.up()
baga.left(90)
baga.fd(200)
baga.right(90)

def olhos(baga,color):
    d = 50
    r = 25
    #faz a parte colorida do olho e volta para o centro
    baga.dot(d,"yellow")
    baga.up()
    baga.forward(d)
    baga.dot(d,"yellow")
    baga.backward(r)
    baga.down()
    baga.right(90)

    # circulos envolta da parte colorida do olho
    for r in range (r,4*r,r):
        baga.circle(r,360)
        baga.left(180)
        baga.circle(r,360)
    
def nariz(baga,color): 
# nariz do palhaço
    l=50
    baga.up()
    baga.bk(200)
    baga.down()
    baga.color("magenta")
    for i in range(30):
        baga.fd(l)
        baga.bk(2*l)
        baga.fd(l)
        baga.left(6)

def boca(baga, color):
    #desloca para fazer a boca
    baga.color("red")
    baga.up()
    baga.fd(150)
    baga.width(6)
    baga.left(90)
    baga.down()

    #faz a boca
    x=30
    z= 360-(2*x)
    baga.circle(180,x)
    baga.up()
    baga.circle(180,z)
    baga.down()
    baga.circle(180,x)

olhos(baga, "color")
nariz(baga, "color")
boca(baga,"color")


turtle.done()
