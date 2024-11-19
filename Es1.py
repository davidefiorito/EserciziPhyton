anni=int(input("Quanti anni di servizio? "))
lv=int(input("Qual è il livello del programmatore? "))
if anni==1:
    if lv==1:
        print("Il bonus di produttività è 100.")
    elif lv==2:
        print("Il bonus di produttività è 200.")
    elif lv==3:
        print("Il bonus di produttività è 300.")
    else:
        print("Livello non valido.")
elif anni>1 and anni<=3:
    if lv==1:
        print("Il bonus di produttività è 200.")
    elif lv==2:
        print("Il bonus di produttività è 300.")
    elif lv==3:
        print("Il bonus di produttività è 400.")
    else:
        print("Livello non valido.")
elif anni>3 and anni<=5:
    if lv==1:
        print("Il bonus di produttività è 300.")
    elif lv==2:
        print("Il bonus di produttività è 400.")
    elif lv==3:
        print("Il bonus di produttività è 500.")
    else:
        print("Livello non valido.")
elif anni>5 and anni<=7:
    if lv==1:
        print("Il bonus di produttività è 400.")
    elif lv==2:
        print("Il bonus di produttività è 500.")
    elif lv==3:
        print("Il bonus di produttività è 600.")
    else:
        print("Livello non valido.")
elif anni>7:
    if lv==1:
        print("Il bonus di produttività è 500.")
    elif lv==2:
        print("Il bonus di produttività è 600.")
    elif lv==3:
        print("Il bonus di produttività è 700.")
    else:
        print("Livello non valido.")
else:
    print("Valore non valido.")