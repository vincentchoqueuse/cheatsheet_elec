Liste des Filtres
=================

Premier ordre
-------------

Passe-Bas (LP)
++++++++++++++

.. math::

    H(p)=\frac{T_0}{\tau p+1}​

* gain statique: :math:`T_0`, 
* constante de temps (en s): :math:`\tau \ge 0` (en s).

Passe-Haut (HP)
+++++++++++++++

.. math::

    H(p)=\frac{T_m\tau p}{\tau p+1}​

* gain haute-fréquence: :math:`T_m`, 
* constante de temps (en s): :math:`\tau \ge 0`


Second Ordre
------------

Passe-bas (LP)
++++++++++++++

.. math::

    H(p)=\frac{T_0}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain statique: :math:`T_0`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`.

Passe-bande (BP)
++++++++++++++++

.. math::

    H(p)=\frac{\frac{2mT_m}{\omega_0}p}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain maximum: :math:`T_m`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 

Passe-haut (HP)
+++++++++++++++

.. math::

    H(p)=\frac{\frac{T_{\infty}}{\omega_0^2}p^2}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain haute-fréquence: :math:`T_{\infty}`,
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 

Rejecteur (Notch)
+++++++++++++++++

.. math::

    H(p)=\frac{T_0\left(\frac{1}{\omega_0^2}p^2+1\right)}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain maximum: :math:`T_0`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 