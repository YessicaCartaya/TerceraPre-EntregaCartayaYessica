# Nombre Proyecto: Viveros Verde es Vida
# Alumno: Yessica Cartaya
# Curso: Python
# Comision:50200
# Fecha: 07/02/2024
# Version: Tercera Pre-Entrega

# Aplicacion que permite registrar las plantas, Macetas y Fettilizantes disponiles en Stock para un Vivero

- Los modelos que posee esta aplicacion son:
    - Planta
    - Maceta
    - Fertilizante

- Prueba de la aplicacion: 
    - Se ingresa al http://localhost:8000/aplicacion/
    - Desde el Menu se selecciona las opciones:
        - Inicio:  Muestra el Home de la aplicacion, el cual contiene el diseño que se hereda en las demas opciones del Menu
                   y el nombre del proyecto
        - Plantas: Lleva al formulario para el registro de las plantas y la informacion de cada una (http://localhost:8000/aplicacion/planta_form/)
                   una vez completado el formulario al pulsar Enviar, lleva automaticamente a la ruta donde se muestra la informacion de todas
                   las plantas cargadas en la Base de Datos (http://localhost:8000/aplicacion/plantas/)
        - Macetas: Lleva al formulario para el registro de las Macetas y la informacion correspondiente a cada una (http://localhost:8000/aplicacion/maceta_form/)
                   una vez completado el formulario al pulsar Enviar, lleva automaticamente a la ruta donde se muestra la informacion de todas
                   las macetas cargadas en la Base de Datos (http://localhost:8000/aplicacion/macetas/)
        - Fertilizantes: Lleva al formulario para el registro de los Fertilizantes y la informacion correspondiente a cada uno (http://localhost:8000/aplicacion/fertilizante_form/)
                   una vez completado el formulario al pulsar Enviar, lleva automaticamente a la ruta donde se muestra la informacion de todos
                   los fertilizantes cargadas en la Base de Datos (http://localhost:8000/aplicacion/fertilizantes/)
        - Buscar:  lleva al formulario donde se realiza el patron de busqueda por nombre de planta (http://localhost:8000/aplicacion/buscar/)
                   al presionar buscar, realiza la buscada de las plantas existentes en la Base de Datos con ese patron de busqueda

