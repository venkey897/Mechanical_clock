import pygame
from datetime import datetime
import math
res=height,width=800,800
H_width,H_height=width//3,height//3
rad=H_height-50
radious_list={'sec':rad-10,'min':rad-55,'hour':rad-100,'rad':rad+20}
pygame.init()
surface=pygame.display.set_mode(res)
clock=pygame.time.Clock()
clock12=dict(zip(range(12),range(0,360,30)))
clock60=dict(zip(range(60),range(0,360,6)))
def get_clock_pos(clock_dict,clock_hand,k):
    x=H_width+radious_list[k]*math.cos(math.radians(clock_dict[clock_hand])-math.pi/2)
    y=H_height+radious_list[k]*math.sin(math.radians(clock_dict[clock_hand])-math.pi/2)
    return x,y
def numbers(number,size,pos):
     font=pygame.font.SysFont('Arial',size,True,False)
     #tim=font.render(f'{t:%H:%M:%S}',True,pygame.Color('forestgreen'),pygame.Color('Orange'))
     text=font.render(number,True,pygame.Color('WHITE'))
     text_rect=text.get_rect(center=pos)
     surface.blit(text,text_rect)
def polar(r,theta):
    x=r*math.sin(math.pi*theta/180)
    y=r*math.cos(math.pi*theta/180)
    return x+H_width/2,-(y-H_height/2)
    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    surface.fill(pygame.Color('black'))
    t=datetime.now()
    hour,minute,seconds=t.hour%12,t.minute,t.second
    for number,i in clock12.items():
        r=20 if not number%3 and not number%5 else 8 if not number%5 else 2
        if(number==0):
            numbers(str(12),40,get_clock_pos(clock12,number,'rad'))
        else:
            numbers(str(number),40,get_clock_pos(clock12,number,'rad'))
    pygame.draw.circle(surface,pygame.Color('darkslategray'),(H_width,H_height),rad)
    pygame.draw.line(surface,pygame.Color('orange'),(H_width,H_height),get_clock_pos(clock12,hour,'hour'),15)
    pygame.draw.line(surface,pygame.Color('green'),(H_width,H_height),get_clock_pos(clock60,minute,'min'),7)
    pygame.draw.line(surface,pygame.Color('magenta'),(H_width,H_height),get_clock_pos(clock60,seconds,'sec'),4)
    pygame.draw.circle(surface,pygame.Color('white'),(H_width,H_height),8)
    pygame.display.flip()       
    clock.tick(20)
