#programa para adivinar entre dos jugadores una fruta 
from random import*

#input
X = input( " jugador uno por favor poner el nombre del estudiante a elegir : ")
Y = input( " jugador dos por favor poner el nombre del estudiante a elegir : ")

#processing and ouput 
Z = choice (["angelica" , "sebastian" , "dorian" , "zury"])

if X == Z and Y == Z:
    print( " los dos jugadores han adivino el nombre del estudiante  " , Z ,)
elif X == Z:
    print( " solo el jugador uno ha adivino el nombre del estudiante  " , Z ,)
elif Y == Z:
    print( " solo el jugador dos ha adivinado el nombre del estudiante  " , Z ,)
else:
    print( " ninguno de los dos ha adivino el nombre del estudiante a elegir " , Z ,)