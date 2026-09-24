import numpy as np
import math
import matplotlib.pyplot as plt

#Q2

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

# Cette méthode fonctionne correctement, mais elle est moins efficace que l'utilisation de np.random.poisson pour de grandes tailles d'échantillon. Pour lambda_star = 3 et N = 1000, la méthode de Knuth est suffisante pour générer les données.




#Q4

# 1. Initialisation des paramètres
lambda_star = 3.0
# Définition d'un tableau de valeurs pour N (de 10 à 100 000)
valeurs_N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

# Création des listes vides pour stocker les résultats calculés
estimations_lambda = []
erreurs_absolues = []

# 2. Boucle de génération et de calcul
for N in valeurs_N:
    # Génération de l'échantillon de taille N. Comme la méthode de Knuth est moins efficace pour de grandes tailles d'échantillon, on utilise np.random.poisson pour générer les données.
    echantillon = np.random.poisson(lambda_star, N)
    
    # Calcul de l'estimateur (moyenne empirique)
    lambda_chapeau = np.mean(echantillon)
    
    # Calcul de l'erreur absolue
    erreur = np.abs(lambda_chapeau - lambda_star)
    
    # Stockage des résultats dans les listes
    estimations_lambda.append(lambda_chapeau)
    erreurs_absolues.append(erreur)

# 3. Représentations graphiques

# Création d'une figure avec deux sous-graphiques (1 ligne, 2 colonnes)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Graphique 1 : Convergence de lambda_chapeau vers lambda_star
ax1.plot(valeurs_N, estimations_lambda, marker='o', linestyle='-', color='blue', label=r"Estimateur $\hat{\lambda}$")
ax1.axhline(y=lambda_star, color='red', linestyle='--', label=r"Valeur Théorique $\lambda^{*}$")
ax1.set_xscale('log') # Échelle logarithmique pour l'axe des N
ax1.set_xlabel(r"$N$")
ax1.set_ylabel(r"Estimateur $\hat{\lambda}$")
ax1.set_title(r"Convergence de l'estimateur de Poisson ")
ax1.legend()
ax1.grid(True, which="both", ls="--", alpha=0.5)

# Graphique 2 : Évolution de l'erreur absolue
ax2.plot(valeurs_N, erreurs_absolues, marker='s', linestyle='-', color='purple')
ax2.set_xscale('log')
ax2.set_yscale('log') # L'erreur décroît, une échelle log-log est pertinente
ax2.set_xlabel(r"$N$")
ax2.set_ylabel(r"Erreur absolue | $\hat{\lambda}$ - $\lambda^{*}$|")
ax2.set_title(r"Décroissance de l'erreur absolue")
ax2.grid(True, which="both", ls="--", alpha=0.5)

# Affichage global
plt.tight_layout()
plt.show()
# Exportation du graphe au format PNG avec une haute résolution
plt.savefig('convergence_poisson.png', dpi=300)


# 2eme sous partie de Q4
M = 10000  # Nombre de répétitions pour l'estimation de la distribution empirique
valeurs_N_2 = [10, 50, 100, 500, 1000]  # Valeurs de N pour lesquelles on veut observer la distribution
plt.figure(figsize=(10, 6))

# 3. Boucle itérative sur les différentes valeurs de N
for N in valeurs_N_2:
    
    # 4. Génération optimisée : matrice de M lignes et N colonnes
    # Chaque ligne est un échantillon indépendant de taille N
    matrice_echantillons = np.random.poisson(lambda_star, (M, N))
    
    # 5. Calcul de la moyenne sur l'axe des colonnes (axis=1)
    # Résultat : un vecteur de dimension M contenant les estimateurs lambda_chapeau
    vecteur_estimateurs = np.mean(matrice_echantillons, axis=1)
    
    # 6. Création de l'histogramme pour la valeur N courante
    # density=True normalise l'aire de l'histogramme à 1
    # alpha=0.6 gère la transparence pour superposer les graphiques
    plt.hist(vecteur_estimateurs, bins=50, density=True, alpha=0.6, 
             label=r"$N = {}$".format(N))

# Paramétrage du rendu graphique
plt.axvline(x=lambda_star, color='red', linestyle='dashed', linewidth=2, 
            label=r"Valeur théorique ($\lambda^{*}$)")
plt.xlabel(r"Valeur de l'estimateur $\hat{\lambda}_{N}$")
plt.ylabel(r"Densité de probabilité empirique")
plt.title(r"Distribution empirique de l'estimateur de Poisson")
plt.legend()
plt.grid(True, alpha=0.3)

# Exportation du graphique
plt.savefig('distribution_empirique.png', dpi=300)




#Q5

