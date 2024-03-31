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
24. Decidi agregar una nueva función en la cual se nos muestre en vez de los números que corresponde a cada marca, el respectivo nombre de la marca. Para asi facilitar más procesos, Además de que puede que más adelante los utilicemos para otras funciones. Además de que agregue un nuevo filtro, el cual es la 6 e inicio con el desarrollo del nuevo filtro con el número 7. Además de que me tocó modificar en la parte del menú inferiror debido a que me daba error todo el tiempo el break, por lo que para solucionarlo decidi importarlo y hacer la respectiva funcion para ir al menú de getActivos ya que ese era el menú anterior, por lo que el break quedaria solucionado.
25. Agregamos más explicaciones a lo que hace el codigo para llevar un mejor control.  Además de que agregamos una función que se encargara de pasar de número de id a la marca y categoria que corresponde. Desarrollamos los ultimos filtros para poder modificar la información de un activo, para poder seguir adelante con las demás opciones del proyecto. Finalizamos el menú de EDITAR INFORMACIÓN DE UN ACTIVO.
26. Solucionamos algunos errores que se me pasaron por alto, se genera el caché, por lo que modificamos el gitnore. Además de corrección de espacios y errores (Problemas de tabulación) en crudActivos que hacia que no corriera el codigo de forma adecuada. Probamos el codigo para ver si funciona correcta y asi es, por lo que ya culminamos CRUDACTIVOS. Actualización de README.
27. Culminación de getActivos, ya está funcionando la función de buscar un activo por medio de su respectivo id o su número de item.
28. Agregamos algunas lineas de codigo debido a que estaban dando error, y porque puede que corran el programa desde un equipo LINUX, por lo que el comando ("cls") no funcionaria, por lo que lo corregimos agregando en caso de que se haga en otro equipo. Todo con relacionado con el CACHÉ se cambia de forma automatica por el computador, asi que no hace falta explicar los procesos de texto que están allí escritos.
29. En PostActivos  agregamos una función que nos permite agregar un nuevo activo. En main se me paso por alto el clear, por lo que lo agregue. Desarrollamos y culminamos el menú de PostActivos, es decir, el menú para poder crear un nuevo activo.
30. Falta arreglar el error de PostActivos debido a que despues del NroItem no pasa. Añadi además una opción por si el activo no tenia un serial en el.
31. Desarrollo de ELIMINAR un activo, pero como tal no es eliminar, sino que ponerle un codigo de no asignado, es decir que si esta activado, ponerle el estado de no asignado. Agrego además el link de donde estoy sacando los diseños para el menú y cruds.
32. Hacemos la carpeta de Personal, donde iran todos los procesos de PERSONAL, además cambiamos la ruta de dirección de main para que sepa que get personal ahora se encuentra en otra carpeta. Desarrolle un submenú en el menú de activos y en getpersonal debido a que pienso que si se llegasen a existir un millón de datos no le gustaria a una persona ver uno por uno, sino que solamente busca uno en especifico por medio de su ID o la cedula de ciudadania. Aunque tambien está la opción de enlistar a TODOS los del personal y activos.
33. Empezamos con la creación del menú de getPersonal, además importamos los archivos de python que usaremos (crud, del y post), además de que empezamos a encarpetar todos los demás procesos (asignacion, categoria, movimiento, zonas, etc.). Cambiamos main para indicarle al archivo python que ahora la información la está sacando de otra ubicación (es decir, del mismo archivo, pero que ese archivo se movio a otra carpeta).
34. Pasamos el codigo realizado por chat gpt para que verifique que todo está escrito bien y que no haya un error o una logica que pueda generar alguna interferencia con otra función, además de que practique el metodo KISS.
35. Desarrollamos el crud del Personal en el cual pedimos que el usuario ingrese el id (codigo del personal) y escoja que es lo que desea editar o agregar.
36. Desarrollamos el menúy para agregar a un personal nuevo a la base de datos, además le creamos el menú.