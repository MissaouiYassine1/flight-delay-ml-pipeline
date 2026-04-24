import csv
import random

# Création d'un fichier CSV avec 1 000 000 de lignes
with open('vols_data_massive.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Écrire l'en-tête
    writer.writerow(['id_vol', 'age_pilote', 'distance_km', 'cible_retard'])
    
    # Générer 1 000 000 de lignes
    for i in range(1, 1000001):
        # Générer des données réalistes
        age_pilote = random.randint(22, 65)  # Âge entre 22 et 65 ans
        distance_km = random.randint(300, 5000)  # Distance entre 300 et 5000 km
        
        # La cible (retard) dépend logiquement de la distance et de l'âge
        # Plus la distance est grande, plus le risque de retard est élevé
        # Les pilotes très jeunes ou très âgés ont plus de risques
        probabilite_retard = 0
        
        # Facteur distance
        if distance_km > 3000:
            probabilite_retard += 0.4
        elif distance_km > 2000:
            probabilite_retard += 0.25
        elif distance_km > 1000:
            probabilite_retard += 0.15
        else:
            probabilite_retard += 0.05
            
        # Facteur âge
        if age_pilote < 30 or age_pilote > 55:
            probabilite_retard += 0.2
        elif age_pilote < 35 or age_pilote > 50:
            probabilite_retard += 0.1
            
        # Ajouter un peu d'aléatoire
        probabilite_retard += random.uniform(-0.1, 0.1)
        
        # Déterminer la cible (0 ou 1) selon la probabilité
        cible_retard = 1 if random.random() < probabilite_retard else 0
        
        # Écrire la ligne
        writer.writerow([i, age_pilote, distance_km, cible_retard])
        
        # Afficher la progression toutes les 100 000 lignes
        if i % 100000 == 0:
            print(f"{i} lignes générées...")

print("✅ Fichier CSV généré avec 1 000 000 de lignes !")