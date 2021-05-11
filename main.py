from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale = 1,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white)


class Voxel1(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale = 0.1,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.green)

class Voxel_gray(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale_x = 2.1,
            scale_z = 1.1,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.gray)

class Voxel_red(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale_x = 0.3,
            scale_z = 0.1,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.red)

class Voxel_blue(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale_x = 0.1,
            scale_z = 0.3,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.blue)
        

def kuchenka():
        voxel = Voxel1(position = (7, 0.1, 1))
        voxel = Voxel1(position = (7, 0.1, 2))
        voxel = Voxel1(position = (5, 0.1, 1))
        voxel = Voxel1(position = (5, 0.1, 2))
        voxel = Voxel_gray(position = (6,1.1, 1.5))
        voxel = Voxel_red(position = (6,1.2, 1.5))
        voxel = Voxel_blue(position = (6,1.2,1.5))
    
app = Ursina()
sky = Sky()


for x in range (20):
    for z in range(20):
        voxel = Voxel(position = (x,0,z))


a = 0.5
b = 0.5

for x in range(20):
    for y in range(10):
        voxel = Voxel(position = (x,y,0))

for z in range(20):
    for y in range(10):
        voxel = Voxel(position = (20,y,z))

for z in range(20):
    for y in range(10):
        voxel = Voxel(position = (0,y,z))

for x in range(20):
    for y in range(10):
        voxel = Voxel(position = (x,y,20))

kuchenka()

voxel = Voxel(position = (1,1,4))
voxel = Voxel(position = (3,2,4))
voxel = Voxel(position = (5,3,4))
voxel = Voxel(position = (7,4,4))
voxel = Voxel(position = (7,5,6))

Vvoxel = Voxel1(position = (8,7,6))
Vvoxel.on_click = application.quit
Vvoxel.tooltip = Tooltip('exit')

Vvoxel = Voxel1(position = (1,1.5,0.5))
Vvoxel.on_click = application.quit
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (1,1.7,0.5))
Vvoxel.on_click = application.quit
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (1,1.9,0.5))
Vvoxel.on_click = application.quit
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (1.2,1.5,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (1.2,1.7,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (1.2,1.9,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (0.8,1.5,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (0.8,1.7,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')

Vvoxel = Voxel1(position = (0.8,1.9,0.5))
Vvoxel.on_click = print('click')
Vvoxel.tooltip = Tooltip('test2')



player = FirstPersonController( position = (2,1,2))

a = Audio('song.mp3', pitch=1, loop=True, autoplay=True)
print(a.clip)





app.run()
