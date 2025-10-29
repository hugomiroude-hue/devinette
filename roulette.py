import random

def devinette_5_essais():
    nombre_secret = random.randint(1, 100)
    essais_restants = 5

    print("Bienvenue dans le jeu de la devinette !")
    print("Vous devez deviner un nombre entre 1 et 100.")
    print("Vous avez 5 essais.")

    while essais_restants > 0:
        try:
            proposition = int(input(f"Il vous reste {essais_restants} essais. Quelle est votre proposition ? "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if proposition < 1 or proposition > 100:
            print("Votre proposition doit être entre 1 et 100.")
            continue

        if proposition < nombre_secret:
            print("C'est plus grand !")
        elif proposition > nombre_secret:
            print("C'est plus petit !")
        else:
            print("Bravo ! Vous avez trouvé le nombre secret !")
            return

        essais_restants -= 1

    print(f"Désolé, vous avez épuisé vos essais. Le nombre secret était {nombre_secret}.")
if __name__ == "__main__":
    devinette_5_essais()
