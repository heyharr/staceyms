from ursina import *

def update():
    first.rotation_x += 50 * time.dt
    first.rotation_y += 25 * time.dt 
    first.rotation_z += 50 * time.dt 

app = Ursina()

first = Entity(model = 'cube',
                color=color.rgb(255,255,180),
                texture='sky_sunset',

                position = (0,0,0),

                rotation = (3,3,8)
)   


app.run()