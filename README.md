# Proyecto Final Gil Mariano

Este es el readme del proyecto Final de Gil Mariano.

## Barra de navegación

- Inicio: te lleva a la página principal donde se encuentran los dos posteos más recientes de todos los pescadores.
- Todas las Pescas: te permite acceder a una vista general de todos los posteos. Si haces clic en el botón "detalle", se mostrará información adicional.
- Iniciar Sesión: te lleva al sistema de inicio de sesión para usuarios registrados.
- Registrarme: te lleva al sistema de registro para nuevos usuarios.
- Enviar Mensaje: te permite enviar mensajes a otros usuarios del blog, independientemente de si están registrados o no.
- Acerca de: te muestra información general sobre el blog.

## Funcionalidades disponibles para usuarios registrados

Una vez registrado y logueado en tu cuenta, podrás acceder a las siguientes funcionalidades adicionales:

- Cargar Pesca: te permite cargar una nueva pesca.
- Mis Pescas: te muestra todos los posteos que has creado.
- Perfil: te permite cargar una imagen y utilizarla como avatar en tu perfil.
- Mis Mensajes: te muestra todos los mensajes que has recibido.
- Logout: te permite cerrar sesión.

Esperamos que disfrutes de nuestro blog de pesca creado con Django. Si tienes alguna pregunta o sugerencia, no dudes en contactarnos. ¡Gracias por utilizar nuestro sitio!

## Instrucciones de instalación y configuración
Para poder correr este proyecto es necesario tener instalado python 3.9 o superior. 

### Paquetes necesarios para la instalación
Desde la terminal correr el siguiente comando
```bash
pip3 install django
```

### Cargar datos de pruebas

Para terminal bash en windows/linux/macos:
```bash
python3 manage.py shell < seed_data.py
```

Para terminal cmd/powershell en windows:
Primero entrar al shell de django con
```bash
python3 manage.py shell
```
Una vez en el shell hacer import seed_data
```bash
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import seed_data
```

### Para poder correr el servidor 

Desde la terminal correr el siguiente comando

```bash
python3 manage.py runserver
```