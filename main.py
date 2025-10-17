import math

def solveur_equation():
    """
    Ce programme résout une équation du second degré de la forme ax² + bx + c = 0.
    """
    print("--- Solveur d'équation du second degré (ax² + bx + c = 0) ---")

    # Demander les coefficients à l'utilisateur
    try:
        a = float(input("Entrez la valeur de a : "))
        b = float(input("Entrez la valeur de b : "))
        c = float(input("Entrez la valeur de c : "))
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")
        return

    # Calculer le discriminant (delta)
    delta = (b**2) - (4*a*c)

    print(f"\nLe discriminant (delta) est : {delta}")

    # Analyser la valeur de delta et trouver les solutions
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"L'équation a deux solutions réelles distinctes :")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x0 = -b / (2*a)
        print(f"L'équation a une unique solution réelle :")
        print(f"x0 = {x0}")
    else: # delta < 0
        partie_reelle = -b / (2*a)
        partie_imaginaire = math.sqrt(-delta) / (2*a)
        print("L'équation n'a pas de solution réelle.")
        print("Les solutions complexes sont :")
        print(f"z1 = {partie_reelle} - {partie_imaginaire}i")
        print(f"z2 = {partie_reelle} + {partie_imaginaire}i")

# Lancer la fonction principale
if __name__ == "__main__":
    solveur_equation()