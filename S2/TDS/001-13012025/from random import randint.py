from random import randint

print(" Bienvenu dans notre jeu \n\n")

while True : 
    nombre = randint(1, 100)
    essai = 0
    while True :
        essai += 1
        proposition = int(input("Entrez un nombre entre 1 et 100 : "))
        if proposition < nombre : 
            print("Trop pétit")
        elif proposition > nombre :
            print("Trop grand")
        else :
            print(f"Bravo,vous avez trouvez le nombre en (essai) essais")
            break
        rejouer = input("Voulez-vous rejouer? (o\n)")
        if rejouer == "n":
            break