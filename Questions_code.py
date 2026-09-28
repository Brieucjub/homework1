import numpy as np
import math
import matplotlib.pyplot as plt

# =====================================================================
# Paramètre global de l'exercice
# =====================================================================
lambda_star = 3.0


# =====================================================================
# Q2 : Génération de données (Loi de Poisson)
# =====================================================================

def generer_poisson_knuth_unitaire(lam):
    """
    Génère une unique variable aléatoire suivant une loi de Poisson 
    de paramètre lam en utilisant la méthode de Knuth.
    """
    L = math.exp(-lam)
    k = 0
    p = 1.0
    
    while True:
        p *= np.random.uniform(0.0, 1.0)
        if p <= L:
            break
        k += 1
        
    return k

def generer_echantillon_poisson_knuth(lam, taille):
    """
    Génère un échantillon de variables aléatoires de Poisson via Knuth.
    """
    return np.array([generer_poisson_knuth_unitaire(lam) for _ in range(taille)])

# Démonstration de la méthode de Knuth pour Q2
N_q2 = 1000
donnees_X_knuth = generer_echantillon_poisson_knuth(lambda_star, N_q2)



# =====================================================================
# Q4 : Estimateur et distribution empirique
# =====================================================================

# Partie 1 : Convergence et erreur absolue

valeurs_N_conv = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

estimations_lambda = []
erreurs_absolues = []

for n_courant in valeurs_N_conv:
    # Justification numérique : La méthode de Knuth étant de complexité O(N * lambda),
    # l'utilisation de np.random.poisson (optimisée en C) est mathématiquement 
    # et informatiquement requise pour de grands échantillons.
    echantillon = np.random.poisson(lambda_star, n_courant)
    
    lambda_chapeau = np.mean(echantillon)
    erreur = np.abs(lambda_chapeau - lambda_star)
    
    estimations_lambda.append(lambda_chapeau)
    erreurs_absolues.append(erreur)

# Modélisation graphique
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(valeurs_N_conv, estimations_lambda, marker='o', linestyle='-', color='blue', label=r"Estimateur $\hat{\lambda}$")
ax1.axhline(y=lambda_star, color='red', linestyle='--', label=r"Valeur Théorique $\lambda^{*}$")
ax1.set_xscale('log')
ax1.set_xlabel(r"$N$")
ax1.set_ylabel(r"Estimateur $\hat{\lambda}$")
ax1.set_title(r"Convergence de l'estimateur de Poisson")
ax1.legend()
ax1.grid(True, which="both", ls="--", alpha=0.5)

ax2.plot(valeurs_N_conv, erreurs_absolues, marker='s', linestyle='-', color='purple')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel(r"$N$")
ax2.set_ylabel(r"Erreur absolue $|\hat{\lambda} - \lambda^{*}|$")
ax2.set_title(r"Décroissance de l'erreur absolue")
ax2.grid(True, which="both", ls="--", alpha=0.5)

plt.tight_layout()
plt.savefig('convergence_poisson.png', dpi=300)
plt.close() 


# Partie 2 : Distribution empirique

M_dist = 10000 
valeurs_N_dist = [10, 50, 100, 500, 1000] 

plt.figure(figsize=(10, 6))

for n_courant in valeurs_N_dist:
    matrice_echantillons = np.random.poisson(lambda_star, (M_dist, n_courant))
    vecteur_estimateurs = np.mean(matrice_echantillons, axis=1)
    
    plt.hist(vecteur_estimateurs, bins=50, density=True, alpha=0.6, 
             label=r"$N = {}$".format(n_courant))

plt.axvline(x=lambda_star, color='red', linestyle='dashed', linewidth=2, label=r"Valeur théorique ($\lambda^{*}$)")
plt.xlabel(r"Valeur de l'estimateur $\hat{\lambda}_{N}$")
plt.ylabel(r"Densité de probabilité empirique")
plt.title(r"Distribution empirique de l'estimateur de Poisson")
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('distribution_empirique.png', dpi=300)
plt.close()


# =====================================================================
# Q5 : Vérification numérique du Théorème Central Limite
# =====================================================================

# Fixation stricte des paramètres pour l'analyse locale
N_tcl = 1000
M_tcl = 100000

echantillons_tcl = np.random.poisson(lambda_star, (M_tcl, N_tcl))
lambda_hat_tcl = np.mean(echantillons_tcl, axis=1)

plt.figure(figsize=(10, 6))

plt.hist(lambda_hat_tcl, bins=75, density=True, alpha=0.5, color='steelblue', 
         edgecolor='black', label=r"Distribution empirique de $\hat{\lambda}_{N}$")

# Modélisation théorique
mu = lambda_star
sigma = np.sqrt(lambda_star / N_tcl)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

plt.plot(x, y, color='red', linewidth=2.5, 
         label=r"Densité théorique $\mathcal{N}\left(\lambda^{*}, \frac{\lambda^{*}}{N}\right)$")

plt.xlabel(r"Valeur de l'estimateur $\hat{\lambda}_{N}$")
plt.ylabel(r"Densité de probabilité")
plt.title(r"Vérification numérique du Théorème Central Limite ($N = {}$)".format(N_tcl))
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('verification_tcl_q5.png', dpi=300)
plt.close()