Utilisation de Python
=====================

Pour illustrer les notions de cours, nous allons utiliser un outil de calculs numériques gratuit et polyvalent: Python.
Python possède un grand nombre de librairies et de modules pour nous simplifier la vie. 

Installation
------------

Au lieu d'utiliser une simple distribution Python, je recommande d'utiliser la distribution `miniconda`. 
Cette distribution permet de maintenir facilement différents environnements Python sur votre système.

* Télécharger Miniconda: https://docs.conda.io/en/latest/miniconda.html et Installer-le
* Lancer Miniconda

De base, `miniconda` est installé avec uniquement quelques librairies non-standards Python (pip, zlib, ...). Il est possible de connaître à tout moment la liste 
des paquets Python installés dans l'environnement Python actif en lançant la commande 

.. code ::

    pip list

Préparation de l'environnement
------------------------------

* Lancer Miniconda
* Installer les librairies de calculs numériques en lançant la commande

.. code ::

    conda install numpy scipy matplotlib jupyter

L'installation peut prendre un certain temps. A la fin de l'installation, il est possible de vérifier que les librairies ont 
bien été installées en lançant la commande :code:`pip list`.

Premier Pas avec Jupyter
------------------------

Jupyter est une application web tournant en local sur votre machine. Jupyter est très utilisé car il permet de 
rédiger des rapports (notebook) contenant du texte (en markdown), des équations (en Latex), du code (en Python mais pas que), et des courbes.

* Lancer Miniconda
* Démarrer Jupyter Notebook en lançant la commande

.. code ::

    jupyter notebook

* Créer une première cellule de code avec le code suivant :

.. code ::

    import numpy as np 
    import matplotlib.pyplot as plt 
    from scipy.signal import lti, step

    # create a first order system 
    H = lti([1],[10**-3, 1])

    # plot the step response
    t, s = step(H)
    plt.plot(t, s)
    plt.grid()
    plt.xlabel("t [s]");