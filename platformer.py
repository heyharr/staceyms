from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

player=PlatformerController2d(y=1, z=.01, scale_y=1, color=color.green)
ground=Entity(model='quad', y=-2, scale_x=10, collider="box", color=color.yellow)
wall=Entity(model='quad', color=color.azure, scale=(1,5), x=5.5, collider="box")

app.run()