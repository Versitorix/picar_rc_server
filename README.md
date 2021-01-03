# RC Server

Ce dépôt contient deux serveurs servant à contrôler le véhicule PiCar de SunFounder à l'aide de commandes envoyés en UDP.

## Pré-requis

 - Python 3
 - Flask
 - [SunFounder_PiCar-V](https://github.com/sunfounder/SunFounder_PiCar-V)

## Installation

1. Copiez (ou dépôt) ce repo sur le raspberry pi
2. Dans le dossier `settings`, copiez le fichier `dev.sample.json` et nommez la copie `dev.json`
3. Dans le fichier `dev.json`, modifiez `"<SERVER IP>"` pour l'adress ip du raspberry py

## Utilisation

Vous devrez avoir deux terminaux d'ouvert pour accèder à toutes les fonctionnalités du vehicule.

### Serveur web

Le serveur web sert a visionner la caméra du Pi-Car.

Windows:
```powershell
python .\webmain.py
```

Linux:
```powershell
python3 ./webmain.py
```

### Serveur de commandes

Le serveur de commandes est un serveur UDP servant à recevoir les directions de contrôles du véhicule.

Windows:
```powershell
python .\main.py
```

Linux:
```shell
python3 ./main.py
```

## Crédits
 Sunfounders pour les contrôles de la caméra et du feed video de la caméra: [Sunfounder Smart Video Car Kit for Raspberry Pi](https://github.com/sunfounder/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi)
