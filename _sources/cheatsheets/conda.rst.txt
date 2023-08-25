Conda 
=====

Introduction
------------

Conda est un système de gestion de paquets open-source et un système de gestion d'environnements pour installer et gérer des paquets logiciels et leurs dépendances. Il est principalement utilisé dans l'écosystème du langage de programmation Python.

Conda permet aux utilisateurs de créer et de gérer des environnements isolés avec des versions spécifiques de Python et d'autres paquets, offrant ainsi des workflows de développement logiciel plus flexibles et reproductibles. Il intègre également un gestionnaire de paquets puissant qui permet aux utilisateurs d'installer, de mettre à jour et de supprimer facilement des paquets logiciels, y compris des dépendances complexes.

Conda est couramment utilisé en science des données, en informatique scientifique et en apprentissage automatique, où il est souvent employé pour gérer des piles logicielles complexes et leurs dépendances. Il est disponible en tant qu'application autonome, ainsi que dans le cadre de la distribution Anaconda, qui comprend un certain nombre de paquets préinstallés couramment utilisés en science des données et en informatique scientifique.

Différence entre conda et pip 
++++++++++++++++++++++++++++++

Conda et pip sont tous deux des systèmes de gestion de paquets pour Python, mais ils présentent des différences clés en termes de fonctionnalités et de cas d'utilisation.

* Pip est un gestionnaire de paquets simple principalement utilisé pour installer et gérer des paquets Python à partir de l'Index des Paquets Python (PyPI). Il installe les paquets dans l'environnement Python par défaut de l'utilisateur et ne fournit aucune fonctionnalité intégrée pour gérer les dépendances ou créer des environnements isolés.

* Conda est un système de gestion de paquets plus puissant conçu pour gérer des piles logicielles complexes et leurs dépendances. Il permet aux utilisateurs de créer et de gérer des environnements isolés avec des versions spécifiques de Python et d'autres paquets, et comprend un gestionnaire de paquet qui peut installer, mettre à jour et supprimer des paquets, y compris des dépendances complexes. Contrairement à Pip, Conda peut gérer des paquets écrits dans plusieurs langages de programmation, pas seulement en Python.

Prise en Main 
-------------

Installation
++++++++++++

* Miniconda: https://docs.conda.io/en/latest/miniconda.html

Liste des environnements 
++++++++++++++++++++++++

.. code ::
    
    $ conda env list

Cette commande retourne la liste des environnements disponibles. 
.. code ::

    base                  *  /opt/anaconda3
    py_37                    /opt/anaconda3/envs/py3_7

L'environnement actif est indiqué avec le symbole :code:`*`. Il est possible que cet environnement soit le seul disponible après l'installation de miniconda. 


Installation d'un environnement
+++++++++++++++++++++++++++++++

Il est possible de créer un nouvel environnement nommé :code:`py_enib` en python 3.9 en utilisant la commande suivant

.. code ::

    $ conda create --name py_enib python=3.9

Installer un environnement particulier pour chaque matière/projet présente plusieurs avantages: 

* Isolation des dépendances : Chaque projet peut avoir ses propres dépendances, et parfois des versions différentes d'une même bibliothèque. Avoir des environnements séparés évite les conflits entre les versions.
* Reproductibilité : Si vous souhaitez partager votre projet, fournir l'environnement Conda associé (souvent via un fichier environment.yml) permet à d'autres de reproduire exactement le même environnement avec les mêmes versions de bibliothèques. 
* Nettoyage simplifié: Si vous n'avez plus besoin d'un projet, vous pouvez simplement supprimer son environnement Conda associé, ce qui supprime toutes les dépendances installées pour ce projet en particulier, sans affecter les autres projets.
* Compatibilité : Parfois, certains projets peuvent nécessiter une version spécifique de Python ou d'une autre bibliothèque en raison de contraintes de compatibilité. Avoir des environnements distincts permet de gérer cela facilement.

Activation de l'environment
+++++++++++++++++++++++++++

.. code ::

    $ conda activate py_enib

Installation de paquets 
+++++++++++++++++++++++

La commande suivante montre comment installer plusieurs paquets python dans l'environnement :code:`py_enib`

.. code ::

    $ conda install numpy scipy matplotlib jupyter

Ces librairies seront nécessaires pour le cours d'électronique S4. Il est possible de vérifier le bon fonctionnement de l'installation en lancant la commande suivante.

.. code ::

    $ pip list

Desactivation de l'environment
++++++++++++++++++++++++++++++

.. code ::

    $ conda deactivate