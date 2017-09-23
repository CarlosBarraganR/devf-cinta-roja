import math
#result = math.sqrt(math.pow(p2[0]-p1[0],2) + math.pow(p2[1]-p1[1],2))

point_1 = raw_input('Ingreso los valores del punto 1 en el siguiente formato P1 = x,y: ')
point_2 = raw_input('Ingreso los valores del punto 2 en el siguiente formato P2 = x,y: ')

point_1 = point_1.split(',')
point_2 = point_2.split(',')
point_1 = map(int, point_1)
point_2 = map(int, point_2)
vectors = [point_1, point_2]

print  vectors

def calculate_vector(p1, p2):
    if len(p1) != len(p2):
        print "Tamanhoos de puntos son diferentes"
    else:
        result = math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))
        print "La distancia euclidiana es: " + str(result)

calculate_vector(point_1,point_2)
