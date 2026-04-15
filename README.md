# ✈️ Prédiction de Retard de Vol (End-to-End Big Data Pipeline)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PySpark](https://img.shields.io/badge/PySpark-MLlib-E25A1C.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B.svg)

## 📖 À propos du projet

Ce projet est une application complète (End-to-End) de Machine Learning et de Big Data, conçue pour prédire si un vol subira un retard en fonction de ses caractéristiques (âge du pilote, distance du vol, etc.). 

Il démontre l'intégration réussie de plusieurs technologies modernes de la Data : du traitement de données distribué à la création d'une interface utilisateur, en passant par le déploiement d'une API robuste.

## 🏗️ Architecture Technique

L'application repose sur une architecture en 3 tiers :

1. **Le Modèle IA (PySpark MLlib) :** Un modèle de classification (`LogisticRegression`) entraîné sur des données massives via le moteur distribué Apache Spark, capable de vectoriser les caractéristiques en temps réel.
2. **Le Backend (FastAPI & Pydantic) :** Une API REST ultra-rapide servant de pont entre l'interface et le modèle Spark. Les données entrantes sont sécurisées et validées grâce à Pydantic.
3. **Le Frontend (Streamlit) :** Une interface utilisateur web interactive permettant de saisir les paramètres du vol et d'afficher le résultat de l'algorithme instantanément.

## ⚙️ Prérequis et Installation

Assurez-vous d'avoir Python 3.10 installé sur votre machine.

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/MissaouiYassine1/flight-delay-ml-pipeline.git](https://github.com/MissaouiYassine1/flight-delay-ml-pipeline.git)
   cd nom-du-repo
Installer les dépendances :

Bash
pip install -r requirements.txt
(Assurez-vous que votre environnement contient pyspark, fastapi, uvicorn, pydantic, streamlit, et requests).

🚀 Utilisation (En local)
Pour faire fonctionner l'application, vous devez lancer le serveur (Backend) et l'interface (Frontend) simultanément dans deux terminaux différents.

1. Lancer l'API (FastAPI) :
Dans le premier terminal, exécutez :

Bash
python mon_api.py
(L'API sera disponible sur https://www.google.com/search?q=http://127.0.0.1:8000 et la documentation Swagger sur /docs)

2. Lancer l'interface (Streamlit) :
Dans un second terminal, exécutez :

Bash
streamlit run mon_app.py
(L'interface s'ouvrira automatiquement dans votre navigateur sur le port 8501)

📁 Structure du projet
Plaintext
├── mon_api.py               # Serveur Backend (FastAPI + Chargement Spark)
├── mon_app.py               # Interface Utilisateur (Streamlit)
├── modele_vol_retard/       # Dossier contenant les poids du modèle PySpark MLlib
├── requirements.txt         # Liste des librairies Python nécessaires
└── README.md                # Documentation du projet

### 👨‍💻 Auteur
##### Yassine Missaoui
