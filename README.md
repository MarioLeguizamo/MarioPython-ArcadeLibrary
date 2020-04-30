# Mario Python

Videojuego de Mario Bros creado en Python con la librería arcade. 
![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/ImageMarioPython.png)

Para instalar la librería usa en la terminal:

    Windows
            pip install arcade 
    Linux o Mac
            pip3 install arcade
            
Si no funciona prueba actualizando pip

            pip install --upgrade pip

El código MarioPython.py ya contiene las físicas necesarias para colisionar con los objetos, la gravedad y el desplazamiento del personaje.

Tiene funciones definidas para que puedas diseñar niveles muy fácil. Puedes agregar elementos de manera sencilla con solo una linea de código, a continuación se detallan los pasos para crear un escenario con solo escribir 4 líneas dentro de la función “def setup(self)”. 

## Crear Piso
Para crear el piso llamamos a la función def crearPiso(inicio, final, posicionY, conPasto):

inicio: valor entero que indica desde donde se dibuja el piso.
final: valor entero que indica hasta donde se dibuja el piso.
posicionY: valor entero que indica la posición en el eje y en la que se dibuja el piso.
conPasto: valor booleano que indica que sprite tomar.
![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial0.png)


## Crear Tuberías
Para agregar algunas tuberías llamamos a la función def crearTuberia(posicionX, posicionY, altura):

posicionX: valor entero que indica la posición en el eje x en la que se dibuja la tubería.
posicionY: valor entero que indica la posición en el eje y en la que se dibuja la tubería.
altura: valor entero que indica la altura de la tubería.
![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial1.png)


## Crear Bloques
Para agregar bloques llamamos a la función def crearBloque(inicio, final, posicionY):

inicio: valor entero que indica desde donde se dibuja el conjunto de bloques.
final: valor entero que indica hasta donde se dibuja el conjunto de bloques.
posicionY: valor entero que indica la posición en el eje y en la que se dibuja el conjunto de bloques..
![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial2.png)


Finalmente, así es como queda el escenario con solo 4 líneas de código, estaré actualizando el repositorio y definiendo nuevas funciones para agregar más elementos.
![](https://github.com/MarioLeguizamo/MarioPython-ArcadeLibrary/blob/master/assets/Images/marioTutorial3.png)
