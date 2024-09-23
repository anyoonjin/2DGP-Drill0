from pico2d import *

open_canvas()

import math

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
ang=0
while(True):
    while(x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x=x+2
        delay(0.01)
    while(y<560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+2
        delay(0.01)
    while(x>20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-2
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-2
        delay(0.01)

close_canvas()
