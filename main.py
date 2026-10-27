import fd3de

# Prototipo de prueba


player = fd3de.spawn(fd3de.load("Modelos/cubo.fd3de"))
tank = fd3de.spawn(fd3de.load("Modelos/tank.fd3de"))
canon = fd3de.spawn(fd3de.load("Modelos/canon.fd3de"))

fd3de.scene_new("main")
fd3de.scene_new("tanks")

fd3de.scene_add("tanks", tank, fd3de.WHITE)
fd3de.scene_add("main", canon, fd3de.WHITE)
#fd3de.scene_add("main", player, fd3de.GREEN)

fd3de.rotate("y", 90, tank)
fd3de.move("y", -30, tank)

fd3de.move("z", -400, player)

fd3de.move("z", -300, canon)
fd3de.move("y", -70, canon)
#fd3de.rotate("x", -10, canon)




while True:
	if fd3de.key_input("right"):
		fd3de.orbit("y", -3, tank, player)
		fd3de.rotate("y", -3, tank)

	if fd3de.key_input("left"):
		fd3de.orbit("y", 3, tank, player)
		fd3de.rotate("y", 3, tank)

	if fd3de.key_input("up"):
		fd3de.scene_move_all("z", -5, "tanks")


	if fd3de.key_input("down"):
		fd3de.scene_move_all("z", 5, "tanks")



	if fd3de.key_input("w") and canon["rotation"][0] > -20:
		fd3de.rotate("x", -1, canon)

	if fd3de.key_input("s") and canon["rotation"][0] < -10:
		fd3de.rotate("x", 1, canon)






#    fd3de.rotate("y", -1, tank)

	fd3de.render_scene(fd3de.ALL)
