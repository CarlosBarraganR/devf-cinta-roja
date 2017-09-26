#set de enteros
set_enteros = {1,2,3}

set_diferentes_datos = {1.0, "Hello", (1,2,3)}

my_set = {1,3}

def add_element_to_set():
    print my_set
    #add an Element
    my_set.add(2)
    print "Element Added, ", str(my_set)
    print my_set
    #add multiple elements on the set
    my_set.update([1,2,3])
    print "Elements " + str(my_set) + ", Added"
    print my_set
    my_set.add(7)
    print "Element Added, ", str(my_set)
    print my_set

def remove_element_from_set():
    print my_set
    #discard does nothing if it is not a member
    my_set.discard(1)

    # remove throws exception if it's not a member
    #my_set.remove(10)

def pop_elements_from_set():
    print my_set
    my_set.pop()
    print my_set


#add_element_to_set()
#remove_element_from_set()
pop_elements_from_set()