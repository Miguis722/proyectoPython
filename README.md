# Proyecto-Python
1. Creación del archivo de MAIN, gitnore y las carpetas donde iran cada uno de los procesos y/o información necesaria durante el desarrollo
2. Ponemos a prueba el menú y añadimos las distintas opciones a seleccionar. Además de que añadimos documentación al código para entenderlo despues.
3. Inicio del desarrollo del menú interactivo añadiendo de documentación
4. Agregamos el primer documento en Storage con toda la información
5. Empezamos con el apartado de documentación para hacer explicación de cada cosita que se va presentando o desarrollando durante el proyecto. Iniciamos la asignación de cada valor del menú
6. Se realiza el desarrollo de los diferentes procesos que necesitaremos a lo largo del proyecto, en estos vamos a hacer cada una de las consultas y/o asignaciones que se desean.
7. Centramos el menú principal
8. Se empieza a generar el caché automaticamente, para que la proxima vez que corramos un proceso, el computador lo pueda hacer de forma más rapida. Añadimos además explicación del proceso realizado.
9. Empezamos asignando el menú en cada uno de los submenús desarrollados, debido a que ACTIVOS, PERSONAL Y ZONAS, poseen el mismo formato, solo debemos de cambiar el nombre del menú.
10. Desarrollamos los SUBMENÚS de ACTIVOS, PERSONAL y ZONAS. En ellos pusimos las condiciones de que solo podemos escoger de 1 hasta 5, si escoge un número distinto dentro de ese rango, volvera a aparecer ese mismo menú hasta que se ingrese un número valido.
11. Importamos REQUESTS para poder visualizar y utilizar la información de un servidor en especifico, el cual nos proporcionara la Data que necesitamos.
12. Hacemos testeos comprobando que las funciones, hagan su respectiva acción. Empezamos el menú de get Asignación.
13. Actualización del README o tambien llamada documentación.
14. Actualizamos getReportes con nuevos menús, además de que le asignamos su respectivo servidor para conseguir toda la Data necesaria.
15. Actualizamos el menú de getMovimiento, le damos condicionales de menú y le asignamos su servidor.
16. Utilizamos el servidor donde se encuentra toda la información.
17. Creamos un filtro en Reportes para poder visualizar todo el Data disponible.
18. Añademos explicación del por que se está nombrando cierta funcion dentro del codigo. Además de que agregamos el primer filtro. Ya funciona el menú de getReportes (el número 5, 1), falta solucionar problemas. Añadiremos tambien documentación y explicación en menú.
19. Los headers de getReportes no sirven, seguimos tratando de encontrar solución eliminando algunos espacios.
20. Agregamos un nuevo modulo el cual se encargara de cada una de las categorias. Colocamos un nuevo filtro en getReportes, en el cual se debera seleccionar la categoria que se desea filtrar para ver. Además de que hacemos su respectivo print o visualización al usuario. NOTA: He decidido agregar un ("clear"), debido a que los demás usuarios puede que no usen windows pero si linux, entonces el comando no funcionaria, por lo que previniendo ese error y problema, he agregado el comando de LINUX. Además, He decidido hacer que el Usuario escoja cual es la categoria que desea ver para hacerlo más facil de entender y visualizar.
21. He agregado dos nuevos filtros al menú de reportes, el cual corresponde a listar a los que están bajados por daño y, al de listar los activos y a quien está asignado. Actualizamos el menú de reportes.
22. Realize el ultimo filtro dentro de REPORTES, además de que edite  los menús de Reportes debido a que se estaban ocultando los comentarios realizados para explicar la funcionalidad de cada uno. Y uno que otro espacio entre ellos para ser más facil la visualización
23. Cree una nueva carpeta llamada "Activos", con el fin de que está almacene todo  lo referente a los activos. Para hacer más facil para mi un control de lo que toca hacer en cuanto a procesos, decidi crear un archivo python para que se encargue de cada funcion, si hay un eliminar, este tiene su propio python aparte. Actualice el menú principal porque al cambiar de dirección el getActivos a la carpeta, si lo hubiera corrido sin haberlo cambiado se hubiera dañado el codigo y dejaria de funcionar. Agregamos el servidor en cada uno de los archivos de ACTIVOS. Vamos en proceso de EDITAR (crudActivos), en el cual ya llevo 4 datos a poder modificar, falta agregar el resto, por ahora, todo funciona. Además de que puse al final una condicion de que si queria seguir editanto más datos o no.