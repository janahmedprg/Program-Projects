from designer import *
from random import randint

SNAKE_SPEED = 6
DELAY = 4

# Define the shape of the World
World = {
    "food": [DesignerObject],
    "body": [DesignerObject],
    "head": DesignerObject,
    "snake speed": int,
    "direction": int,
    'score': int,
    'message': DesignerObject,
}

# Create a function that creates new worlds
def create_the_world() -> World:
    # Actually create an initial World instance
    return {
        "food": [],
        "body": [],
        "head": circle("red", 10),
        "snake speed": SNAKE_SPEED,
        "direction": 0,
        "position":[],
        'score': 0,
        'message': text('black', '', 20, get_width()/2, 10),
    }

# move snake
def move_snake(world:World):
    distance = 2
    world['position'].insert(0, [world['head']['x'], world['head']['y']])

    for body in world['body']:
        body['x']=world["position"][distance][0]
        body['y']=world["position"][distance][1]
        distance += 3

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

def change_direction(world: World, key: str):
    if key == 'left':
        head_left(world)
    elif key == 'right':
        head_right(world)
    elif key == 'up':
        head_up(world)
    elif key == 'down':
        head_down(world)

# create food
def create_food() -> DesignerObject:
    food = image('apple.png')
    food['scale_x'] = 1
    food['scale_y'] = 1
    food['anchor'] = 'center'
    food['x'] = randint(20, 780)
    food['y'] = randint(20, 580)
    return food

def make_food(world: World):
    not_too_much_food = len(world['food']) < 1
    random_chance = randint(1, 1) == not_too_much_food
    if not_too_much_food and random_chance:
        world['food'].append(create_food())

# create body
def create_body(world) -> DesignerObject:
    body = circle("green", 10)
    distance = 5
    body['x']=world["position"][distance][0]
    body['y']=world["position"][distance][1]
    return body

# food_ate
def food_ate(world):
    # Compare every drop to every fire
    for head in [world['head']]:
        for food in world['food']:
            # Check if there are any collisions between each pair
            if colliding(head, food):
                # Remember to remove this drop and fire
                food['x'] = randint(20, 780)
                food['y'] = randint(20, 580)
                world['body'].append(create_body(world))
                # And increase our score accordingly
                world['score'] += 1

#Counter
def update_message(world):
    world['message']['text'] = str(world["score"])

# game over
def game_over(world: World):
    world['message']['text'] = "GAME OVER!"

# food_ate
def dead_snake(world):
    # Compare every drop to every fire
    for head in [world['head']]:
        for body in world['body'][2:]:
            # Check if there are any collisions between each pair
            if colliding(head, body):
                game_over(world)
                pause()

# food_ate
def dead_snake2(world):
    # Compare every drop to every fire
    for head in [world['head']]:
            # Check if there are any collisions between each pair
            if not(0 < world["head"]["x"] <= get_width()) or not(0 < world["head"]["y"] <= get_height()):
                game_over(world)
                pause()

# This tells Designer to call our `create_the_world` function
# when the game starts, in order to setup our initial World.
when("starting", create_the_world)
when("updating", move_snake)
when('typing', change_direction)
#Creating food
when('updating', make_food)
# food_ate
when('updating', food_ate)
#Counter
when('updating', update_message)
when(dead_snake, pause)
when(dead_snake2, pause)
start()
