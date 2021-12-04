from designer import *

PLANE_SPEED =4

World = {
    'plane': DesignerObject,
    'plane speed': int,
}

def create_world() -> World:
    return {
        'plane': image(r"D:\Users\janah\Desktop\Program-Projects\py projects\airplane2.png", 100, 100),
        'plane speed': PLANE_SPEED,
        }

def create_plane() -> DesignerObject:
    plane = image(r"D:\Users\janah\Desktop\Program-Projects\py projects\airplane2.png")
    plane['scale'] = .25
    return plane

def move_plane(world: World):
    world['plane']['x'] += world['plane speed']

def head_left(world: World):
    world['plane speed'] = -PLANE_SPEED
    world['plane']['flip_x']=True

def head_right(world: World):
    world['plane speed'] = PLANE_SPEED
    world['plane']['flip_x']=False

def bounce_plane(world: World):
    if world['plane']['x'] > get_width():
        head_left(world)
    elif world['plane']['x'] < 0:
        head_right(world)

when('starting', create_world)
when("updating", create_plane)
when('updating', move_plane)
when('updating', bounce_plane)
start()
