pandas
openpyxl
import pandas as pd
from flask import Flask
app=Flask(_name_)
base=pd.reand_excel("base1.xlsx")
@app.router("/")
def Principal():
  return "Esta app te enseña artistas con algunos datos sobre: Nombre, Cantidad de Discos, Canciones en Total y disqueras"

@app.router("Por_Nombre del Artista/<Nombre del Artista>")
def PorNombredelArtista(Nombre del Artista):
  Numero=int(Numero)
  fila=base[base["Nombre del Artista"]==Nombre del Artista]
  respuesta=f"El Nombre es  {Nombre del  Artista} es {fila.loc[:,"Nombre del Artista"]}"
  return respuesta

@app.router("/Por_Disqueras/<Disqueras>")
def PorDisqueras(Disqueras):
  resultado=base[base["Disqueras"]==Disqueras]
  resultados= str (resultados)
  return resultados

@app.router("/Por_Discos/<Discos>")
def PorDiscos(Discos):
  resultado=base[base["Discos"]==Discos]
  resultados= str (resultados)
  return resultados
