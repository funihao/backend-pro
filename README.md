Repositorio clases Backend-Pro de Mejorando.la
==============================================

Este repositorio comienza con la clase de Julian Amaya, "Django Revolutions Parte II", antes de comenzar con los "test".

La idea, a partir de aquí, es crear commits de acuerdo al avance de las clases, de tal forma que uno pueda engancharse al inicio de una clase o de un tema de una clase, sin mas que situarse en el commit apropiado.

**AVISO**, esto es una prueba, no obstante espero que a medida que avanzo en el curso pueda ir dejando las suficientes migas (commits) para poder cumplir con la idea inicial.

**Sería magnifico que este repositorio comenzase con la primera clase de Harvey ...**


Requisitos
==========

El archivo **requirements.txt** contiene todos los paquetes que tienen que tener instalados para que todo funcione.

Se trabaja en un entorno virtual en el que se instalan y configuran los distintos paquetes, **ver "Guía de comienzo rápido"**.


Paquetes y versiones
--------------------

- **python3** and **pip3**
- **virtualenv and virtualenvwrapper**
  Estos requisistos son previos y obvios para poder trabajar con Django y crear entornos virtuales
- **Django==1.7.1**             #
- **Pillow==2.6.1**             # Librería de tratm. imagenes
- **Werkzeug==0.9.6**           # Debug en el navegador
- **argparse==1.2.1**           #
- **django-grappelli==2.6.3**   # Tema admin de django
- **django-extensions==1.4.9**  # Comandos extendidos, necesario para Werkzeug
- **ipdb==0.8**                 # Herramienta de debug (import ipdb... en el código)
- **ipython==2.3.1**            #
- **six==1.8.0**                #
- **tablib==0.10.0**            # Librería para exportar a excel, csv,..
- **wsgiref==0.1.2**            #


Guía de comienzo rápido
=======================

Esta guía no pretende ser un tutorial de python, así pués se entiende que se tienen suficientes conocimientos básicos del lenguaje y de como instalar paquetes.


Crear un entorno virtual
------------------------

Si se desconoce como crear entornos virtuales en python con **virtualenv** y **virtualenvwrapper**, recomiendo ver alguno de los tutoriales que se pueden encontrar en la red, por ejemplo:

- Tutorial de Python virtualenvwrapper de [Rukbottoland.com](http://rukbottoland.com/blog/tutorial-de-python-virtualenvwrapper/).
- Tutorial de Django de [Marina Mele](http://www.marinamele.com/taskbuster-django-tutorial/taskbuster-working-environment-and-start-django-project).


Descarga el proyecto de "backend-pro"
-------------------------------------

Descarga el proyecto desde GitHub, como un archivo zip o  usando la terminal:

    $ git clone git://github.com/funihao/backend-pro.git

Esto descargará el repositorio en el directorio actual.


