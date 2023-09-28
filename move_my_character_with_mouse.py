from pico2d import *
import math
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')

idle = [load_image('knight_idle_front.png'),
        load_image('knight_idle_back.png'),
        load_image('knight_idle_front_right.png'),
        load_image('knight_idle_front_left.png')
       ]

run = [load_image('knight_run_front.png'),
       load_image('knight_run_back.png'),
       load_image('knight_run_front_right.png'),
       load_image('knight_run_front_left.png')
       ]
run_frame = [6,6,6,6]
idle_frame = [4,4,4,4]

pos = []

click = []

x = 600
y=500
frame = 0
looking =0

running = True

while (running):
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH / 2, TUK_HEIGHT / 2)
    if len(pos) > 0:
        run[looking].clip_draw(frame * (int(run[looking].w / run_frame[looking])), 0,
                               int(run[looking].w / run_frame[looking]), run[looking].h, x, y,
                               int(run[looking].w / run_frame[looking]) * 4, run[looking].h * 4)
        frame = (frame + 1) % run_frame[looking]
        x, y = pos[0][0], pos[0][1]
        pos.pop(0)
        if len(pos) == 0:
            click.pop(0)
    else:
        idle[looking].clip_draw(frame*(int(idle[looking].w/idle_frame[looking])), 0, int(idle[1].w/idle_frame[looking]), idle[looking].h, x, y,int(idle[1].w/idle_frame[looking])*4, idle[looking].h*4)
        frame = (frame + 1) % idle_frame[looking]
    for i in click:
        hand.draw(i[0],i[1])

    if len(pos) == 0 and len(click) > 0:
        x1, y1 = x, y
        x2, y2 = click[0][0], click[0][1]
        if x1 < x2:
            looking = 2
        else:
            looking = 3
        pos = [((1 - (i / 100)) * x1 + (i / 100) * x2, (1 - (i / 100)) * y1 + (i / 100) * y2) for i in range(0, 100 + 1, 4)]

    update_canvas()
    delay(0.05)
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            click.append((event.x, TUK_HEIGHT - event.y))

close_canvas()