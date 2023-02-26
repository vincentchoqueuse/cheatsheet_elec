Fonction de Transfert
=====================

Considérons un système linéaire et invariant dans le temps (SLIT) décrit par une équation différentielle linéaire à coefficients constants d'ordre n :

.. math ::

    a_n \frac{d^n s(t)}{dt^n} + \cdots+a_1 \frac{d s(t)}{dt}  +a_0 s(t) =b_m \frac{d^m e(t)}{dt^m} +\cdots+b_0 e(t)

Le plus souvent l'analyse d'un SLIT sera réalisée à partir de la fonction de transfert du système. Au lieu 
de manipuler des dérivées, l'utilisation de la fonction de transfert permet de revenir à la manipulation de polynômes.

Dans ce cours, nous allons nous focaliser spécifiquement à différent type d'entrées :math:`e(t)`:

* Impulsion: Lorsque :math:`e(t)=\delta(t)`, la sortie du système est appelée **réponse impulsionnelle**,
* Echelon d'amplitude E: Lorsque :math:`e(t)=Eu(t)`, la sortie du système est appelée **réponse indicielle**,
* Sinusoïde: Lorsque :math:`E\cos(\omega t + \varphi_e)`, la sortie du système est appelée **réponse fréquentielle**.

Définition
----------

La fonction de transfert du système est définie par :

.. math ::

    H(p) = \frac{S(p)}{E(p)}

* :math:`p \in \mathbb{C}` désigne la variable de Laplace,
* :math:`E(p)=\mathcal{L}[e(t)]` désigne la transformée de Laplace de l'entrée,
* :math:`S(p)=\mathcal{L}[s(t)]` désigne la transformée de Laplace de la sortie.


L'expression de :math:`H(p)` peut s'obtenir

* à partir de l'équation différentielle en appliquant la transformée de Laplace,
* à partir de l'analyse d'un circuit électronique en utilisant directement la notion d'impédance généralisée.

Forme Polynomiale [ba]
++++++++++++++++++++++

.. math ::

    H(p) = \frac{N(p)}{D(p)}=\frac{b_m p^m+\cdots+b_1p+b_0}{a_n p^n+\cdots+a_1 p+a_0}

Forme Factorisée [zpk]
++++++++++++++++++++++

.. math ::

    H(p) = G\frac{(p-z_m)\times \cdots\times (p-z_1)}{(p-p_n)\times \cdots\times (p-p_1)}

* le paramètre :math:`G=\frac{b_m}{a_n}` est un coefficient d'amplification,
* les **zéros** :math:`z_l` correspondent aux racines du numérateur c-a-d aux solutions de l'équation 

.. math ::
    b_m p^m+\cdots+b_1p+b_0,

* les **pôles** :math:`p_l` correspondent aux racines du dénominateur (c-à-d du polynôme caractéristique) c-a-d aux solutions de l'équation 

.. math ::
    a_n p^n+\cdots+a_1p+a_0 = 0.

Il est courant de représenter la localisation des pôles (:math:`\times`) et des zéros (:math:`\circ`) dans le plan complexes.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    m = 0.6
    w0 = 1
    poles = np.array([-3, -1.1, -0.5+0.9j, -0.5-0.9j, -0.1])
    zeros = np.array([1, 1.2j, -1.2j, -2])


    fig = plt.figure(figsize=[7,4.8])
    plt.plot(np.real(poles),np.imag(poles),'x', label="poles")
    plt.plot(np.real(zeros),np.imag(zeros),'o', label="zeros")
    plt.xlabel("$\Re e(.)$")
    plt.ylabel("$\Im m(.)$")
    plt.legend()
    plt.grid()

Les pôles jouent un rôle de premier plan au niveau de la réponse temporelle (stabilité, présence d'oscillation, rapidité).

Propriétés 
----------

Stabilité (BIBO)
++++++++++++++++

Un système est dit stable (au sens BIBO: Bounded Input Bounded Output) si pour toute entrée bornée :math:`|e(t)|<\infty`, la sortie est également bornée c-à-d :math:`|s(t)|<\infty`.

Pour qu'un système soit stable, il est possible d'établir que tous les pôles du systèmes doivent posséder une partie réelle négative c-à-d 

.. math ::

    \Re e(p_l)\le 0, \text{ pour }l=1,.., n. 


Gain statique 
+++++++++++++

Le gain statique, noté :math:`K`, est le rapport entre la sortie et l'entrée en régime permanent lorsque l'entrée est un échelon d'amplitude :math:`E`. Mathématiquement, le gain statique s'exprime sous la forme :

.. math ::

    K = \frac{s(\infty)}{E} = H(0) = \frac{b_0}{a_0}

* Lorsque l'entrée est une sinusoïde, le gain statique correspond au gain basse-fréquence c-a-d lorsque :math:`\omega \to 0`. 
* Si l'entrée et/ou la sortie ne sont pas nulles, le gain statique correspond au rapport entre la variation de la sortie et la variation de l'entrée.

Comportement Fréquentiel
++++++++++++++++++++++++

Exponentielle Complexe 
``````````````````````

Lorsque l'entrée est une exponentielle complexe de pulsation :math:`\omega`, c-à-d :math:`e(t)=ce^{j\omega t}`, la sortie est une sinusoïde de même pulsation et s'exprime sous la forme :

.. math::
    
    s(t)=H(j\omega)ce^{j\omega t}.

Sinusoïde
`````````

Lorsque l'entrée est une sinusoïde de pulsation :math:`\omega`, c-à-d :math:`e(t)=E\cos(\omega t + \varphi_e)`, la sortie est une sinusoïde de même pulsation et s'exprime sous la forme :

.. math::
    
    s(t)=|H(j\omega)|E\cos(\omega t + \varphi_e + \arg[H(j\omega)]),

* :math:`|H(j\omega)|` correspond au gain du système à la pulsation :math:`\omega`,
* :math:`\arg[H(j\omega)]` correspond au déphasage du système à la pulsation :math:`\omega`.

L'allure du gain :math:`|H(j\omega)|` permet de caractériser le type de filtre (passe-bas, passe-bande, passe-haut, rejecteur, ...)

