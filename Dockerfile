# iniciando de una imagen base
FROM        orchardup/python:2.7

# instalamos los requerimientos
RUN         pip install Flask

# copiamos el contenido del directorio actual
ADD         . /code

# nos movemos hacia el directorio copiado
WORKDIR     /code

# publicamos el puerto 5000
EXPOSE      5000

# iniciamos la aplicación
CMD         ["python", "app.py"]

#docker build -t leopic/componentes-servidor-python /Users/leo/Sites/componentes/servidorPython
#docker run --name servidor-python -p 4001:5000 -d -v /Users/leo/Sites/componentes/servidorPython:/src leopic/componentes-servidor-python
#docker logs -tf servidor-python
