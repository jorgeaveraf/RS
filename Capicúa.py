numero = int ( input ( ' Digite un número entero positivo : ' ) )
if numero >= 0 :
    if str ( numero ) == str ( numero ) [ :: - 1 ] :
        print ( '% i es capicúa. ' % numero )
    else : print (' % i no es capicúa. ' % numero )
else : print("Ingrese un número entero positivo")