# Made and developed by gneval9 Software
# 28-10-2026


import fd3de
import time
import math as m

player = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
tank_model = fd3de.load("Modelos/tank.fd3de")
tank_model_LP = fd3de.load("Modelos/square.fd3de")
canon = fd3de.spawn(fd3de.load("Modelos/canon.fd3de"))

fd3de.scene_new("main")
fd3de.scene_new("tanks")

tank = fd3de.spawn(tank_model)
tank_LP = fd3de.spawn(tank_model_LP)

fd3de.scene_add("main", canon, fd3de.WHITE, 0.8)
fd3de.scene_add("tanks", tank, fd3de.WHITE)

fd3de.move("z", -400, player)

fd3de.move("z", -230, canon)
fd3de.move("y", -50, canon)


LOD_dist = 3000

chasis_offset = 400
height_offset = 30

player_coords = [0,0,0]
player_orient = 0
player_speed = 5

canon_deg = 0

tank_coords = [0,0,1900]
tank_orient = 90





while True:

    # Entrada de teclado
    if fd3de.key_input("right"):
        player_orient += 2

    if fd3de.key_input("left"):
        player_orient += -2



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

    


    # Calcular posición relativa
    tank["position"] = [tank_coords[0] - player_coords[0], tank_coords[1] - player_coords[1], tank_coords[2] - player_coords[2]]
    

    if tank["position"][0] > LOD_dist or tank["position"][2] > LOD_dist:
        tank["original"] = fd3de.spawn(tank_model_LP)["original"]    

        tank["position"][1] -= height_offset
        tank["position"][2] -= chasis_offset
 
        fd3de.scene_orbit_all("y", -player_orient, "tanks", player)
        tank["rotation"][1] = -player_orient



    else:
        tank["original"] = fd3de.spawn(tank_model)["original"]    

        tank["position"][1] -= height_offset
        tank["position"][2] -= chasis_offset


        # Calcular posición relativa (rotación)
        fd3de.scene_orbit_all("y", -player_orient, "tanks", player)
        tank["rotation"][1] = -player_orient + tank_orient



    # Ángulo del cañón
    canon["rotation"][0] = canon_deg





    fd3de.render_scene(fd3de.ALL)
