import os
import gzip

fichiers = ['uniform.txt', 'half.txt', 'abcd.txt', 'abcd2.txt']

entropies_theoriques = [8.0, 7.0, 2.0, 1.75]

print("Comparaison des performances de compression")
print("-" * 85)
print(f"{'Fichier':<15} | {'Taille Init. (o)':<16} | {'Taille Comp. (o)':<16} | {'Ratio Exp.':<12} | {'Ratio Théo.':<12}")
print("-" * 85)

for fichier, H in zip(fichiers, entropies_theoriques):
    if not os.path.exists(fichier):
        print(f"Erreur : Le fichier '{fichier}' est introuvable. Place-le dans le même dossier que le notebook.")
        continue

    taille_initiale = os.path.getsize(fichier)

    fichier_compresse = fichier + '.gz'
    with open(fichier, 'rb') as f_in:
        with gzip.open(fichier_compresse, 'wb') as f_out:
            f_out.writelines(f_in)

    taille_compressee = os.path.getsize(fichier_compresse)

    ratio_experimental = taille_initiale / taille_compressee

    ratio_theorique = 8.0 / H

    print(f"{fichier:<15} | {taille_initiale:<16} | {taille_compressee:<16} | {ratio_experimental:<12.2f} | {ratio_theorique:<12.2f}")

    os.remove(fichier_compresse)


import numpy as np

freqs_lettres = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
    'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
    'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974,
    'z': 0.00074
}

probabilites = np.array(list(freqs_lettres.values()))
probabilites = probabilites / np.sum(probabilites)
entropie_anglais = -np.sum(probabilites * np.log2(probabilites))
ratio_compression = 8.0 / entropie_anglais

print(f"Entropie de l'anglais (26 lettres) : {entropie_anglais:.3f} bits/caractère")
print(f"Rapport de compression théorique   : {ratio_compression:.3f}")




taille_initiale_octets = 1_000_000_000  
taille_compressee_record = 100_424_672

ratio_hutter = taille_initiale_octets / taille_compressee_record
bits_par_caractere_hutter = 8.0 / ratio_hutter

entropie_q1 = entropie_anglais
ratio_q1 = ratio_compression

print("=== Comparaison des performances de compression ===")
print(f"1. Modèle théorique Q1 (Ordre 0) : {entropie_q1:.3f} bits/lettre | Ratio = {ratio_q1:.2f}")
print(f"2. Record Hutter Prize (IA)      : {bits_par_caractere_hutter:.3f} bits/lettre | Ratio = {ratio_hutter:.2f}")
print("-" * 65)
print(f"-> Le Hutter Prize compresse environ {ratio_hutter / ratio_q1:.1f} fois mieux que notre limite théorique.")




entropie_q1 = entropie_anglais 

entropie_exp_min = 1.2178
entropie_exp_max = 1.7921
entropie_exp_moyenne = (entropie_exp_min + entropie_exp_max) / 2

print("=== Expérience de Shannon (cerveau humain) ===")
print(f"Entropie estimée : entre {entropie_exp_min} et {entropie_exp_max} bits/caractère")
print("-" * 65)
print(f"-> Le cerveau humain réduit l'incertitude d'un facteur {entropie_q1 / entropie_exp_moyenne:.1f} par rapport au calcul naïf d'ordre 0 !")