Travail Collaboratif : Analyse des filtres d'ordre 2
====================================================

Acquis d'Apprentissage Visés
----------------------------

* AAv2 (Modélisation et représentations des systèmes LTI ordre 1 et 2) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de déterminer, pour un système LTI décrit dans un formalisme donné, la réponse indicielle et fréquentielle en utilisant la résolution de l’équation différentielle ou la transformée de Laplace, et de représenter ces réponses sous forme adéquates. Les formalismes considérés incluent:
    * la forme factorisée: z,p,k;
    * la forme polynomiale: b,a. 
    
    L’étudiant sera en mesure de vérifier la validité de ses développements avec un logiciel de simulation (Python/Numpy/Scipy).

* AAv3 (Caractérisation et identification) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de caractériser le comportement d’un système LTI représenté par sa réponse indicielle, sa réponse fréquentielle ou son diagramme des pôles et des zéros. La caractérisation portera sur les critères suivants:
    * Caractéristiques temporelles: stabilité, présence de dépassement, temps de réponse à 5 %,
    * Caractéristiques fréquentielles: type, amplification, fréquence propre, amortissement, comportement asymptotique.

Description du travail
----------------------

Chaque groupe de travail travaille sur l'un des 4 filtres suivants: 


.. math::

    H_{LP}(p)&=\frac{T_0}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}\\
    H_{BP}(p)&=\frac{\frac{2mT_m}{\omega_0}p}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​\\
    H_{HP}(p)&=\frac{\frac{T_{\infty}}{\omega_0^2}p^2}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​\\
    H_{BR}(p)&=\frac{T_0\left(\frac{1}{\omega_0^2}p^2+1\right)}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

L'objectif final est l'identification des paramètres :math:`T_x`, :math:`\omega_0` et :math:`m` d'un filtre à partir de :

* la cartographie des pôles et des zéros, 
* l'analyse de la réponse temporelle (indicielle, ...),
* l'analyse de la réponse fréquentielle. 

Méthodologie
------------

Dans l'objectif de proposer une technique d'identification, nous proposons d'utiliser la méthodologie suivante :

Pôles et Zéros 
++++++++++++++

* Détermination de l'expression analytique des pôles et zéros,
* Identification de :math:`\omega_0` et :math:`m` à partir de la position des pôles.

Réponse Temporelle 
++++++++++++++++++

* Détermination de l'expression analytique de la solution libre :math:`s_l(t)`. Dans le cas où cette solution présente des oscillations: 
    * Détermination de la pseudo-pulsation :math:`\omega_p`,
    * Détermination du ratio :math:`R=s_l(t)/s_l(t+T_p)` entre deux dépassements consécutifs de même signe où :math:`T_p` désigne la pseudo-pulsation.

* Détermination de l'expression analytique de la solution particulière :math:`s_l(t)` dans le cas d'une réponse indicielle,
* Détermination des constantes d'intégration. Dans le cas où les conditions initiales sont nulles, 
    * Détermination de la valeur initiale :math:`s(0^+)`
    * Détermination de la dérivée en :math:`0^+` c-à-d :math:`\left.\frac{ds(t)}{dt}\right|_{t=0^+}`

* Détermination de l'expression analytique de la réponse indicielle. 

Réponse Fréquentielle 
+++++++++++++++++++++

* Détermination de l'expression analytique de la réponse fréquentielle (module et argument),
* Détermination du comportement asymptotique en :math:`\omega\to 0` et :math:`\omega\to +\infty`,
* Détermination du comportement singulier en :math:`\omega_0`,
* Détermination des coordonnées de l'extremum du module (pulsation, module, argument),
* [Filtre BP ou BR] Identification de la largeur de la bande-passante (ou bande rejetée) à :math:`-3` dB.