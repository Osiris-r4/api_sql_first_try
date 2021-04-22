# BBDD Scripts Visualization with Flask

Para visualizar el programa tienes que: 

1) clonear el repositorio 

https://github.com/Osiris-r4/api_sql_first_try.git


2)  - Navegar en la terminal hasta el repositiorio y correr *python app_sql.py*

    - VS Code: ejecutar la pestaña *python app_sql.py*


## Diferentes Rutas

1) Para Visualizar toda la base da datos en formato Json en tu    local Host 

        http://127.0.0.1:5000/monthypython/all




2) Se visualizaran todos los episodios numero 10, puedes cambiar 10 por el numero de episodio que quieras. Si el Num de episodio no existe devuelve un dicionario vacio

        http://127.0.0.1:5000/monthypython/all/filters?episode=10




3) Visualizar los episodios numeros 10 que el character sea "Man" , otras opciones : ""It's Man" , ""Voice Over", "Wife" , "Robber", "Assistant" , "Mr Vercotti", etc.. 

        http://127.0.0.1:5000/monthypython/all/filters?episode=10&character=Man



4) Visualizar episodios 10, character Wife y tipo dialogo , otras opciones : "Direction"

        http://127.0.0.1:5000/monthypython/all/filters?episode=10&character=Wife&type=Dialogue






- Despues de filters?, puedes filtrar por los tres, por dos, por uno Etc. Son combinables pero siempre siguiendo el orden de episode, character y type.


Espero que os ayude para empezar a visualizar los cosas que se pueden hacer con flask, Api con sus distintos Metododos, los mas imp (Get y post) los requests etc..

- GET (Consultar la Api)
- POST (Añadir a la Api)
