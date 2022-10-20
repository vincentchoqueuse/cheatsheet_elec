Rappels d'Electronique
======================

Dipôles de Base
---------------

Resistance 
++++++++++

.. figure:: img/resistor.svg
  :width: 180
  :align: center

* Modèle : :math:`u(t)=Ri(t)`
* Impedance généralisée : :math:`Z_R=R`


Condensateur 
++++++++++++

.. figure:: img/capacitor.svg
  :width: 180
  :align: center

* Modèle :  :math:`i(t)=C\frac{du(t)}{dt}`
* Impedance généralisée : :math:`Z_C=\frac{1}{Cp}`

Bobine 
++++++

.. figure:: img/inductor.svg
  :width: 180
  :align: center

* Modèle :  :math:`u(t)=L\frac{di(t)}{dt}`
* Impedance généralisée: :math:`Z_L=Lp`

Associations de dipôles
-----------------------

Mise en série 
+++++++++++++

.. figure:: img/serie.svg
  :width: 200
  :align: center

* Impedance généralisée équivalente :

.. math ::

    Z_{eq}=Z_1+Z_2

Mise en parallèle 
+++++++++++++++++

.. figure:: img/parallel.svg
  :width: 200
  :align: center

* Impedance généralisée équivalente : 

.. math ::

    \frac{1}{Z_{eq}}=\frac{1}{Z_1}+\frac{1}{Z_2}

Pont diviseur
+++++++++++++

.. figure:: img/voltage_divider.svg
  :width: 200
  :align: center

* Mise en équation : 

.. math ::

    \frac{V_2(p)}{V_1(p)}=\frac{Z_2}{Z_1+Z_2}

Potentiel des noeuds 
++++++++++++++++++++

.. figure:: img/node.svg
  :width: 300
  :align: center

* Mise en équation : 

.. math ::

    \frac{V_1(p)-V_A(p)}{Z_1}+\frac{V_2(p)-V_A(p)}{Z_2}+\frac{V_3(p)-V_A(p)}{Z_3}=0


Exemple 
-------

On considère le circuit suivant :


.. figure:: img/MFB_BP2.svg
  :width: 300
  :align: center
  :alt: MFB BP2


Mise en équation 
++++++++++++++++

Soit V la tension aux bornes de :math:`R_2`. Cette tension représente le potentiel du noeud d'entrée du circuit.

* Equation 1 (loi des noeuds) 

.. math ::

    \frac{V_e(p) - V(p)}{R_1} + \frac{0-V(p)}{R_2}+\frac{V_s(p) - V(p)}{Z_{C2}}+\frac{V^-(p) - V(p)}{Z_{C1 }} =0


* Equation 2 (loi des noeuds)

.. math ::

    \frac{V(p) - V_-(p)}{Z_{C1}} + \frac{V_s(p)-V_-(p)}{R_3} =0

* Equation 3 (AOP regime linéaire)

.. math ::

    V_+(p) = V_-(p)

* Equation 4 (entrée +):

.. math ::

    V_+(p) = 0

Fonction de transfert 
+++++++++++++++++++++

Pour obtenir la fonction de transfert, nous allons déterminer une équation avec que des termes en :math:`V_e(p)` d'un côté et 
que des termes en :math:`V_s(p)` de l'autre côté.

En manipulant les 4 équations, nous obtenons : 

.. math ::

    \frac{V_e(p)}{R_1}  = -\frac{V_s(p)}{Z_{C2}} +\frac{V(p)}{Z_{C2}}+ \frac{V(p)}{R_2}+ \frac{V(p)}{Z_{C1 }} + \frac{V(p)}{R_1}
   
.. math ::

    V(p)  = -\frac{Z_{C1}}{R_3}V_s(p)

Il en vient que

.. math ::

    \frac{V_e(p)}{R_1}  = -V_s(p)\left(\frac{1}{Z_{C2}} -\frac{Z_{C1}}{Z_{C2}R_3} -\frac{Z_{C1}}{R_2R_3}-\frac{1}{R_3} -\frac{Z_{C1}}{R_1R_3}\right)
   
En remplaçant les impédances par leur expressions et en mettant tout sous le même denominateur pour le terme de droite, nous obtenons

.. math ::

    \frac{V_e(p)}{R_1}  = -\frac{V_s(p)}{R_1R_2R_3C_1p} \left( R_1R_2R_3C_1C_2p^2  + R_1R_2C_2p + R_1 + R_1R_2C_1p + R_2\right)
   

Finalement,

.. math ::

    H(p) = \frac{V_s(p)}{V_e(p)} = -\frac{\frac{R_2R_3}{R_1 + R_2}C_1p}{ \frac{R_1R_2R_3}{R_1 + R_2}C_1C_2p^2  + \frac{R_1R_2}{R_1 + R_2}(C_1+C_2)p + 1}
   
