# Projet Dash - Git

Ce dépôt contient une application web interactive construite avec **Dash** et **Dash Bootstrap Components**.

## 🚀 Installation & Lancement

> ⚠️ **Important** : Le dossier d'environnement virtuel (`.venv`) ne doit pas être partagé ou copié d'un ordinateur à un autre car il contient des chemins absolus spécifiques à chaque machine. Chaque développeur doit créer son propre environnement virtuel sur sa machine.

---

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

---

### Méthode 2 : Avec `uv` (Recommandé)

Si `uv` est installé sur votre machine :

```bash
uv sync
uv run python app.py
```
