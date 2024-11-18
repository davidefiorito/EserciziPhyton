fascine=int(input("Fascine acquistate: "))
sacchi=int(input("Sacchi acquistati: "))
bancali=int(input("Bancali acquistati: "))
fascine=fascine*5
sacchi=sacchi*20
bancali=bancali*50
tot=fascine+sacchi+bancali
print(f"Peso totale: {tot} kg")
prezzo=round(tot*0.8,1)
print(f"Prezzo della legna senza sconto: {prezzo}0 euro")
if tot>100:
  sconto=round(prezzo*0.15,1)
  prezzo=prezzo-sconto
else:
  sconto=0.00
print(f"Sconto applicato: {sconto}0 euro")
print("Spese di trasporto: 3 euro")
print(f"Prezzo finale su scontrino: {prezzo}0 euro")