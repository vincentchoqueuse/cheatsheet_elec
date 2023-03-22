Détermination des constantes d'intégration
==========================================

Introduction
------------

Ce tutorial montre comment déterminer les constantes d'intégration pour la réponse temporelle d'un système de second ordre décrit 
par une équation différentielle linéaire à coefficients constants. La méthode décrite ici fait intervenir des notions de calculs matriciels et
peut s'étendre facilement à des systèmes d'ordres supérieurs.


Expression de la solution
-------------------------

Pour un système d'ordre 2, la réponse temporelle du système s'exprime sous la forme générale suivante :

.. math ::

    s(t) = \lambda_1 e^{p_1 t} +\lambda_2 e^{p_2 t} + s_p(t)

Notre objectif ici est la détermination des constantes d'intégration :math:`\lambda_1` et :math:`\lambda_2` sous l'hypothèse où les valeurs de 
:math:`p_1`, :math:`p_2` et :math:`s_p(t)` sont connues et que les conditions initiales en :math:`0^+` sont données.
Pour simplifier nos calculs, nous allons conserver l'expression initiale de :math:`s(t)` qui est composée d'une combinaison linéaire de fonctions exponentielles et d'un terme additionnel.


Utilisation des conditions initiales
------------------------------------

Cas général 
+++++++++++

Pour déterminer les deux constantes d'intégrations, nous avons besoin de deux conditions initiales. Dans notre contexte, nous allons 
exploiter la connaissance de :

.. math ::

    s(0^+) &= \lim_{t\to 0^+} s(t)\\
    \dot{s}(0^+) &= \lim_{t\to 0^+} \frac{ds(t)}{dt}

En utilisant ces informations, nous pouvons poser que :

.. math ::

    s(0^+) &= \lambda_1 +\lambda_2 + s_p(0^+)\\
    \dot{s}(0^+) &= \lambda_1 p_1 +\lambda_2 p_2  + \dot{s}_p(0^+)

Pour résoudre ce système linéaire, une approche efficace consiste à modéliser le problème sous forme matricielle :

.. math ::

    \mathbf{x} = \begin{bmatrix}
    s(0^+)-s_p(0^+)\\
    \dot{s}(0^+)-\dot{s}_p(0^+)
    \end{bmatrix}
    = \begin{bmatrix}1 & 1 \\ p_1 & p_2 \end{bmatrix}
    \begin{bmatrix}
    \lambda_1\\
    \lambda_2
    \end{bmatrix}

où :math:`\textbf{x} \in \mathbb{R}^2` est un vecteur connus. 

Il en vient que :

.. math ::

    \begin{bmatrix}
    \lambda_1\\
    \lambda_2
    \end{bmatrix} = \frac{1}{p_2-p_1}
    \begin{bmatrix}p_2 & -1 \\ -p_1 & 1 \end{bmatrix}\mathbf{x}

Cas où :math:`m<1`
++++++++++++++++++


Notons que lorsque les pôles sont complexes-conjugués, c-à-d :math:`p_1=p_2^*`, nous obtenons :

.. math ::

    \begin{bmatrix}
    \lambda_1\\
    \lambda_2
    \end{bmatrix} = \frac{j}{2\Im m(p_1)}
    \begin{bmatrix}p_1^* & -1 \\ -p_1 & 1 \end{bmatrix}\mathbf{x}
    
En utilisant le fait que :math:`\textbf{x} \in \mathbb{R}^2`, il est alors possible d'établir que :math:`\lambda_2 = \lambda_1^*`