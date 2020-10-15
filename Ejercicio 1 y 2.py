nombre = input ("Introduzca un nombre: ")           #INPUT NOMBRE (STR)
Nota1 = float (input ("Introduzca una nota: "))     #INPUT NOTA 1 (FLOAT)
Nota2 = float (input ("Introduzca otra nota: "))    #INPUT NOTA 2 (FLOAT)

media = (Nota1+Nota2)/2     #CALCULO MEDIA (FLOAT)
Aprueba = (media>=5)        #BOOLEAN CONDICIÓN: MEDIA>=5

print ("La nota media de",nombre,"es",media)        #OUTPUT
print ("Aprueba la asignatura:",Aprueba)        #OUTPUT