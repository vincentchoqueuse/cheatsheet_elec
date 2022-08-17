Rappels sur les Equations Differentielles
=========================================

Modèle Mathématique 
-------------------

Une équation différentielle linéaire à coefficients constants d'ordre n s'exprime sous la forme 

.. math ::

    a_n \frac{d^n s(t)}{dt^n} + \cdots+a_1 \frac{d s(t)}{dt}  +a_0 s(t) =b_m \frac{d^m e(t)}{dt^m} +\cdots+b_0 e(t)

* :math:`a_n` et :math:`b_m` désigne les paramètres de l'équation différentielle,
* La partie droite de l'équation est appelée second membre.


Expression de la Solution
-------------------------

La solution complète de l'équation différentielle s'exprime sous la forme :

.. math ::

    s(t)=s_l(t)+s_p(t)

* :math:`s_l(t)`: solution libre (régime libre),
* :math:`s_p(t)`: solution particulière (régime forcé).

Solution libre
++++++++++++++

Le terme :math:`s_l(t)` désigne la solution libre de l'équation sans second membre définie par :

.. math ::

    a_n \frac{d^n s(t)}{dt^n} + \cdots+a_1 \frac{d s(t)}{dt}  +a_0 s(t) =0

La solution libre s'exprime sous la forme

.. math ::

    s_l(t)=\sum_{k=1}^{n}\lambda_k e^{p_kt}

* :math:`\lambda_k\in \mathbb{C}` désigne des constantes d'intégration. Ces constantes peuvent être déterminées à partir de la connaissance des conditions initiales de l'équation différentielle.
* :math:`p_k \in \mathbb{C}` désigne les racines du polynôme caractéristique :math:`a_n p^n+a_{n-1}p^{n-1}+\cdots+a_1 p+a_0`.


Solution particulière
+++++++++++++++++++++

Le terme :math:`s_p(t)` désigne une solution particulière de l'équation avec second membre. Il n'y a pas d'expression générale 
permettant de déterminer :math:`s_p(t)` quelque soit :math:`e(t)`. Le plus souvent, la solution particulière possède la même "forme"
que :math:`e(t)`.

Par exemple,

* Si :math:`e(t)=\alpha` est une constante, :math:`s_p(t)=\beta` est une constante,
* Si :math:`e(t)` est un polynôme de degré :math:`Q`, :math:`s_p(t)` est un polynôme de degré :math:`Q` (avec des coefficients différents),
* Si :math:`e(t)` est une sinusoïde de pulsation :math:`\omega`, :math:`s_p(t)` est une sinusoïde de pulsation :math:`\omega` (avec une amplitude et une phase différentes).

Les paramètres de la solution particulière s'obtiennent par identification en remplaçant :math:`s(t)` par :math:`s_p(t)` dans l'équation différentielle.

Exemple
-------

Considérons l'équation différentielle suivante de premier ordre

.. math ::

    \tau \frac{d s(t)}{dt} + s(t)= Ku(t)

où :math:`u(t)` désigne l'échelon unité (:math:`u(t)=0` si :math:`t<0` et :math:`u(t)=1` si :math:`t\ge 0`) et :math:`s(0)=0`. 

La solution complète s'exprime sous la forme :

.. math ::

    s(t)=s_l(t)+s_p(t)

* Solution libre: :math:`s_l(t)=\lambda_1 e^{p_1t}` avec :math:`\tau p_1+1=0 \Rightarrow p_1=-\frac{1}{\tau}`.
* Solution particulière: :math:`s_p(t)=\beta` avec :math:`\tau \times 0 +\beta = K\times 1 \Rightarrow \beta=K`.

La solution complète s'exprime alors sous la forme :

.. math ::

    s(t)=\lambda_1 e^{-\frac{1}{\tau} t} + K

Pour déterminer la constante d'intégration :math:`\lambda_1`, il est nécessaire d'exploiter une condition initiale. En utilisant le fait 
que :math:`s(0)=0`, nous obtenons :math:`\lambda_1  + K = 0 \Rightarrow \lambda_1=-K`. Pour :math:`t\ge 0`, nous obtenons finalement l'expression :

.. math ::

    s(t) = K(1-e^{-\frac{1}{\tau}t})