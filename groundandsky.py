from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(model='plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (100,1,100))

player = FirstPersonController()
Sky()

app.run()