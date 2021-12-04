from designer import *
import random

SNAKE_SPEED = 6

# Define the shape of the World
World = {
    "food": DesignerObject,
    "head": DesignerObject,
    "snake speed": int,
    "direction": int,
}

# Create a function that creates new worlds
def create_the_world() -> World:
    # Actually create an initial World instance
    return {
        "food": image(r"D:\Users\janah\Desktop\Program-Projects\py projects\apple.png", random.randint(0,get_width()), random.randint(0,get_height())),
        "head": circle("green", 10),
        "snake speed": SNAKE_SPEED,
        "direction": 0

    }

def move_snake(world:World):
    if world['direction'] == 0:
        world["head"]["y"] += world["snake speed"]
    elif world['direction'] == 1:
        world["head"]["x"] += world["snake speed"]

def head_left(world: World):
    world["snake speed"] = -SNAKE_SPEED
    world['head']['flip_x'] = True
    world['direction'] = 1

def head_right(world: World):
    world["snake speed"] = SNAKE_SPEED
    world['head']['flip_x'] = False
    world['direction'] = 1

def head_up(world: World):
    world["snake speed"] = -SNAKE_SPEED
    world['head']['flip_y'] = True
    world['direction'] = 0

def head_down(world: World):
    world["snake speed"] = SNAKE_SPEED
    world['head']['flip_y'] = False
    world['direction'] = 0

def flip_snake(world: World):
    if world['head']['x'] > get_width():
        head_left(world)
    elif world['head']['x'] < 0:
        head_right(world)
    elif world['head']['y'] > get_height():
        head_up(world)
    elif world['head']['y'] < 0:
        head_down(world)

def change_direction(world: World, key: str):
    if key == 'left':
        head_left(world)
    elif key == 'right':
        head_right(world)
    elif key == 'up':
        head_up(world)
    elif key == 'down':
        head_down(world)

def collision(world: World):
    if (world['head']['x'] <= (world['food']['x']+20) and world['head']['x'] >= (world['food']['x']-20)) and (world['head']['y'] <= (world['food']['y']+20) and world['head']['y'] >= (world['food']['y']-20)):
        world['food']['x']=random.randint(0,get_width())
        world['food']['y']=random.randint(0,get_height())

when("starting", create_the_world)
when("updating", move_snake)
when('updating', flip_snake)
when('updating',collision)
when('typing', change_direction)
start()
