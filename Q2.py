import numpy as np
import math

def generer_poisson_knuth_unitaire(lambda_star):
    """
    Génère une unique variable aléatoire suivant une loi de Poisson 
    de paramètre lambda_star en utilisant la méthode de Knuth.
    """
    # Définition du seuil limite
    L = math.exp(-lambda_star)
    
    # Initialisation des variables
    k = 0
    p = 1.0
    
    # Boucle d'accumulation
    while True:
        p *= np.random.uniform(0.0, 1.0)
        if p <= L:
            break
        k += 1
        
    return k

def generer_echantillon_poisson(lambda_star, N):
    """
    Génère un échantillon de taille N de variables aléatoires de Poisson.
    """
    # Utilisation d'une compréhension de liste pour exécuter la routine N fois
    echantillon = [generer_poisson_knuth_unitaire(lambda_star) for _ in range(N)]
    return np.array(echantillon)

# Définition des paramètres de l'exercice
lambda_star = 3
N = 1000

# Génération des données
donnees_X = generer_echantillon_poisson(lambda_star, N)

