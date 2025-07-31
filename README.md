# WIMS - Who Is My Double

🎭 **Une application web de reconnaissance faciale pour trouver votre sosie parmi les célébrités**

## 📋 Description

WIMS (Who Is My Sosie) est une application web interactive qui utilise l'intelligence artificielle et la reconnaissance faciale pour identifier à quelle célébrité vous ressemblez le plus. L'application analyse les caractéristiques de votre visage et les compare avec une base de données de célébrités pour trouver votre sosie.

*Projet développé dans le cadre du DUT Informatique, utilisant Python avec dlib et OpenCV pour la comparaison des visages.*

## ✨ Fonctionnalités

- 📸 **Upload d'image** : Téléchargez votre photo pour l'analyse
- 🔍 **Reconnaissance faciale avancée** : Utilise dlib et OpenCV pour l'analyse des traits du visage
- 🌟 **Base de données de célébrités** : Compare avec plus de 20 célébrités différentes
- 🎨 **Interface moderne** : 3 thèmes visuels différents
- 📊 **Résultats détaillés** : Affichage du pourcentage de ressemblance
- 🔄 **Temps réel** : Traitement en direct avec WebSocket

## 🏗️ Architecture technique

### Backend
- **Node.js** avec Express.js
- **Python** pour le traitement d'images et la reconnaissance faciale
- **MongoDB** pour le stockage des données
- **Socket.io** pour la communication temps réel

### Frontend
- **HTML/CSS/JavaScript**
- **Pug** comme moteur de templates
- **Interface responsive** avec plusieurs thèmes

### Intelligence Artificielle
- **dlib** pour la détection et reconnaissance faciale
- **OpenCV** pour le traitement d'images
- **Modèles pré-entraînés** :
  - `shape_predictor_68_face_landmarks.dat`
  - `dlib_face_recognition_resnet_model_v1.dat`
  - `mmod_human_face_detector.dat`

## 🚀 Installation

### Prérequis
- Node.js (version 14+)
- Python 3.8+
- MongoDB

### Installation des dépendances Node.js
```bash
npm install
```

### Installation des dépendances Python
```bash
cd public/compare
pip install -r requirements.txt
```

### Configuration de la base de données
1. Configurez votre connexion MongoDB dans `public/compare/main.py`
2. La connexion actuelle pointe vers MongoDB Atlas

## 🎯 Utilisation

### Démarrage de l'application
```bash
npm start
```

L'application sera accessible sur `http://localhost:3000`

### Utilisation de l'interface

1. **Accédez à l'application** dans votre navigateur
2. **Choisissez un thème** (3 thèmes disponibles)
3. **Téléchargez votre photo** en respectant les recommandations :
   - Visage bien visible et centré
   - Pas de cheveux devant les yeux
   - Éclairage correct
4. **Attendez l'analyse** - Le traitement se fait en temps réel
5. **Découvrez votre sosie** avec le pourcentage de ressemblance

## 📁 Structure du projet

```
WIMS/
├── app.js                 # Point d'entrée de l'application
├── package.json           # Dépendances Node.js
├── Procfile              # Configuration Heroku
├── bin/www               # Serveur HTTP
├── routes/               # Routes Express
├── views/                # Templates Pug
├── public/
│   ├── compare/          # Module Python de reconnaissance faciale
│   │   ├── main.py       # Logique principale d'analyse
│   │   ├── *.dat         # Modèles de reconnaissance faciale
│   │   └── package/      # Utilitaires Python
│   ├── images/           # Base de données d'images de célébrités
│   ├── javascripts/      # Scripts côté client
│   └── stylesheets/      # Styles CSS
└── README.md
```

## 🎨 Célébrités incluses

La base de données comprend des images de référence pour :
- Anne Hathaway, Arnold Schwarzenegger, Ben Affleck
- Bourvil, Brian Shaw, Dwayne Johnson
- Eddie Hall, Elton John, Gerard Depardieu
- Hafthor Julius Bjornsson, Jerry Seinfeld
- Kate Beckinsale, Keanu Reeves, Lauren Cohan
- Louis de Funès, Madonna, Mindy Kaling
- Ragnar, Ryan Gosling, Simon Pegg
- Sofia Vergara, Travis Fimmel, Trump, Will Smith

## 🔧 Configuration

### Variables d'environnement
- `MONGODB_URI` : URL de connexion MongoDB
- `PORT` : Port du serveur (défaut: 3000)

### Personnalisation
- **Ajouter des célébrités** : Placez les images dans `public/images/celeb/`
- **Modifier les thèmes** : Éditez les fichiers CSS dans `public/stylesheets/`

## 🚀 Déploiement

L'application est configurée pour un déploiement sur Heroku :
```bash
git push heroku master
```

## 📝 Licence

Ce projet est sous licence privée. Tous droits réservés.
