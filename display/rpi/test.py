# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

from random import randrange
from demo_opts import get_device
from luma.core.render import canvas


def init_stars(num_stars, max_depth):
    stars = []
    for i in range(num_stars):
        star = [randrange(-25, 25), randrange(-25, 25),
                randrange(1, max_depth)]
        stars.append(star)
    return stars


def move_and_draw_stars(stars, max_depth):
    origin_x = device.width // 2
    origin_y = device.height // 2

    with canvas(device) as draw:
        for star in stars:
            star[2] -= 0.19
            if star[2] <= 0:
                star[0] = randrange(-25, 25)
                star[1] = randrange(-25, 25)
                star[2] = max_depth
            k = 128.0 / star[2]
            x = int(star[0] * k + origin_x)
            y = int(star[1] * k + origin_y)
            if 0 <= x < device.width and 0 <= y < device.height:
                size = (1 - float(star[2]) / max_depth) * 4
                if (device.mode == "RGB"):
                    shade = (
                        int(100 + (1 - float(star[2]) / max_depth) * 155),) * 3
                else:
                    shade = "white"
                draw.rectangle((x, y, x + size, y + size), fill=shade)


def main():
    max_depth = 32
    stars = init_stars(512, max_depth)
    while True:
        move_and_draw_stars(stars, max_depth)


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
