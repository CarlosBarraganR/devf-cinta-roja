#IP Filter

"""
    ip_filter(input)
    
    Validates if the string provided is a valid ip address
"""
def ip_filter(input):
    if len(input) > 0 and len(input.split(".")) < 5:

        ip_list = input.split(".")
        ip_list = map(int, ip_list)
        print ip_list

        for ip in ip_list:
            if ip < 256:
                print "IP Valida"
            else:
                print "IP invalida: Error en la IP por el numero es mayor a 255..., numero incorrecto: " + str(ip)
                break
    else:
        print "Error en la IP, verifica el dato."


ip_input = raw_input("Inserta la Direccion IP: ")
ip_filter(ip_input)
