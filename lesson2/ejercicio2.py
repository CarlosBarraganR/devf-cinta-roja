# Multiplication tables example for 1 to 10 with For ... in with range
for index in range(1, 11):
    print "La tabla del " + str(index)
    for index2 in range(1,11):
        print str(index) + " X " + str(index2) +  " = " + str(index * index2)