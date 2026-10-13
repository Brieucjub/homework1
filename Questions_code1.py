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




    