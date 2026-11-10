from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}

    def __init__(self, x, y, velocity, item=1):
        image_names = {1: 'ball21x21.png', 2: 'ball41x41.png'}
        if item not in image_names:
            raise ValueError(f'Unsupported ball item: {item}')
        if item not in Ball.images:
            Ball.images[item] = load_image(image_names[item])
        self.image = Ball.images[item]
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
