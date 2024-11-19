v1=float(input("Inserisci il primo voto: "))
v2=float(input("Inserisci il secondo voto: "))
v3=float(input("Inserisci il terzo voto: "))
decCen=int(input("Digita 1 se vuoi visualizzare la media in decimi, 2 in centseimi: "))
if decCen==1:
    print(f"La media in decimi è {(v1+v2+v3)/3}")
elif decCen==2:
    print(f"La media in centesimi è {(v1+v2+v3)/0.3}")
else:
    print("Valore non valido")