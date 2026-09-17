# 📊 Projet Dash Multi-Pages

Ce dépôt contient une application web interactive construite avec **Python**, **Dash**, **Plotly Express** et **Dash Bootstrap Components**.

---

## 🌟 Présentation de l'Application

L'application est structurée en plusieurs modules d'analyse de données accessibles via la barre de navigation latérale :

* **🏠 Accueil (`/`)** : Vue d'ensemble du projet, présentation des technologies utilisées et résumé des différentes pages d'analyse.
* **📈 Page 1 - Louis (`/page-1`)** : Analyse de l'évolution boursière des géants de la Tech (GAFAM & Netflix) basée sur le jeu de données `stocks`. Permet la sélection dynamique multi-entreprises et le basculement entre graphique temporel (lignes) et niveau récent (histogramme).
* **📊 Page Bernice (`/bernice`)** : Exploration du jeu de données `Gapminder` (Espérance de vie vs PIB par habitant) avec des contrôles interactifs organisés sous forme d'**Accordéon Bootstrap**.
* **📑 Page Ilona (`/ilona`)** : Exploration du jeu de données `Gapminder` avec les contrôles organisés sous forme d'**Onglets Bootstrap (Tabs)**.

---

## 📁 Structure du Projet

```text
Projet-git/
│
├── app.py                  # Point d'entrée principal de l'application Dash (layout & sidebar)
├── requirements.txt        # Dépendances Python (Dash, Plotly, Pandas, DBC, Gunicorn)
├── pyproject.toml / uv.lock# Fichiers de gestion de projet (uv)
├── render.yaml             # Configuration de déploiement Render
├── README.md               # Documentation du projet
│
├── assets/                 # Fichiers statiques
│   ├── style.css           # Styles CSS pour le layout fixe et la barre latérale
│   └── img/                # Images et logos
│       └── logo.png
│
└── pages/                  # Pages de l'application (routing dynamique Dash)
    ├── home.py             # Page d'accueil ( path='/' )
    ├── louis_bouquerel.py  # Page 1 ( path='/page-1' )
    ├── bernice.py          # Page Bernice ( path='/bernice' )
    └── ilona.py            # Page Ilona ( path='/ilona' )
```

---

## 🚀 Installation & Lancement

> ⚠️ **Important** : Le dossier d'environnement virtuel (`.venv`) ne doit pas être partagé ou copié d'un ordinateur à un autre car il contient des chemins absolus spécifiques à chaque machine. Chaque développeur doit créer son propre environnement virtuel sur sa machine.

### Méthode 1 : Avec `pip` (Python standard)

1. **Supprimer l'ancien dossier `.venv`** s'il a été copié depuis une autre machine.
2. **Créer un nouvel environnement virtuel** dans le dossier du projet :
   * **Windows** :
     ```powershell
     python -m venv .venv
     ```
   * **Mac / Linux** :
     ```bash
     python3 -m venv .venv
     ```
3. **Activer l'environnement virtuel** :
   * **Windows (PowerShell)** :
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
     *(Si PowerShell affiche une erreur de sécurité, tapez d'abord : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)*
   * **Windows (CMD)** :
     ```cmd
     .\.venv\Scripts\activate.bat
     ```
   * **Mac / Linux** :
     ```bash
     source .venv/bin/activate
     ```
4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
5. **Lancer l'application** :
   ```bash
   python app.py
   ```
   L'application sera accessible sur `http://127.0.0.1:8050/`.

---

### Méthode 2 : Avec `uv` (Recommandé)

Si `uv` est installé sur votre machine :

```bash
uv sync
uv run python app.py
```

---

## ☁️ Déploiement

Le projet contient un fichier `render.yaml` configuré pour un déploiement automatique sur **Render** via **Gunicorn** :
```bash
gunicorn app:server
```

