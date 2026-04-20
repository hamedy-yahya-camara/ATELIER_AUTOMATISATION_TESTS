# 🧪 Atelier "Testing as Code & API Monitoring"

## 👤 Étudiant
**Hamedy Yahya Camara**

## 🌐 URL du site
👉 https://camara.pythonanywhere.com

## 🎯 Objectif
Tester automatiquement une API publique, mesurer sa qualité de service et exposer un dashboard de métriques.

## 🔌 API choisie : Agify
- **URL de base** : https://api.agify.io
- **Authentification** : Aucune
- **Description** : Prédit l'âge d'une personne à partir de son prénom

## 🚀 Routes disponibles

| Route | Description |
|-------|-------------|
| `/` | Page de consignes |
| `/run-tests` | Lance les tests sur l'API Agify |
| `/dashboard` | Dashboard des résultats |
| `/metrics` | Métriques JSON (taux de succès, temps de réponse) |

## 📊 Résultats des tests
- **Total tests** : 5
- **Succès** : 5
- **Échecs** : 0
- **Taux de succès** : 100%
- **Temps moyen de réponse** : 51.24ms

## 🛠️ Stack technique
- Python + Flask
- SQLite (historique des tests)
- PythonAnywhere (hébergement)
- GitHub Actions (déploiement automatique)

## ⚙️ Déploiement automatique
A chaque commit sur GitHub, le code est automatiquement déployé sur PythonAnywhere via GitHub Actions.

## 📁 Structure du projet
