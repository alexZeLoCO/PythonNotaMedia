N1 = int (input ("Introduzca una nota:"))       #SOLICITA NOTA
N2 = int (input ("Introduzca una nota:"))       #SOLICITA NOTA
N3 = int (input ("Introduzca una nota:"))       #SOLICITA NOTA
N4 = int (input ("Introduzca una nota:"))       #SOLICITA NOTA
media = (N1+N2+N3+N4)/4     #CALCULA MEDIA
if media>=90:       #[90,100]
    print ("A")     #OUTPUT
elif media>=80:     #[80,90)
    print ("B")     #OUTPUT
elif media>=70:     #[70,80)
    print ("C")     #OUTPUT
elif media>=60:     #[60,70)
    print ("D")     #OUTPUT
else:               #[0,60)
    print ("E")     #OUTPUT