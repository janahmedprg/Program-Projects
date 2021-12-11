from designer import *
from random import randint

SNAKE_SPEED = 10

# Define the shape of the World
World = {
    "food": [DesignerObject],
    "head": DesignerObject,
    "snake speed": int,
    "direction": int,
    "body": [DesignerObject],
}

# Create a function that creates new worlds
def create_the_world() -> World:
    # Actually create an initial World instance
    return {
        "food": [],
        "body":[],
        "head": rectangle("green",18,18),
        "snake speed": SNAKE_SPEED,
        "direction": 0,
        "position":[],
        "score": 0,
    }

def move_snake(world:World):
    i=0
    if len(world['position'])>world['score']:
        world['position'].pop()
    world['position'].insert(0,[world['head']['x'],world['head']['y']])

    for body in world['body']:
        body['x']=world["position"][i][0]
        body['y']=world["position"][i][1]
        i+=1

    if world['direction'] == 0:
        world["head"]["y"] += world["snake speed"]
    elif world['direction'] == 1:
        world["head"]["x"] += world["snake speed"]

def head_left(world: World):
    world["snake speed"] = -SNAKE_SPEED
    world['head']['flip_x'] = True
    for body in world['body']:
        body['flip_x']=True
    world['direction'] = 1

def head_right(world: World):
    world["snake speed"] = SNAKE_SPEED
    world['head']['flip_x'] = False
    for body in world['body']:
        body['flip_x']=False
    world['direction'] = 1

def head_up(world: World):
    world["snake speed"] = -SNAKE_SPEED
    world['head']['flip_y'] = True
    for body in world['body']:
        body['flip_y']=True
    world['direction'] = 0

def head_down(world: World):
    world["snake speed"] = SNAKE_SPEED
    world['head']['flip_y'] = False
    for body in world['body']:
        body['flip_y']=False
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

def create_food() -> DesignerObject:
    food = image(r"D:\Users\janah\Desktop\Program-Projects\py projects\apple.png")
    food['scale_x'] = 1
    food['scale_y'] = 1
    food['anchor'] = 'midbottom'
    food['x'] = randint(0, get_width())
    food['y'] = randint(0, get_height())
    return food

def create_body(world) -> DesignerObject:
    body = rectangle("green", 18,18)
    body['x'] = world['head']['x']
    body['y'] = world['head']['y']
    return body

def make_food(world: World):
    not_too_much_food = len(world['food']) < 1
    random_chance = randint(1, 1) == not_too_much_food
    if  not_too_much_food and random_chance:
        world['food'].append(create_food())

# food_ate
def food_ate(world):
    # Compare head to food
    for head in [world['head']]:
        for food in world['food']:
            # Check if there are any collisions between each pair
            if colliding(head, food):
                # Remember to change food location
                food['x'] = randint(0, get_width())
                food['y'] = randint(0, get_height())
                # And increase our score accordingly
                world['body'].append(create_body(world))
                world['score']+=1

# This tells Designer to call our `create_the_world` function
# when the game starts, in order to setup our initial World.
when("starting", create_the_world)
when("updating", move_snake)
when('updating', flip_snake)
when('typing', change_direction)
#Creating food
when('updating', make_food)
# food_ate
when('updating', food_ate)
start()
