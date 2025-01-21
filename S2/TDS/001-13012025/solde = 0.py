solde = 0
while True :
    s = input()
    if not s :
        break
    values = s.split()
    operation = values[0]
    montant = int (values[1])
    if operation == "D" : 
        solde += montant
    elif operation == "R":
        solde -= montant
    else:
        print("Operation invalide")

print(solde)

    