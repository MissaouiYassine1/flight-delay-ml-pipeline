import streamlit as st
import requests

# 1. Design de la page
st.title("✈️ Prédiction de Retard de Vol")
st.write("Bienvenue sur l'application. Veuillez entrer les caractéristiques du vol :")

# 2. Les widgets d'entrée utilisateur
age = st.number_input("Âge du pilote", min_value=18, max_value=80, value=40)
distance = st.number_input("Distance du vol (en km)", min_value=100.0, max_value=10000.0, value=1500.0)

# 3. Le bouton d'action
if st.button("Prédire le retard"):
    
    # On prépare le "colis" (dictionnaire) à envoyer à FastAPI
    donnees_a_envoyer = {
        "age_pilote": age,
        "distance_km": distance
    }
    
    try:
        # On fait la requête POST vers ton serveur FastAPI
        reponse = requests.post("http://127.0.0.1:8000/predictions", json=donnees_a_envoyer)
        
        # Si la requête a réussi (statut 200)
        if reponse.status_code == 200:
            resultat = reponse.json()
            st.success(f"Prédiction réussie ! Résultat de l'IA : {resultat['prediction_retard']}")
        else:
            st.error("Erreur lors de la communication avec l'API.")
            
    except requests.exceptions.ConnectionError:
         st.error("🚨 Impossible de joindre l'API. Le serveur FastAPI (Uvicorn) est-il bien allumé ?")