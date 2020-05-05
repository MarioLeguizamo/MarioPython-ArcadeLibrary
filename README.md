# Mario Python

Videogame de Mario Bros creado en Python conla  librería arcade.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/MarioPython0.png)

Para instalar la librería arcade, usa en la terminal:

    Windows
            pip install arcade 
    Linux o Mac
            pip3 install arcade

Si no funciona prueba actualizando pip.

            pip install --upgrade pip

El código MarioPython.py contiene las físicas necesarias para colisionar con los objetos, la gravedad y el desplazamiento del personaje.

Tiene funciones definidas para que puedas diseñar niveles muy fácil. Puedes agregar elementos de manera sencilla con una linea de código, a continuación se detallan los pasos para crear un escenario con solo escribir cuatro líneas dentro de la función “def setup(self):”.

## Crear Piso

Para crear el piso llamamos a la función def crearPiso(inicio, final, posicionY, conPasto):

- inicio: valor entero que indica desde donde se dibuja el piso.
- final: valor entero que indica hasta donde se dibuja el piso.
- posicionY: valor entero que indica la posición en el eje y en la que se dibuja el piso.
- conPasto: valor booleano que indica que sprite tomar.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial0.png)


## Crear Tuberías

Para agregar algunas tuberías llamamos a la función def crearTuberia(posicionX, posicionY, altura):

- posicionX: valor entero que indica la posición en el eje x en la que se dibuja la tubería.
- posicionY: valor entero que indica la posición en el eje y en la que se dibuja la tubería.
- altura: valor entero que indica la altura de la tubería.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial1.png)


## Crear Bloques

Para agregar bloques llamamos a la función def crearBloque(inicio, final, posicionY):

- inicio: valor entero que indica desde donde se dibuja el conjunto de bloques.
- final: valor entero que indica hasta donde se dibuja el conjunto de bloques.
- posicionY: valor entero que indica la posición en el eje y en la que se dibuja el conjunto de bloques.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial2.png)


Finalmente, así es como queda el escenario con solo cuatro líneas de código.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial3.png)

Para escenarios o niveles más detallados, con varios elementos, recomiendo crear una lista con los argumentos e iterar con un ciclo para construirlos, por ejemplo.

- listaTuberias = [[ 4, 1, 1],[ 8, 1, 2],[12, 1, 3]]
- for coordenadas in listaTuberias:
  - crearTuberia(coordenadas[0], coordenadas[1], coordenadas[2])

Estaré actualizando el repositorio y definiendo nuevas funciones para agregar más funcionalidades y elementos al juego.


### Actualización Mayo 4, 2020.

Agregue las funciones.

- def crearNube(inicio, final, posicionY):
- def crearArbusto(inicio, final, posicionY):

Funcionan de la misma forma que crearBloque(), con la diferencia de que no contienen fisicas.

![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/MarioPython1.png)
