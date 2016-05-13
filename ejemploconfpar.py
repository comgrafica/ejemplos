import ConfigParser

archivo="inicial.map"
externo= ConfigParser.ConfigParser()
print "antes de leer el archivo"
print externo.sections()

externo.read(archivo)
print "despues de leer el archivo"
print externo.sections()

s1= externo.get("@", "pared")
print s1

mapa = externo.get("nivel","mapa").split("\n")
for nf, filas in enumerate(mapa):
   print nf, filas
   
indice={}
for seccion in externo.sections():
  #print "longitud:", len(seccion)
  print seccion
  if len(seccion) == 1:
       desc = dict(externo.items(seccion))
       indice[seccion] = desc
       print desc

print "llaves:", indice.keys()
print indice['#']['fondo']

ancho = len(mapa[0])
alto = len(mapa)
print "ancho:", ancho, "alto:", alto
print "posicion (2,2):", mapa[2][2]
print "posicion (0,2):", mapa[0][2]

info=[]
try:
  char = mapa[2][8]
  print char
except IndexError:
  print "error en posicin del mapa"
try:
  info = indice[char]
  print info
except KeyError:
  print "error en caracter llave"
t="tipo"
print info[t]







