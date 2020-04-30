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
		self.spriteJugador = arcade.Sprite("assets/sprites/mario.png", ESCALADO_PERSONAJE)
		self.spriteJugador.center_x = 64
		self.spriteJugador.center_y = 93
		self.listaJugador.append(self.spriteJugador)

		# Funciòn para crear piso
		def crearPiso(inicio, final, posicionY, conPasto):
			for posicionX in range(inicio, final):
				if conPasto == True:
					spritePiso = arcade.Sprite("assets/sprites/ground0.png", ESCALADO_SUELO)
				else:
					spritePiso = arcade.Sprite("assets/sprites/ground1.png", ESCALADO_SUELO)
				spritePiso.center_x = 64*posicionX
				spritePiso.center_y = 64*posicionY + 32
				self.listaSprites.append(spritePiso)

		# Funciòn para crear bloque
		def crearBloque(inicio, final, posicionY):
			for posicionX in range(inicio, final):
				spriteBloque = arcade.Sprite("assets/sprites/wall0.png", ESCALADO_SUELO)
				spriteBloque.center_x = 64*posicionX
				spriteBloque.center_y = 64*posicionY + 32
				self.listaSprites.append(spriteBloque)
						 
		# Funciòn para crear tuberia
		def crearTuberia(posicionX, posicionY, altura):
			for y in range(posicionY, posicionY+altura-1):
				spriteTuberia = arcade.Sprite("assets/sprites/cylinder1.png", ESCALADO_TUBERIA)
				spriteTuberia.center_x = 64*posicionX
				spriteTuberia.center_y = 64*y + 32 
				self.listaSprites.append(spriteTuberia)
			spriteTuberia = arcade.Sprite("assets/sprites/cylinder0.png", ESCALADO_TUBERIA)
			spriteTuberia.center_x = 64*posicionX
			spriteTuberia.center_y = 64*(posicionY + altura - 1) + 46 
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

		listaBloques = [[ 6, 7, 2],
					    [10,11, 2],
					    [14,15, 2],
					    [22,23, 4],
						[35,40, 8]]

		listaTuberias = [[ 4, 1, 1],
						 [ 8, 1, 2],
						 [12, 1, 3],
						 [16, 1, 4],
						 [20, 3, 3],
						 [24, 3, 4],
						 [28, 6, 2],
						 [32, 6, 1]]

		for coordenadas in listaBloques:
			crearBloque(coordenadas[0], coordenadas[1], coordenadas[2])

		for coordenadas in listaTuberias:
			crearTuberia(coordenadas[0], coordenadas[1], coordenadas[2])		

		#Iniciando "motor de físicas"
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

		# Scrolling
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