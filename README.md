# ✈️ Flight Delay Prediction — End-to-End Big Data Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-MLlib-E25A1C.svg?style=for-the-badge&logo=apachespark&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![License: MIT](https://img.shields.io/badge/Licence-MIT-F7B731.svg?style=for-the-badge)

**Une application ML complète qui prédit les retards de vol en exploitant Apache Spark, FastAPI et Streamlit — du pipeline de données brutes jusqu'à l'interface utilisateur.**

[Démo](#-utilisation) · [Installation](#-installation) · [Architecture](#-architecture) · [Contact](#-contact)

</div>

---

## 📋 Table des Matières

- [À Propos](#-à-propos)
- [Architecture](#-architecture)
- [Technologies](#-technologies)
- [Structure du Projet](#-structure-du-projet)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Jeu de Données](#-jeu-de-données)
- [Roadmap](#-roadmap)
- [Contribution](#-contribution)
- [Licence](#-licence)
- [Contact](#-contact)

---

## 🚀 À Propos

Ce projet est une **application End-to-End de Machine Learning et Big Data**, conçue pour prédire si un vol subira un retard en fonction de ses caractéristiques (âge du pilote, distance du vol, etc.).

> 💡 **Problème résolu :** Les compagnies aériennes perdent des milliards chaque année à cause des retards. Ce modèle permet d'anticiper ces retards pour une meilleure planification opérationnelle.

### ✨ Points clés

- 🔥 **1 million de vols** traités avec Apache Spark
- ⚡ **API REST** ultra-rapide via FastAPI
- 🎨 **Interface web interactive** via Streamlit
- 🧠 **Modèle LogisticRegression** (PySpark MLlib)

**Public cible :** compagnies aériennes, aéroports, data scientists et développeurs souhaitant apprendre l'intégration de technologies Big Data dans une application ML.

---

## 🏗 Architecture

L'application repose sur une architecture **3-tiers** claire et découplée :

```
┌─────────────────────┐        HTTP POST        ┌──────────────────────┐
│  🎨 Streamlit        │ ──────────────────────► │  ⚡ FastAPI Backend   │
│     Frontend         │ ◄────────────────────── │  (api.py)            │
│  (app.py)            │      JSON Response       └──────────┬───────────┘
└─────────────────────┘                                      │ Charge
                                                             ▼
                                                ┌──────────────────────┐
                                                │  🧠 PySpark Model     │
                                                │  (MLlib LR)           │
                                                └──────────────────────┘
```

| Couche | Technologie | Rôle |
|--------|-------------|------|
| 🧠 **Modèle IA** | PySpark MLlib | Classification LogisticRegression sur 1M de vols |
| ⚡ **Backend** | FastAPI + Pydantic | API REST avec validation des données |
| 🎨 **Frontend** | Streamlit | Interface interactive de saisie et visualisation |

---

## 🛠 Technologies

| Catégorie | Technologies |
|-----------|-------------|
| **Big Data** | Apache Spark, PySpark MLlib |
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Frontend** | Streamlit, Requests |
| **Data Processing** | Pandas, NumPy |
| **Versioning** | Git, GitHub |
| **Langage** | Python 3.10+ |

---

## 📁 Structure du Projet

```
flight-delay-prediction/
│
├── 📄 api.py                      # API FastAPI (backend)
├── 📄 app.py                      # Interface Streamlit (frontend)
├── 📄 ml.py                       # Script d'entraînement du modèle
│
├── 📓 notebooks/                  # Scripts pédagogiques
│   ├── data.py                   # Introduction à Pandas
│   ├── dataset.py                # Manipulation de datasets
│   ├── gen_data.py               # Génération de données massives (1M lignes)
│   └── spark.py                  # Premiers pas avec PySpark
│
├── 🤖 modele_vol_retard/          # Modèle ML sauvegardé
│   ├── data/                     # Données transformées (ignorées par Git)
│   └── metadata/                 # Métadonnées Spark (ignorées par Git)
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Prérequis

- Python **3.10+**
- Git
- **4 GB RAM minimum** (8 GB recommandé pour Spark)

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/MissaouiYassine1/flight-delay-ml-pipeline.git
cd flight-delay-ml-pipeline

# 2. Créer et activer un environnement virtuel
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur Mac/Linux
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

### `requirements.txt`

```txt
pyspark
fastapi
uvicorn
streamlit
pydantic
requests
pandas
numpy
```

---

## 🖥 Utilisation

### Étape 1 — Générer le jeu de données *(optionnel)*

```bash
python notebooks/gen_data.py
# ✅ Génère vols_data_massive.csv avec 1 000 000 de lignes
```

### Étape 2 — Entraîner le modèle

```bash
python ml.py
# ✅ Sauvegarde le modèle dans modele_vol_retard/
```

### Étape 3 — Lancer l'API *(Terminal 1)*

```bash
python api.py
# ✅ API disponible sur http://127.0.0.1:8000
# 📚 Documentation Swagger : http://127.0.0.1:8000/docs
```

### Étape 4 — Lancer l'interface *(Terminal 2)*

```bash
streamlit run app.py
# ✅ Interface ouverte sur http://localhost:8501
```

### Étape 5 — Tester avec cURL

```bash
curl -X POST "http://127.0.0.1:8000/predictions" \
     -H "Content-Type: application/json" \
     -d '{"age_pilote": 45, "distance_km": 2500}'
```

**Réponse attendue :**

```json
{
  "statut": "succès",
  "age_pilote": 45,
  "distance_km": 2500,
  "prediction_retard": 1
}
```

---

## 📊 Jeu de Données

Le dataset **`vols_data_massive.csv`** contient **1 000 000 de vols générés synthétiquement**.

| Colonne | Type | Description |
|---------|------|-------------|
| `id_vol` | Integer | Identifiant unique du vol |
| `age_pilote` | Integer | Âge du pilote (22–65 ans) |
| `distance_km` | Integer | Distance du vol (300–5 000 km) |
| `cible_retard` | Integer | `1` = Retard · `0` = Pas de retard |

> **Règle de génération :** La probabilité de retard augmente avec la distance et pour les pilotes très jeunes (< 30 ans) ou très expérimentés (> 55 ans).

---

## 📍 Roadmap

- [x] **Phase 1** — Génération du dataset massif (1M lignes)
- [x] **Phase 2** — Entraînement du modèle PySpark MLlib
- [x] **Phase 3** — Déploiement API FastAPI
- [x] **Phase 4** — Interface Streamlit
- [ ] **Phase 5** — Ajout de features (météo, jour de semaine, compagnie)
- [ ] **Phase 6** — Déploiement Docker + CI/CD GitHub Actions
- [ ] **Phase 7** — Monitoring avec MLflow

---

## 🤝 Contribution

Toute contribution est la bienvenue ! Nous suivons le **GitHub Flow** :

```bash
# 1. Forkez le projet

# 2. Créez votre branche
git checkout -b feature/AmazingFeature

# 3. Committez vos modifications
git commit -m 'feat: add AmazingFeature'

# 4. Pushez sur votre fork
git push origin feature/AmazingFeature

# 5. Ouvrez une Pull Request 🎉
```

### Standards de code

- ✅ Respectez **PEP 8** pour Python
- ✅ Commentez les fonctions complexes
- ✅ Ajoutez des **tests** pour toute nouvelle fonctionnalité

---

## 📄 Licence

Distribué sous la licence **MIT**. Voir [`LICENSE`](LICENSE) pour plus d'informations.

---

## ✉️ Contact

<div align="center">

**Yassine Missaoui**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/missaoui-yassine-m1y/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MissaouiYassine1)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yassine.missaoui@enis.tn)

🔗 **Lien du projet :** [github.com/MissaouiYassine1/flight-delay-ml-pipeline](https://github.com/MissaouiYassine1/flight-delay-ml-pipeline)

</div>

---

<div align="center">

*Made with ❤️ and ☕ — Star ⭐ the repo if you found it useful!*

</div>
