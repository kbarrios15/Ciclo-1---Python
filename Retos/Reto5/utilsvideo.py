def peliculas_sin_repeticion(lista):
  resultado=[]
  for item in lista:
    if item not in resultado:
      resultado.append(item)
  return resultado


def pelicula_en_posiciones(posicion,lista,pelicula):
  posicion_seleccionada=[i for i,x in enumerate(lista) if x==pelicula]
  seleccion=[]
  for elemento in posicion_seleccionada:
    if elemento in posicion:
      seleccion.append(elemento)
  return seleccion


def solo_drama(drama,amor):
  es_drama=[]

  for pelicula in drama:
     if pelicula not in amor:
       es_drama.append(pelicula)
  return es_drama


def numero_cambios(usuario1,usuario2):

  cambios1=0
  cambios2=0

  for pelicula in usuario1:
    if pelicula not in usuario2:
        cambios1+=1
  for pelicula in usuario2:
    if pelicula not in usuario1:
        cambios2+=1
  if cambios1>cambios2:
    return cambios2 
  if cambios2>cambios1:
    return cambios1
  if cambios2==cambios1:
    return cambios1