l1=float(input("Inserisci la lunghezza del primo lancio: "))

l2=float(input("Inserisci la lunghezza del secondo lancio: "))

l3=float(input("Inserisci la lunghezza del terzo lancio: "))

l4=float(input("Inserisci la lunghezza del quarto lancio: "))

l5=float(input("Inserisci la lunghezza del quinto lancio: "))
if l3==0==l1==l2==l4==l5:
    n=1

elif l4==0:
    n=4
else:
    n=5
media=(l1+l2+l3+l4+l5)/n
print(media)