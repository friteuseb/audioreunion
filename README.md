# Outil de conversion audio en texte et résumé de réunion

Cet outil permet d'enregistrer une réunion en temps réel, de convertir l'audio en texte, et de générer un résumé de la réunion.

## Installation

1. Assurez-vous d'avoir Python 3.7+ installé sur votre système.
2. Clonez ce dépôt ou téléchargez les fichiers dans un dossier local.
3. Ouvrez un terminal et naviguez vers le dossier du projet.
4. Installez les dépendances en exécutant :
   ```
   pip install -r requirements.txt
   ```

## Utilisation

1. Exécutez le script principal :
   ```
   python main.py
   ```
2. Appuyez sur 's' pour démarrer l'enregistrement.
3. Parlez clairement dans votre microphone.
4. Appuyez sur 'q' pour arrêter l'enregistrement.
5. Le script convertira automatiquement l'audio en texte et générera un résumé.

## Remarques

- L'audio enregistré est sauvegardé dans un fichier 'recorded_audio.wav'.
- La transcription et le résumé sont affichés dans la console.
- Assurez-vous d'avoir une connexion Internet active pour la reconnaissance vocale et la génération de résumé.

## Dépendances principales

- SpeechRecognition : pour la conversion audio en texte
- sounddevice : pour l'enregistrement audio
- keyboard : pour la gestion des commandes clavier
- transformers : pour la génération de résumé
