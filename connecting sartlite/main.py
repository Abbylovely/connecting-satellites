import pgzrun
from random import randint
WIDTH=800
HEIGHT=600
TITLE="connecting satellites"
no_of_sat=8
satellites=[]
next_sat=0
def creat_sat():
    for i in range(no_of_sat):
        sat=Actor("sat")
        sat.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(sat)
def draw():
    screen.blit("bg",(0,0))
    number=1
    for i in satellites:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number=number+1

def update():
    pass
def on_mouse_down(pos):
   if next_sat <no_of_sat:
       if
creat_sat()
pgzrun.go()