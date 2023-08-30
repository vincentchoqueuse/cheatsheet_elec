LTSpice
=======

Introduction
------------

LTspice est un logiciel de simulation de circuits électroniques de haute performance développé par Linear Technology, désormais une division d'Analog Devices. Il s'agit d'un simulateur SPICE standard avec une interface graphique améliorée et sans les limitations courantes des simulateurs SPICE traditionnels. Voici quelques points saillants concernant LTspice:

* **Gratuité:** LTspice est offert gratuitement aux concepteurs et aux étudiants. Il ne possède pas de limitations sur le nombre de nœuds, de composants ou de n'importe quel autre paramètre caractéristique des versions d'évaluation d'autres outils.
* **Interface Utilisateur Intuitive:** L'interface de LTspice est conçue pour être intuitive. Les utilisateurs peuvent dessiner des schémas, exécuter des simulations, et visualiser les résultats avec facilité.
* **Librairies Complètes:** LTspice est fourni avec des librairies comprenant des milliers de composants. Toutefois, sa principale force réside dans les modèles de composants de Linear Technology.
* **Types de Simulation:** Outre les analyses DC, AC et transitoires standard, LTspice supporte également la simulation thermique, la simulation de bruit, et d'autres types plus avancés.
* **Personnalisation:** Les utilisateurs peuvent ajouter leurs propres modèles SPICE, ce qui rend LTspice extrêmement flexible.
* **Compatibilité:** Étant un outil basé sur SPICE, LTspice peut souvent exécuter des fichiers de netlist d'autres simulateurs SPICE, et ses fichiers peuvent également être importés dans d'autres outils SPICE.


Exemple 
+++++++

Un fichier LTspice peut s'ouvrir avec un éditeur de texte. Le code ci-dessous correspond au contenu du fichier LTSpice :code:`.asc` pour un filtre Rauch de type LP.

.. code ::

    Version 4
    SHEET 1 1876 900
    WIRE -224 -128 -432 -128
    WIRE -816 -112 -1008 -112
    WIRE -560 -112 -816 -112
    WIRE -816 -96 -816 -112
    WIRE -1120 16 -1168 16
    WIRE -1008 16 -1008 -32
    WIRE -1008 16 -1040 16
    WIRE -960 16 -1008 16
    WIRE -816 16 -816 -32
    WIRE -816 16 -880 16
    WIRE -752 16 -816 16
    WIRE -608 32 -688 32
    WIRE -560 32 -560 -112
    WIRE -560 32 -608 32
    WIRE -752 48 -816 48
    WIRE -1168 64 -1168 16
    WIRE -368 64 -368 32
    WIRE -1008 80 -1008 16
    WIRE -816 80 -816 48
    WIRE -368 96 -368 64
    WIRE -1168 176 -1168 144
    WIRE -1008 176 -1008 144
    WIRE -432 272 -432 -128
    WIRE -224 272 -224 -128
    WIRE -224 272 -432 272
    FLAG -368 64 0
    FLAG -368 -48 +Vcc
    IOPIN -368 -48 Out
    FLAG -368 176 -Vcc
    IOPIN -368 176 Out
    FLAG -720 0 +Vcc
    IOPIN -720 0 In
    FLAG -720 64 -Vcc
    IOPIN -720 64 In
    FLAG -608 32 vs
    FLAG -1168 16 ve
    IOPIN -1168 16 In
    FLAG -816 80 0
    FLAG -1008 176 0
    FLAG -1168 176 0
    SYMBOL voltage -368 -64 R0
    SYMATTR InstName V1
    SYMATTR Value 15
    SYMBOL voltage -368 80 R0
    SYMATTR InstName V2
    SYMATTR Value 15
    SYMBOL UniversalOpamp2 -720 32 R0
    SYMATTR InstName U1
    SYMBOL res -1136 32 R270
    WINDOW 0 32 56 VTop 2
    WINDOW 3 0 56 VBottom 2
    SYMATTR InstName R1
    SYMATTR Value 1000
    SYMBOL res -976 32 R270
    WINDOW 0 32 56 VTop 2
    WINDOW 3 0 56 VBottom 2
    SYMATTR InstName R3
    SYMATTR Value 1000
    SYMBOL res -1024 -128 R0
    SYMATTR InstName R2
    SYMATTR Value 5000
    SYMBOL cap -832 -96 R0
    SYMATTR InstName C2
    SYMATTR Value 23n
    SYMBOL cap -1024 80 R0
    SYMATTR InstName C1
    SYMATTR Value 3.5µ
    SYMBOL voltage -1168 48 R0
    WINDOW 123 24 124 Left 2
    WINDOW 39 0 0 Left 2
    SYMATTR Value2 AC 1 0
    SYMATTR InstName V3
    SYMATTR Value ""
    TEXT -400 250 Left 1 ;alimentation AOP
    TEXT -1200 300 Left 2 !.ac dec 100 10 10k

Gestion des fichiers Audio 
--------------------------

Dans LTspice, il est possible d'importer un fichier son pour l'utiliser comme une source de signal dans une simulation. Ceci est utile si vous souhaitez, par exemple, simuler le comportement d'un circuit à un signal sonore réel. 


Import de fichiers
++++++++++++++++++

* Placez une source de tension sur votre schéma.
* Faites un clic droit sur la source de tension pour éditer ses propriétés.
* Dans le champ "Value", tapez :code:`wavefile="{{filename}}.wav"` (remplacez :code:`{{filename}}"` par le chemin complet du fichier .wav sur votre ordinateur).
* Lancer la simulation

Export 
++++++

Tapez la directive suivante : 

.. code ::
    
    .wave nom_du_fichier.wav nBits nSamples V({{noeud}})

* :code:`nom_du_fichier.wav` est le nom du fichier où vous souhaitez sauvegarder la sortie.
* :code:`nBits` est le nombre de bits par échantillon (par exemple, 16 pour une résolution de 16 bits).
* :code:`nSamples` est la fréquence d'échantillonnage (par exemple, 44100 pour 44,1 kHz).
* :code:`V({{noeud}})` est la tension que vous souhaitez exporter, où :code:`{{noeud}}` est le nom du nœud ou point de votre schéma dont vous souhaitez exporter la tension.

Par exemple, si vous souhaitez exporter la tension au point nommé Out avec une résolution de 16 bits et une fréquence d'échantillonnage de 44,1 kHz, la directive serait : :code:`..wave sortie.wav 16 44100 V(Out)`


Création Automatique de fichier LTspice
---------------------------------------

Pour créer automatiquement des fichiers LTspice, une solution consiste à utiliser le moteur de template Python Jinja.
L'utilisation de Jinja en Python pour générer des fichiers LTspice présente plusieurs avantages, en particulier dans le cadre de simulations automatisées, d'optimisations ou d'analyses de paramètres. Voici quelques raisons pour lesquelles cette approche pourrait être bénéfique:

* **Automatisation des simulations**: En générant des fichiers LTspice avec Jinja, vous pouvez créer automatiquement plusieurs variantes de schémas basés sur différents paramètres. C'est utile pour exécuter des séries de simulations avec différentes conditions ou valeurs de composants.
* **Optimisation**: Si vous souhaitez optimiser certaines performances d'un circuit (comme le gain, la bande passante, etc.), vous pouvez générer des schémas avec différentes configurations, exécuter des simulations pour chacune d'elles et analyser les résultats pour trouver la meilleure configuration.
* **Reproductibilité**: La génération programmée de fichiers LTspice garantit que les schémas sont toujours créés de la même manière, réduisant les erreurs humaines.
* **Modularité**: Avec Jinja, vous pouvez créer des modèles réutilisables pour des parties courantes de circuits, vous permettant de construire rapidement des schémas complexes à partir de blocs préexistants.
* **Gestion de grands projets**: Pour les projets complexes qui nécessitent de nombreux scénarios de simulation ou des variations de conception, la gestion manuelle des fichiers LTspice peut devenir fastidieuse. En utilisant Jinja, vous pouvez structurer et organiser votre flux de travail de manière plus systématique.

Installation de Jinja 
+++++++++++++++++++++

.. code ::

    pip install jinja2


Structure du Projet
+++++++++++++++++++

Dans l'exemple ci dessous, nous allons considérer la création d'un fichier LTspice permettant de simuler un circuit RC-RC.

.. code :: bash

    /output
    /templates
        RCRC.asc //<- template contenant le code asc
    generate_filter.py

Fichier LTSpice 
+++++++++++++++

Le contenu du template LTSpice RCRC.asc est le suivant :

.. code ::

    Version 4
    SHEET 1 1876 900
    WIRE -816 32 -832 32
    WIRE -768 32 -816 32
    WIRE -656 32 -688 32
    WIRE -560 32 -656 32
    WIRE -448 32 -480 32
    WIRE -400 32 -448 32
    WIRE -656 96 -656 32
    WIRE -448 96 -448 32
    WIRE -832 192 -832 112
    WIRE -656 192 -656 160
    WIRE -448 192 -448 160
    WIRE 992 320 992 -304
    FLAG -816 32 ve
    IOPIN -816 32 In
    FLAG -656 192 0
    FLAG -400 32 vs
    IOPIN -400 32 Out
    FLAG -448 192 0
    FLAG -832 192 0
    SYMBOL res -784 48 R270
    WINDOW 0 32 56 VTop 2
    WINDOW 3 0 56 VBottom 2
    SYMATTR InstName R1
    SYMATTR Value {{R1}}
    SYMBOL cap -672 96 R0
    SYMATTR InstName C1
    SYMATTR Value {{C1}}
    SYMBOL res -576 48 R270
    WINDOW 0 32 56 VTop 2
    WINDOW 3 0 56 VBottom 2
    SYMATTR InstName R2
    SYMATTR Value {{R2}}
    SYMBOL cap -464 96 R0
    SYMATTR InstName C2
    SYMATTR Value {{C2}}
    SYMBOL voltage -832 16 R0
    WINDOW 123 24 124 Left 2
    WINDOW 39 0 0 Left 2
    SYMATTR Value2 AC 1 0
    SYMATTR InstName V1
    SYMATTR Value ""

Ce fichier de template contient les tags jinja :code:`{{R1}}`, :code:`{{R2}}`, :code:`{{C1}}`, :code:`{{C2}}`. Le code jinja va permettre 
de remplacer ces tags par une valeur via python.


Code Python 
+++++++++++


Le contenu du fichier python :code:`generate_filter.py` est le suivant.

.. code ::
    
    from jinja2 import Environment, FileSystemLoader


    # chargement du template Jinja
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('RCRC.asc')

    # Valeurs pour les composants à insérer dans le template
    values = {
        "R1": "10k",
        "C1": "10n",
        "R2": "100k",
        "C2": "1n"
    }
    template.stream(values).dump("output/RCRC_output.asc")

       


