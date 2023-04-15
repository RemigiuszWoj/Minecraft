import ursina

from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor


grass_texture = "assets/grass_14.png"

terain_width = 32


def input(key):
    if key == 'q' or key == "escape":
        quit()


def update():
    pass


app = ursina.Ursina()

ursina.window.color = ursina.color.rgb(r=0, g=200, b=211)
ursina.window.exit_button.visible = False

ursina.scene.fog_color = ursina.color.rgb(0, 0, 0)
ursina.scene.fog_density = 0.04

terrein = ursina.Entity(model=None, collider=None)
noise = PerlinNoise(octaves=2, seed=2021)
amp = 6
freq = 24


for i in range(terain_width * terain_width):
    block = ursina.Entity(model="cube", color=ursina.color.green)
    block.x = floor(i / terain_width)
    block.z = floor(i % terain_width)
    block.y = floor((noise([block.x/freq, block.z/freq])) * amp)
    block.parent = terrein

terrein.combine()
terrein.collider = "mesh"
terrein.texture = grass_texture

player = FirstPersonController()
player.cursor.visible = False
player.gravity = 1
player.x = 5
player.z = 5
player.y = 12

app.run()
