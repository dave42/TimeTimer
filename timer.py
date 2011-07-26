#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys, pygame, numpy
import datetime
pygame.init()

width = height = 640
size = width, height
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

screen = pygame.display.set_mode(size)

# Create 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 in black with background white
font_size=20
font = pygame.font.Font(None, font_size)
numbers = [font.render(str(num), True, black, white) for num in range(0, 60, 5)]
bigfont = pygame.font.Font(None, 100)
paused = bigfont.render("PAUSED", True, red, white)
done = bigfont.render("TIME'S UP", True, red, white)
border_width=40

minutes = int(sys.argv[1])
end_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Draw the clock
    screen.fill(black)
    # White circle, filled
    pygame.draw.ellipse(screen, white, pygame.Rect(0,0,width,height))
    # Black inner circle
    pygame.draw.ellipse(screen,black,pygame.Rect(border_width,border_width,width-border_width*2,height-border_width*2), 3)
    # Mark 60 lines in black on the Circle, bigger ones on the 5 minute intervals
    for tick in range(60):
        big_tick = (tick % 5 == 0)
        tick_x = numpy.sin(tick*numpy.pi/30)
        tick_y = -numpy.cos(tick*numpy.pi/30)
        if big_tick:
            length = 20
        else:
            length = 10
        start_x = tick_x*(width/2-border_width) + width/2
        end_x = tick_x*(width/2-border_width-length) + width/2
        start_y = tick_y*(height/2-border_width) + height/2
        end_y = tick_y*(height/2-border_width-length) + height/2
        pygame.draw.line(screen, black, (start_x, start_y), (end_x, end_y))
    # Place the text on the correct lines
    for tick, ticknum in enumerate(numbers):
        tick_x = -numpy.sin(tick*numpy.pi/6)
        tick_y = -numpy.cos(tick*numpy.pi/6)
        centre_x = tick_x*(width/2-font_size) + width/2
        centre_y = tick_y*(height/2-font_size) + height/2
        _x = centre_x - ticknum.get_width()/2
        _y = centre_y - ticknum.get_height()/2
        screen.blit(ticknum, (_x, _y))
    # Draw the arc in red on the clock
    current_time = datetime.datetime.now()
    if current_time < end_time:
        minutes_left = (end_time - current_time).seconds / 60.0
        angle_start = numpy.pi*minutes_left/30.0 + numpy.pi/2
        pygame.draw.arc(screen, red, pygame.Rect(border_width+20, border_width+20, width-border_width*2-40, width-border_width*2-40), numpy.pi/2, angle_start, width/2-border_width-20)
        pygame.draw.arc(screen, red, pygame.Rect(border_width+20, border_width+20, width-border_width*2-40, width-border_width*2-40), numpy.pi/2-0.01, angle_start-0.01, width/2-border_width-20)
        pygame.draw.arc(screen, red, pygame.Rect(border_width+20, border_width+20, width-border_width*2-40, width-border_width*2-40), numpy.pi/2+0.01, angle_start+0.01, width/2-border_width-20)
    else:
        _x = width/2 - done.get_width()/2
        _y = height/2 - done.get_height()/2
        screen.blit(done, (_x, _y))
    pygame.display.flip()
