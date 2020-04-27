import arcade

# Constantes de la ventana
NOMBRE_VENTANA = "Mario Python"
ALTO_PANTALLA = 500
ANCHO_PANTALLA = 1000

# Constantes para escalar los sprites
ESCALADO_PERSONAJE = 0.17
ESCALADO_SUELO = 0.20
ESCALADO_TUBERIA = 0.20

# Constantes para física del jugador
VELOCIDAD_MOVIMINETO_JUGADOR = 5
VELOCIDAD_SALTO_JUGADOR = 20
GRAVEDAD = 1

# Constantes del margen minimo entre el jugador y el borde de la pantalla
MARGEN_ALTO = 100
MARGEN_BAJO = 50
MARGEN_IZQUIERDO = 250
MARGEN_DERECHO = 250


class MyGame(arcade.Window):

	def __init__(self):

		super().__init__(ANCHO_PANTALLA, ALTO_PANTALLA, NOMBRE_VENTANA)

		arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

		self.listaJugador = None
		self.listaSprites = None

		# Variable del sprite del jugador
		self.spriteJugador = None

		# Variables para seguir despalzamiento del jugador
		self.seguimientoX = 0
		self.seguimientoY = 0

	def setup(self):
		self.listaJugador = arcade.SpriteList()
		self.listaSprites = arcade.SpriteList()

		# Crear Jugador
		self.spriteJugador = arcade.Sprite("assets/mario.png", ESCALADO_PERSONAJE)
		self.spriteJugador.center_x = 64
		self.spriteJugador.center_y = 93
		self.listaJugador.append(self.spriteJugador)

		# Funciòn para crear piso
		def crearPiso(inicio, final, posicionY, conPasto):
			for posicionX in range(inicio, final):
				if conPasto == True:
					spritePiso = arcade.Sprite("assets/ground0.png", ESCALADO_SUELO)
				else:
					spritePiso = arcade.Sprite("assets/ground1.png", ESCALADO_SUELO)
				spritePiso.center_x = 64*posicionX
				spritePiso.center_y = 64*posicionY + 32
				self.listaSprites.append(spritePiso)
		"""
		# Funciòn para crear tuberia
		def crearTuberia(coordenadaX, coordenadaY, tamaño):
			for y in range(coordenadaY, tamaño+coordenadaY):
				spriteTuberia = arcade.Sprite("assets/cylinder1.png", ESCALADO_TUBERIA)
				spriteTuberia.center_x = 64*coordenadaX
				spriteTuberia.center_y = 64*y + 32 + 64*coordenadaY
				self.listaSprites.append(spriteTuberia)
			spriteTuberia = arcade.Sprite("assets/cylinder0.png", ESCALADO_TUBERIA)
			spriteTuberia.center_x = 64*coordenadaX
			spriteTuberia.center_y = 64*tamaño + 110 + 64*coordenadaY -64
			self.listaSprites.append(spriteTuberia)
		"""
		spriteTuberia = arcade.Sprite("assets/cylinder1.png", ESCALADO_TUBERIA)
		spriteTuberia.center_x = 64*8
		spriteTuberia.center_y = 64*1 + 32 + 64*2
		self.listaSprites.append(spriteTuberia)
		spriteTuberia = arcade.Sprite("assets/cylinder1.png", ESCALADO_TUBERIA)
		spriteTuberia.center_x = 64*8
		spriteTuberia.center_y = 64*3 + 32 + 64*2
		self.listaSprites.append(spriteTuberia)
		spriteTuberia = arcade.Sprite("assets/cylinder1.png", ESCALADO_TUBERIA)
		spriteTuberia.center_x = 64*8
		spriteTuberia.center_y = 64*2 + 32 + 64*2
		self.listaSprites.append(spriteTuberia)

		spriteTuberia = arcade.Sprite("assets/cylinder0.png", ESCALADO_TUBERIA)
		spriteTuberia.center_x = 64*8
		spriteTuberia.center_y = 64*3 + 110 + 64*2
		self.listaSprites.append(spriteTuberia)
		
		
		crearPiso( 0, 40, 0, True)
		crearPiso(19, 40, 0, False)
		crearPiso(19, 24, 1, False)
		crearPiso(24, 40, 1, False)
		crearPiso(24, 40, 2, False)
		crearPiso(24, 40, 3, False)
		crearPiso(24, 25, 4, True)
		crearPiso(25, 40, 4, False)
		crearPiso(25, 40, 5, True)
		crearPiso(40, 41, 0, True)
		crearPiso(19, 24, 2, True)

		# This shows using a coordenadas list to place sprites
		listaTuberias = [[ 4, 1, 0],
						 [ 8, 1, 1],
						 [12, 1, 2]]

		for coordenadas in listaTuberias:
			crearTuberia(coordenadas[0], coordenadas[1], coordenadas[2])

		listaPiso = [[ 6, 7, 1, True],
					 [10,11, 1, True],
					 [14,15, 1, True]]

		for coordenadas in listaPiso:
			crearPiso(coordenadas[0], coordenadas[1], coordenadas[2], coordenadas[3])

		#Creathe the "physics engine"
		self.physics_engine = arcade.PhysicsEnginePlatformer(self.spriteJugador, self.listaSprites, GRAVEDAD)
	
	def on_draw(self):
		arcade.start_render()
		self.listaJugador.draw()
		self.listaSprites.draw()

	def on_key_press(self, key, modifiers):
		"""Called whenever a key is pressed. """

		if key == arcade.key.UP or key == arcade.key.W:
			if self.physics_engine.can_jump():
				self.spriteJugador.change_y = VELOCIDAD_SALTO_JUGADOR
		elif key == arcade.key.LEFT or key == arcade.key.A:
			self.spriteJugador.change_x = -VELOCIDAD_MOVIMINETO_JUGADOR
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.spriteJugador.change_x = VELOCIDAD_MOVIMINETO_JUGADOR

	def on_key_release(self, key, modifiers):
		"""Called when the user releases a key. """

		if key == arcade.key.LEFT or key == arcade.key.A:
			self.spriteJugador.change_x = 0
		elif key == arcade.key.RIGHT or key == arcade.key.D:
			self.spriteJugador.change_x = 0

	def on_update(self, delta_time):
		""" Movement and game logic """

		# Move the player with the physics engine
		self.physics_engine.update()

		# --- Manage Scrolling ---
		changed = False

        # Scroll left
		left_boundary = self.seguimientoX + MARGEN_IZQUIERDO
		if self.spriteJugador.left < left_boundary:
			self.seguimientoX -= left_boundary - self.spriteJugador.left
			changed = True

		# Scroll right
		right_boundary = self.seguimientoX + ANCHO_PANTALLA - MARGEN_DERECHO
		if self.spriteJugador.right > right_boundary:
			self.seguimientoX += self.spriteJugador.right - right_boundary
			changed = True

		# Scroll up
		top_boundary = self.seguimientoY + ALTO_PANTALLA - MARGEN_ALTO
		if self.spriteJugador.top > top_boundary:
			self.seguimientoY += self.spriteJugador.top - top_boundary
			changed = True

        # Scroll down
		bottom_boundary = self.seguimientoY + MARGEN_BAJO
		if self.spriteJugador.bottom < bottom_boundary:
			self.seguimientoY -= bottom_boundary - self.spriteJugador.bottom
			changed = True

		if changed:
			# Only scroll to integers. Otherwise we end up with pixels that
			# don't line up on the screen
			self.seguimientoY = int(self.seguimientoY)
			self.seguimientoX = int(self.seguimientoX)

			# Do the scrolling
			arcade.set_viewport(self.seguimientoX, ANCHO_PANTALLA + self.seguimientoX, self.seguimientoY,ALTO_PANTALLA + self.seguimientoY)

def main():
	window = MyGame()
	window.setup()
	arcade.run()

if __name__ == "__main__":
	main()