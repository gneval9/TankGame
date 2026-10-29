# Made and developed by gneval9 Software
# 28-10-2026


import fd3de
import time
import math as m

player = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
tank_model = fd3de.load("Modelos/tank.fd3de")
canon = fd3de.spawn(fd3de.load("Modelos/canon.fd3de"))
bullet_model = fd3de.load("Modelos/cubo.fd3de")


fd3de.scene_new("main")
fd3de.scene_new("tanks")
fd3de.scene_new("bullets")

tank = fd3de.spawn(tank_model)


fd3de.scene_add("main", canon, fd3de.WHITE, 0.8)
fd3de.scene_add("tanks", tank, fd3de.WHITE)

fd3de.move("z", -400, player)

fd3de.move("z", -230, canon)
fd3de.move("y", -50, canon)


last_shot = 0
space_was_pressed = False



rot_speed = 1

chasis_offset = 400
height_offset = 30

player_coords = [0,0,0]
player_orient = 0
player_speed = 5

canon_deg = 0

tank_coords = [-100,0,400]
tank_orient = 90


bullets = [fd3de.spawn(bullet_model), fd3de.spawn(bullet_model)]

def shoot():
    for n in range(len(bullets)):
        if not fd3de.scene_contains("bullets", bullets[n]):
            fd3de.scene_add("bullets", bullets[n], fd3de.ORANGE, 0.1)
            print("BAANG!")


        else:
            print("Not bang.")

    


while True:

    # Entrada de teclado
    if fd3de.key_input("right"):
        player_orient += rot_speed

    if fd3de.key_input("left"):
        player_orient += -rot_speed



    if fd3de.key_input("up"):
        player_coords[0] += m.sin(m.radians(player_orient)) * player_speed
        player_coords[2] += m.cos(m.radians(player_orient)) * player_speed 

    if fd3de.key_input("down"):
        player_coords[0] -= m.sin(m.radians(player_orient)) * player_speed
        player_coords[2] -= m.cos(m.radians(player_orient)) * player_speed 




    if fd3de.key_input("s") and canon["rotation"][0] > -10:
        canon_deg -= 1
 
    if fd3de.key_input("w") and canon["rotation"][0] < 0:
        canon_deg += 1

    
    # Disparar
    if fd3de.key_input("space") or fd3de.key_input("enter"):
        if time.time() - last_shot > 0.5 and space_was_pressed == False:
            last_shot = time.time()
            shoot()
            space_was_pressed = True

    if not fd3de.key_input("space"):
        space_was_pressed = False


    



    # Calcular posición relativa
    tank["position"] = [tank_coords[0] - player_coords[0], tank_coords[1] - player_coords[1], tank_coords[2] - player_coords[2]]
    

    tank["original"] = fd3de.spawn(tank_model)["original"]    

    tank["position"][1] -= height_offset
    tank["position"][2] -= chasis_offset


    # Calcular posición relativa (rotación)
    fd3de.scene_orbit_all("y", -player_orient, "tanks", player)
    tank["rotation"][1] = -player_orient + tank_orient



    # Ángulo del cañón
    canon["rotation"][0] = canon_deg





    fd3de.render_scene(fd3de.ALL)
