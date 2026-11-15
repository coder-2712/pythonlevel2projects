
import turtle
from datetime import datetime as dt, timedelta
from math import sin, pi
import random

# its supposed to be synced to real time but i added a a part that can speed it up so that the animation is visible, thats why its 720x.

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.colormode(255)
screen.tracer(0)

width = screen.window_width()
height = screen.window_height()


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

cloud = turtle.Turtle()
cloud.hideturtle()
cloud.speed(0)
cloud.penup()

sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)
sun.penup()

star_pen = turtle.Turtle()
star_pen.hideturtle()
star_pen.speed(0)
star_pen.penup()

grounddraw = turtle.Turtle()
grounddraw.hideturtle()
grounddraw.speed(0)
grounddraw.penup()

moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
moon.penup()

bgdraw = turtle.Turtle()
bgdraw.hideturtle()
bgdraw.speed(0)
bgdraw.penup()

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def blend_colour(colour1, colour2, t):

    red = int(colour1[0] + (colour2[0] - colour1[0]) * t)
    green = int(colour1[1] + (colour2[1] - colour1[1]) * t)
    blue = int(colour1[2] + (colour2[2] - colour1[2]) * t)

    return (red, green, blue)


night = [
    (55, 64, 91), (51, 60, 87), (47, 56, 83),
    (43, 52, 79), (39, 48, 76), (35, 44, 72),
    (32, 41, 69), (29, 38, 66), (26, 35, 63),
    (24, 33, 60), (22, 31, 57), (20, 29, 54),
    (18, 27, 51), (16, 24, 47), (13, 21, 43)
]

morning = [
    (255, 195, 155), (255, 190, 151), (255, 184, 148),
    (252, 178, 150), (246, 173, 157), (237, 169, 169),
    (222, 166, 187), (203, 165, 204), (181, 164, 218),
    (158, 164, 225), (137, 161, 225), (119, 155, 219),
    (104, 145, 208), (91, 132, 194), (79, 117, 177)
]

day = [
    (155, 222, 255), (147, 218, 255), (139, 214, 255),
    (130, 209, 255), (120, 203, 255), (110, 197, 255),
    (100, 190, 252), (91, 183, 249), (82, 176, 246),
    (74, 169, 242), (67, 162, 238), (62, 155, 234),
    (57, 148, 230), (53, 142, 226), (49, 136, 222)
]

sunset = [
    (255, 187, 130), (255, 178, 120), (255, 166, 113),
    (251, 152, 112), (245, 137, 117), (237, 123, 125),
    (225, 110, 135), (210, 99, 143), (192, 91, 148),
    (172, 85, 149), (151, 79, 145), (129, 73, 137),
    (107, 67, 125), (84, 60, 109), (62, 53, 91)
]


def draw_sky(colours):

    pen.clear()

    strips = 600
    strip_height = height / strips + 1

    for i in range(strips):

        position = i / (strips - 1)
        segment = position * (len(colours) - 1)
        index = int(segment)

        if index >= len(colours) - 1:
            index = len(colours) - 2

        t = segment - index

        colour = blend_colour(
            colours[index],
            colours[index + 1],
            t
        )

        y = -height / 2 + i * strip_height

        pen.goto(-width / 2, y)
        pen.color(colour)
        pen.begin_fill()

        pen.goto(width / 2, y)
        pen.goto(width / 2, y + strip_height)
        pen.goto(-width / 2, y + strip_height)
        pen.goto(-width / 2, y)

        pen.end_fill()

sky_keyframes = [
    (0, night),
    (270, night),
    (360, morning),
    (480, day),
    (960, day),
    (1080, sunset),
    (1200, night),
    (1440, night)
]


def get_sky_colours(game_time):

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )

    for i in range(len(sky_keyframes) - 1):

        starttime, start_colours = sky_keyframes[i]
        end_time, end_colours = sky_keyframes[i + 1]

        if starttime <= minutes < end_time:

            t = (minutes - starttime) / (end_time - starttime)

            new_colours = []

            for colour1, colour2 in zip(start_colours, end_colours):

                colour = blend_colour(colour1, colour2, t)
                new_colours.append(colour)

            return new_colours

    return night

stars = []

random.seed(42)

for i in range(100):

    x = random.randint(int(-width / 2 + 20), int(width / 2 - 20))
    y = random.randint(int(-height / 2 + 50), int(height / 2 - 20))

    size = random.choice([2, 2, 3, 3, 4])

    stars.append((x, y, size))


def staropacity(game_time):

    minutes = game_time.hour * 60 + game_time.minute + game_time.second / 60

    if 18 * 60 + 30 <= minutes < 19 * 60:
        return (minutes - (18 * 60 + 30)) / 30

    elif minutes >= 19 * 60 or minutes < 4 * 60:
        return 1

    elif 4 * 60 <= minutes < 4 * 60 + 30:
        return 1 - ((minutes - 4 * 60) / 30)

    return 0


def draw_stars(game_time, sky_colours):

    star_pen.clear()

    opacity = staropacity(game_time)

    if opacity <= 0:
        return

    for x, y, size in stars:

        position = (y + height / 2) / height

        segment = position * (len(sky_colours) - 1)
        index = min(int(segment), len(sky_colours) - 2)
        t = segment - index

        background = blend_colour(
            sky_colours[index],
            sky_colours[index + 1],
            t
        )

        star_colour = blend_colour(
            background,
            (255, 255, 255),
            opacity
        )

        star_pen.goto(x, y)
        star_pen.dot(size, star_colour)


cloud_shape_1 = [
    ".....####.....",
    "...########...",
    "..##########..",
    ".############.",
    "##############",
    "##############",
    "..##########.."
]

cloud_shape_2 = [
    "....######....",
    "..##########..",
    ".############.",
    "##############",
    "##############",
    "##############",
    "..##########.."
]


cloud_keyframes = [
    (0, ((125, 145, 180), (75, 95, 135))),
    (270, ((125, 145, 180), (75, 95, 135))),
    (360, ((255, 220, 195), (220, 145, 150))),
    (480, ((255, 255, 255), (190, 215, 235))),
    (960, ((255, 255, 255), (190, 215, 235))),
    (1080, ((255, 215, 180), (205, 130, 155))),
    (1200, ((125, 145, 180), (75, 95, 135))),
    (1440, ((125, 145, 180), (75, 95, 135)))
]


def get_cloud_colours(game_time):

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )

    for i in range(len(cloud_keyframes) - 1):

        starttime, start_colours = cloud_keyframes[i]
        end_time, end_colours = cloud_keyframes[i + 1]

        if starttime <= minutes < end_time:

            t = (minutes - starttime) / (end_time - starttime)

            highlight = blend_colour(
                start_colours[0],
                end_colours[0],
                t
            )

            shadow = blend_colour(
                start_colours[1],
                end_colours[1],
                t
            )

            return highlight, shadow

    return cloud_keyframes[0][1]


clouds = [
    [-width * 0.35, height * 0.27, 1.0, 0.8, 1, 1],
    [width * 0.15, height * 0.38, 0.75, 0.7, 2, -1],
    [width * 0.65, height * 0.22, 1.2, 0.85, 1, -1],
    [-width * 0.85, height * 0.40, 0.9, 0.75, 2, 1]
]


def draw_pixel_cloud(x, y, scale, shade, design, highlight, shadow):

    pixel_size = 9 * scale

    if design == 1:
        shape = cloud_shape_1
    else:
        shape = cloud_shape_2

    white = blend_colour(
        (65, 75, 95),
        highlight,
        shade
    )

    dark_shadow = blend_colour(
        (35, 45, 70),
        shadow,
        shade
    )

    for row, line in enumerate(shape):

        for col, pixel in enumerate(line):

            if pixel == "#":

                px = x + (col - len(line) / 2) * pixel_size
                py = y + (len(shape) - 1 - row) * pixel_size


                if row >= len(shape) - 2:
                    cloud.color(dark_shadow)
                else:
                    cloud.color(white)

                cloud.goto(px, py)
                cloud.begin_fill()

                cloud.goto(px + pixel_size, py)
                cloud.goto(px + pixel_size, py + pixel_size)
                cloud.goto(px, py + pixel_size)
                cloud.goto(px, py)

                cloud.end_fill()


def draw_clouds(game_time):

    cloud.clear()

    highlight, shadow = get_cloud_colours(game_time)

    for cloud in clouds:

        x, y, scale, shade, design, direction = cloud

        draw_pixel_cloud(
            x, y, scale, shade, design,
            highlight, shadow
        )


def move_clouds():

    for cloud in clouds:

        x, y, scale, shade, design, direction = cloud


        cloud[0] += 0.35 * scale * direction
        cloud_width = 14 * 9 * scale
        margin = cloud_width / 2 + 20
        if direction == 1 and cloud[0] > width / 2 + margin:

            cloud[0] = -width / 2 - margin

        elif direction == -1 and cloud[0] < -width / 2 - margin:

            cloud[0] = width / 2 + margin


ground_keyframes = [
    (0, (
        (48, 72, 91),
        (36, 65, 73),
        (27, 54, 55)
    )),
    (270, (
        (48, 72, 91),
        (36, 65, 73),
        (27, 54, 55)
    )),
    (360, (
        (151, 160, 125),
        (112, 139, 91),
        (82, 119, 72)
    )),
    (480, (
        (145, 190, 112),
        (104, 163, 85),
        (69, 132, 65)
    )),
    (960, (
        (145, 190, 112),
        (104, 163, 85),
        (69, 132, 65)
    )),
    (1080, (
        (173, 133, 105),
        (133, 105, 84),
        (91, 91, 65)
    )),
    (1200, (
        (48, 72, 91),
        (36, 65, 73),
        (27, 54, 55)
    )),
    (1440, (
        (48, 72, 91),
        (36, 65, 73),
        (27, 54, 55)
    ))
]


def get_ground_colours(game_time):

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )

    for i in range(len(ground_keyframes) - 1):

        starttime, start_colours = ground_keyframes[i]
        end_time, end_colours = ground_keyframes[i + 1]

        if starttime <= minutes < end_time:

            t = (minutes - starttime) / (end_time - starttime)

            colours = []

            for colour1, colour2 in zip(start_colours, end_colours):

                colours.append(
                    blend_colour(colour1, colour2, t)
                )

            return colours

    return ground_keyframes[0][1]


def drawhill(baseheight, amplitude, phase, colour):

    grounddraw.color(colour)

    grounddraw.goto(-width / 2, -height / 2)
    grounddraw.begin_fill()

    grounddraw.goto(-width / 2, baseheight)

    steps = 45

    for i in range(steps + 1):

        x = -width / 2 + (width * i / steps)

        y = (
            baseheight
            + sin((x / width * 2 * pi) + phase) * amplitude
            + sin((x / width * 4 * pi) + phase) * amplitude * 0.25
        )

        grounddraw.goto(x, y)

    grounddraw.goto(width / 2, -height / 2)
    grounddraw.goto(-width / 2, -height / 2)

    grounddraw.end_fill()

def get_grass_height(x):

    return (
        -height * 0.39
        + sin((x / width * 2 * pi) + 2) * height * 0.012
        + sin((x / width * 5 * pi) + 1) * height * 0.006
    )


def drawgrass(colour):

    grounddraw.color(colour)

    grounddraw.goto(-width / 2, -height / 2)
    grounddraw.begin_fill()

    grounddraw.goto(-width / 2, get_grass_height(-width / 2))

    for i in range(45):

        x = -width / 2 + width * i / 44

        grounddraw.goto(x, get_grass_height(x))

    grounddraw.goto(width / 2, -height / 2)
    grounddraw.goto(-width / 2, -height / 2)

    grounddraw.end_fill()



def grassdetail():

    random.seed(15)

    for i in range(32):

        x = random.randint(
            int(-width / 2 + 15),
            int(width / 2 - 15)
        )

        y = get_grass_height(x)

        grounddraw.color((40, 105, 55))

        grounddraw.width(2)

        grounddraw.goto(x, y + 2)
        grounddraw.pendown()
        grounddraw.goto(x - 3, y + 9)

        grounddraw.penup()
        grounddraw.goto(x, y + 2)
        grounddraw.pendown()
        grounddraw.goto(x + 3, y + 8)

        grounddraw.penup()


def draw_ground(game_time):

    grounddraw.clear()

    distant, near, foreground = get_ground_colours(game_time)

    drawhill(
        -height * 0.31,
        height * 0.045,
        0.5,
        distant
    )
    drawhill(
        -height * 0.36,
        height * 0.045,
        2.5,
        near
    )

    draw_scenery(game_time)

    drawgrass(foreground)

    grassdetail()

    grounddraw.width(1)


foliage_keyframes = [
    (0, ((38, 67, 65), (27, 49, 53))),      
    (270, ((38, 67, 65), (27, 49, 53))),
    (360, ((151, 157, 91), (102, 120, 68))),  
    (480, ((91, 151, 70), (54, 111, 58))),   
    (960, ((91, 151, 70), (54, 111, 58))),
    (1080, ((165, 119, 65), (112, 91, 57))),  
    (1200, ((38, 67, 65), (27, 49, 53))),
    (1440, ((38, 67, 65), (27, 49, 53)))
]


def get_foliage_colours(game_time):

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )

    for i in range(len(foliage_keyframes) - 1):

        start_time, start_colours = foliage_keyframes[i]
        end_time, end_colours = foliage_keyframes[i + 1]

        if start_time <= minutes < end_time:

            t = (minutes - start_time) / (end_time - start_time)

            main = blend_colour(
                start_colours[0],
                end_colours[0],
                t
            )

            dark = blend_colour(
                start_colours[1],
                end_colours[1],
                t
            )

            return main, dark

    return foliage_keyframes[0][1]


def draw_pixel_rect(x, y, rect_width, rect_height, colour):
    bgdraw.penup()
    bgdraw.goto(x, y)
    bgdraw.color(colour)
    bgdraw.begin_fill()
    bgdraw.goto(x + rect_width, y)
    bgdraw.goto(x + rect_width, y + rect_height)
    bgdraw.goto(x, y + rect_height)
    bgdraw.goto(x, y)
    bgdraw.end_fill()
    bgdraw.penup()


def tree(x, base_y, scale, phase, game_time):

    main_leaf, dark_leaf = get_foliage_colours(game_time)
    highlight_leaf = blend_colour(main_leaf, (220, 225, 150), 0.28)
    sway_time = dt.now().timestamp()
    sway = round(sin(sway_time * 1.0 + phase) * 2 * scale)

    trunk_colour = (105, 70, 48)
    trunk_shadow = (78, 53, 42)
    branch_colour = (91, 61, 43)

    trunk_width = 16 * scale
    trunk_height = 57 * scale

    draw_pixel_rect(
        x - trunk_width / 2,
        base_y,
        trunk_width,
        trunk_height,
        trunk_colour
    )
    draw_pixel_rect(
        x + trunk_width / 2 - 5 * scale,
        base_y,
        5 * scale,
        trunk_height,
        trunk_shadow
    )

    draw_pixel_rect(
        x - 29 * scale,
        base_y + 48 * scale,
        25 * scale,
        9 * scale,
        branch_colour
    )
    draw_pixel_rect(
        x + 4 * scale,
        base_y + 53 * scale,
        25 * scale,
        9 * scale,
        branch_colour
    )

    tile = 16 * scale
    canopy_rows = [
        (126, [-1, 0, 1]),
        (110, [-2, -1, 0, 1, 2]),
        (94,  [-3, -2, -1, 0, 1, 2, 3]),
        (78,  [-3, -2, -1, 0, 1, 2, 3]),
        (62,  [-2, -1, 0, 1, 2]),
        (46,  [-1, 0, 1])
    ]

    for row_index, (offset_y, columns) in enumerate(canopy_rows):
        row_sway = sway if row_index < 4 else round(sway * 0.5)

        for column in columns:
            leaf_x = x + column * tile + row_sway * scale
            leaf_y = base_y + offset_y * scale
            if (column + row_index) % 3 == 0:
                leaf_colour = dark_leaf
            else:
                leaf_colour = main_leaf

            draw_pixel_rect(
                leaf_x - tile / 2,
                leaf_y,
                tile,
                tile,
                leaf_colour
            )


    highlight_tiles = [
        (-1, 110), (2, 94), (-2, 78), (1, 62)
    ]
    for column, offset_y in highlight_tiles:
        leaf_x = x + column * tile + sway * scale
        leaf_y = base_y + offset_y * scale + 5 * scale
        draw_pixel_rect(
            leaf_x - 3 * scale,
            leaf_y,
            6 * scale,
            6 * scale,
            highlight_leaf
        )


def draw_house(game_time):

    x = width * 0.035
    base_y = get_grass_height(x) - 2

    house_width = 108
    wall_height = 60

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )
    is_night = minutes >= 18 * 60 + 30 or minutes < 5 * 60 + 30

    draw_pixel_rect(
        x - house_width / 2,
        base_y,
        house_width,
        wall_height,
        (91, 65, 53)
    )
    draw_pixel_rect(
        x - house_width / 2 + 4,
        base_y + 4,
        house_width - 8,
        wall_height - 4,
        (224, 197, 153)
    )

    draw_pixel_rect(
        x - house_width / 2 + 4,
        base_y + 4,
        house_width - 8,
        7,
        (183, 145, 108)
    )

    draw_pixel_rect(
        x + 25,
        base_y + 91,
        15,
        28,
        (91, 55, 48)
    )
    draw_pixel_rect(
        x + 29,
        base_y + 91,
        7,
        24,
        (151, 83, 67)
    )
    roof_layers = [
        (132, 12, (91, 48, 45)),
        (108, 12, (119, 57, 49)),
        (84, 12, (137, 67, 55)),
        (60, 12, (151, 78, 62)),
        (36, 12, (165, 91, 69))
    ]

    for layer_index, (layer_width, layer_height, roof_colour) in enumerate(roof_layers):
        layer_y = base_y + wall_height + layer_index * 11
        draw_pixel_rect(
            x - layer_width / 2,
            layer_y,
            layer_width,
            layer_height,
            (78, 48, 45)
        )
        draw_pixel_rect(
            x - layer_width / 2 + 3,
            layer_y + 3,
            layer_width - 6,
            layer_height - 3,
            roof_colour
        )
    draw_pixel_rect(
        x - 10,
        base_y + 4,
        20,
        36,
        (91, 61, 48)
    )
    draw_pixel_rect(
        x - 7,
        base_y + 4,
        13,
        32,
        (139, 91, 61)
    )
    draw_pixel_rect(
        x + 3,
        base_y + 21,
        3,
        3,
        (239, 195, 105)
    )

    window_colour = (255, 218, 125) if is_night else (145, 194, 207)

    for window_x in (x - 34, x + 34):
        window_y = base_y + 25

        draw_pixel_rect(
            window_x - 10,
            window_y - 2,
            20,
            21,
            (82, 60, 49)
        )
        draw_pixel_rect(
            window_x - 7,
            window_y + 1,
            14,
            15,
            window_colour
        )
        draw_pixel_rect(
            window_x - 1,
            window_y + 1,
            3,
            15,
            (82, 60, 49)
        )
        draw_pixel_rect(
            window_x - 7,
            window_y + 7,
            14,
            3,
            (82, 60, 49)
        )

    draw_pixel_rect(
        x - 68,
        base_y + wall_height - 2,
        8,
        5,
        (78, 48, 45)
    )
    draw_pixel_rect(
        x + 60,
        base_y + wall_height - 2,
        8,
        5,
        (78, 48, 45)
    )

    bgdraw.width(1)


def draw_scenery(game_time):

    bgdraw.clear()

    left_x = -width * 0.34
    right_x = width * 0.36

    tree(
        left_x,
        get_grass_height(left_x) - 3,
        1.0,
        0,
        game_time
    )

    tree(
        right_x,
        get_grass_height(right_x) - 3,
        0.78,
        2.1,
        game_time
    )

    draw_house(game_time)


def draw_sun(game_time):

    sun.clear()

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )
    sunrise = 300
    sunset_time = 1080
    if minutes < sunrise or minutes >= sunset_time:
        return
    progress = (minutes - sunrise) / (sunset_time - sunrise)
    radius = 45
    margin = 60
    x = (
        -width / 2 + margin
        + progress * (width - margin * 2)
    )
    bottom = -height / 2 - 60
    highest_point = height * 0.35
    y = (
        bottom
        + sin(progress * pi) * (highest_point - bottom)
    )
    sun_layers = [
        (54, "#F79650"),
        (50, "#FCB752"),
        (46, "#FDE08A"),
        (42, "#FCF4BC")
    ]

    for size, colour in sun_layers:

        sun.goto(x, y - size)
        sun.color(colour)
        sun.begin_fill()
        sun.circle(size)
        sun.end_fill()

game_time = dt.now()
last_real_time = dt.now()
last_sky_update = dt.now()

def drawmoon(game_time):

    moon.clear()

    minutes = (
        game_time.hour * 60
        + game_time.minute
        + game_time.second / 60
    )

    if minutes >= 18 * 60 + 30 or minutes < 5 * 60 + 30:

        x = width * 0.32
        y = height * 0.32

        halo_frames = [
            (0, (160, 175, 230)),       
            (240, (160, 175, 230)),      
            (330, (255, 190, 190)),     
            (1110, (255, 205, 155)),     
            (1200, (230, 175, 220)),   
            (1320, (165, 175, 240)),  
            (1440, (160, 175, 230))   
        ]

        halo_colour = halo_frames[0][1]

        for i in range(len(halo_frames) - 1):

            start_time, start_colour = halo_frames[i]
            end_time, end_colour = halo_frames[i + 1]

            if start_time <= minutes < end_time:

                t = (
                    (minutes - start_time)
                    / (end_time - start_time)
                )

                halo_colour = blend_colour(
                    start_colour,
                    end_colour,
                    t
                )

                break

        glow1 = blend_colour(
            (20, 25, 45),
            halo_colour,
            0.30
        )

        glow2 = blend_colour(
            (20, 25, 45),
            halo_colour,
            0.55
        )

        glow3 = blend_colour(
            (20, 25, 45),
            halo_colour,
            0.80
        )

        moon.goto(x, y)
        moon.dot(110, glow1)

        moon.goto(x, y)
        moon.dot(90, glow2)

        moon.goto(x, y)
        moon.dot(70, glow3)

        moon.goto(x, y)
        moon.dot(54, (255, 244, 210))

        craters = [
            (-9, 8, 8),
            (10, 13, 6),
            (13, -7, 9),
            (-12, -11, 5),
            (1, -2, 5)
        ]

        for cx, cy, size in craters:

            moon.goto(x + cx, y + cy)
            moon.dot(size, (225, 215, 190))

        moon.goto(x - 13, y + 15)
        moon.dot(3, (255, 252, 235))

        moon.goto(x + 5, y + 18)
        moon.dot(2, (255, 252, 235))

def draw_clock():
    t.clear()
    t.penup()
    t.goto(10, 0)

    if game_time.hour >= 18 or game_time.hour < 6:
        t.color("white")
    else:
        t.color("black")

    t.write(
        game_time.strftime("%I:%M %p"),
        align="center",
        font=("Courier", 30, "bold")
    )


def update_clock():

    global game_time, last_real_time, last_sky_update

    current_time = dt.now()
    elapsed_time = current_time - last_real_time

    game_time += elapsed_time * 720
    last_real_time = current_time

    if current_time - last_sky_update >= timedelta(seconds=1):

        sky_colours = get_sky_colours(game_time)

        draw_sky(sky_colours)
        draw_stars(game_time, sky_colours)

        last_sky_update = current_time

        screen.title(
            "Pixel Weather | " + game_time.strftime("%I:%M %p")
        )

    move_clouds()
    draw_sun(game_time)
    draw_ground(game_time)
    drawmoon(game_time)
    draw_clouds(game_time)
    draw_clock()

    screen.update()
    screen.ontimer(update_clock, 30)


sky_colours = get_sky_colours(game_time)

draw_sky(sky_colours)
draw_sun(game_time)
draw_stars(game_time, sky_colours)
draw_ground(game_time)
drawmoon(game_time)
draw_clouds(game_time)
draw_clock()

screen.update()

screen.title(
    "Animated Clock Time: " + game_time.strftime("%I:%M %p")
)

screen.ontimer(update_clock, 30)

turtle.done()
