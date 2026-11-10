from pico2d import clear_canvas, get_events, load_image, update_canvas
from sdl2 import SDL_KEYDOWN, SDL_QUIT, SDLK_0, SDLK_1, SDLK_2

import game_framework
import game_world
import play_mode


image = None


def init():
    global image
    image = load_image('item_select.png')
    play_mode.boy.set_controls_enabled(False)


def finish():
    global image
    del image
    play_mode.boy.set_controls_enabled(True)


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type != SDL_KEYDOWN:
            continue

        if event.key == SDLK_0:
            play_mode.boy.item = 0
        elif event.key == SDLK_1:
            play_mode.boy.item = 1
        elif event.key == SDLK_2:
            play_mode.boy.item = 2
        else:
            continue

        game_framework.pop_mode()
        return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()
