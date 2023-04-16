import ursina

from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from numpy import floor


grass_texture_path = "assets/grass_14.png"
# grass_texture = ursina.load_texture(name="grass_14.png",
#   path=grass_texture_path)

grass_texture = grass_texture_path
terain_width = 32


def input(key):
    if key == 'q' or key == "escape":
        quit()


def update():
    pass


# def generate_shell(shell_width: int, shellies: list, player, freq: int, amp: int) -> None:
#     for i in range(len(shellies)):
#         x = shellies[i].x = floor((i / shell_width) + player.x)
#         z = shellies[i].z = floor((i / shell_width) + player.z)
#         shellies[i].y = floor((noise([x/freq, z/freq])) * amp)


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

shell_width = 6
shellies = [ursina.Entity(model="cube", collider="box") for _ in range(
    shell_width * shell_width)]


player = FirstPersonController()
player.cursor.visible = False
player.gravity = 1
player.x = 5
player.z = 5
player.y = 12

chicken_model = ursina.load_model("chicken.obj")
vincent = ursina.Entity(model=chicken_model, scale=1,
                        x=22, z=16, y=7.1,
                        texture="chicken.png",
                        double_sided=True)

app.run()
