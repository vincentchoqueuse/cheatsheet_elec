Systèmes de Second Ordre 
========================

Modélisation
------------

Equation différentielle 
+++++++++++++++++++++++

.. math ::

    \frac{1}{\omega_0^2}\frac{d^2 s(t)}{dt^2} +\frac{2m}{\omega_0}\frac{d s(t)}{dt}+s(t) = b_2\frac{d^2 e(t)}{dt^2} +b_1\frac{d e(t)}{dt}+e(t)

* :math:`\omega_0` désigne la pulsation propre [rad/s],
* :math:`m` le coefficient d'amortissement.

Fonction de transfert
+++++++++++++++++++++

La fonction de transfert d'un système de second ordre peut s'exprimer sous la forme normalisée suivante :

.. math ::

    H(p)=\frac{N(p)}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}

* :math:`N(p)` désigne le numérateur de la fonction de transfert (polynôme de degré inférieur ou égale à 2).

Exemples
++++++++

.. math::

    H_{LP}(p)&=\frac{T_0}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}\\
    H_{BP}(p)&=\frac{\frac{2mT_m}{\omega_0}p}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​\\
    H_{HP}(p)&=\frac{\frac{T_{\infty}}{\omega_0^2}p^2}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​\\
    H_{BR}(p)&=\frac{T_0\left(\frac{1}{\omega_0^2}p^2+1\right)}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​



Expressions des Pôles 
---------------------

Les pôles s'obtiennent en déterminant les racines du dénominateur
de la fonction de transfert c-a-d en déterminant les valeurs de :math:`p` telles que : 

.. math::

    \frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1 = 0

Cette équation est une équation du second degré. Le discriminant s'exprime sous la forme suivante:

.. math::

    \Delta = \left(\frac{2m}{\omega_0}\right)^2-\frac{4}{\omega_0^2} =\frac{4}{\omega_0^2}\left(m^2-1\right)

L'expression du discriminant montre que la valeur de m joue un rôle essentiel dans l'expression des 
deux racines. Nous pouvons distinguer 3 cas de figure.

Cas où m>1
++++++++++

Lorsque :math:`m>1`, le système possède deux poles réels et distincts. Les pôles s'expriment sous la forme 

.. math::
    p_1 = -m\omega_0 +\omega_0 \sqrt{m^2-1}\\
    p_2 = -m\omega_0 -\omega_0 \sqrt{m^2-1}

Mathématiquement, nous obtenons les propriétés suivantes:

* le produit des deux pôles est égale à :math:`p_1p_2=m^2\omega_0^2-\omega_0^2(m^2-1)=\omega_0^2`
* la somme des deux pôle est égale à :math:`p_1+p_2=-2m\omega_0`.

Nous en déduisons alors que:

.. math::
    \omega_0 &= \sqrt{p_1p_2}\\
    m &= -\frac{p_1+p_2}{2\omega_0}

Géométriquement, les deux pôles sont placés sur un cercle de centre :math:`-m\omega_0` et de rayon :math:`\omega_0\sqrt{m^2-1}`.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    m = 2
    w0 = 1
    poles = np.sort(np.roots([1/(w0**2),2*m/w0,1]))
    center = -m*w0

    angle = np.arange(0,2*np.pi,0.05)
    radius = w0*np.sqrt(m**2-1)

    fig = plt.figure(figsize=[7,4.8])
    plt.plot(np.real(poles),np.imag(poles),'x')
    plt.plot(center-radius*np.cos(angle),radius*np.sin(angle),'k--', linewidth=1)
    plt.xlabel("$\Re e(.)$")
    plt.ylabel("$\Im m(.)$")
    plt.grid()
    plt.xlim([-5,5])
    plt.xticks([poles[0],-m*w0,poles[1],0],["$p_2$","$-m\omega_0$","$p_1$","0"])
    plt.yticks([-w0*np.sqrt(m**2-1),0,w0*np.sqrt(m**2-1)],["$-\omega_0\sqrt{m^2-1}$","$0$","$\omega_0\sqrt{m^2-1}$"])
    plt.axis("equal")


Cas où m=1
++++++++++

Lorsque :math:`m=1`, le système possède un pole réel double. Le pole réel double s'exprime sous la forme

.. math::
    p_1 = p_2 = -m\omega_0

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    m = 1
    w0 = 1
    poles = np.sort(np.roots([1/(w0**2),2*m/w0,1]))

    fig = plt.figure(figsize=[7,4.8])
    plt.plot(np.real(poles),[0,0],'x')
    plt.xlabel("$\Re e(.)$")
    plt.ylabel("$\Im m(.)$")
    plt.grid()
    plt.xlim([-2.5,0.5])
    plt.xticks([-m*w0,0],["$-m\omega_0$","0"])
    plt.yticks([0],["0"])
    

Cas où m<1
++++++++++

Lorsque :math:`m<1`, le système possède une paire de pôles complex-conjugués. Les pôles s'expriment sous la forme 

.. math::
    p_1 = -m\omega_0 +j\omega_0 \sqrt{1-m^2}\\
    p_2 = -m\omega_0 -j\omega_0 \sqrt{1-m^2}

Mathématiquement, 

* le module de chaque pôle est égal à :math:`|p_1|=|p_2|=\sqrt{(m\omega_0)^2+\omega_0^2(1-m^2)}=\omega_0`.
* l'angle formé entre le pôle :math:`p_1` et l'axe des réels est donné par :math:`\cos(\theta)=-\Re e(p_1)/|p_1|=m`

Nous en déduisons alors que:

.. math::
    \omega_0 &= \sqrt{p_1p_1^*}=|p_1|\\
    m &= -\frac{\Re e(p_1)}{\omega_0 }

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    import matplotlib.pyplot as plt

    m = 0.6
    w0 = 1
    poles = np.sort(np.roots([1/(w0**2),2*m/w0,1]))
    center = -m*w0
    angle = np.arange(0,2*np.pi,0.05)
    radius = w0*np.sqrt(1-m**2)

    fig = plt.figure(figsize=[7,4.8])
    plt.plot(center-radius*np.cos(angle),radius*np.sin(angle),'k--', linewidth=1)
    plt.plot(np.real(poles),np.imag(poles),'x')
    plt.xlabel("$\Re e(.)$")
    plt.ylabel("$\Im m(.)$")
    plt.grid()
    plt.xlim([-3,0.5])
    plt.xticks([-m*w0,0],["$-m\omega_0$","0"])
    plt.yticks([-w0*np.sqrt(1-m**2), 0, w0*np.sqrt(1-m**2)],["$-\omega_0\sqrt{1-m^2}$","$0$","$\omega_0\sqrt{1-m^2}$"])
    plt.axis("equal")


Réponse Temporelle
------------------

La réponse à une entrée quelconque s’exprime sous la forme :

.. math ::
    
    s(t) = s_l(t) + s_p(t)

* :math:`s_l(t)`: solution libre,
* :math:`s_p(t)`: solution particulière.

Cas où m>1
++++++++++

Le régime libre s'exprime sous la forme :

.. math ::
    
    s_l(t)=\lambda_1 e^{-(m-\sqrt{m^2-1})\omega_0t}+\lambda_2 e^{-(m+\sqrt{m^2-1})\omega_0t}

Le régime libre est donné par la contribution de deux systèmes de premier ordre ayant pour constantes de temps :

.. math ::
    
    \tau_{1,2} =-\frac{1}{p_{1,2}}=\frac{1}{\omega_0 (m\pm \sqrt{m^2-1})}


Cas où m<1
++++++++++

Le régime libre s'exprime alors sous la forme :

.. math ::

    s_l(t)=\lambda e^{-m\omega_0t}\cos(\omega_0 \sqrt{1-m^2}t+\varphi)

* :math:`-m\omega_0`` régit la vitesse de décroissance de l'enveloppe,
* :math:`\omega_p=\omega_0 \sqrt{1-m^2}` correspond à la pseudo-pulsation des oscillations [rad/s] 


Propriétés 
``````````

* Oscillations : pseudo-pulsation et pseudo-période.

.. math ::

    \omega_p &=\omega_0\sqrt{1-m^2}\\
    T_p &= \frac{2\pi}{\omega_0\sqrt{1-m^2}}

* Ratio des amplitudes après une oscillation :

.. math ::
    
    R = \frac{s_l(t_1)}{s_l(t_1+T_p)}=e^\frac{2\pi m}{\sqrt{1-m^2}} > 1


Lorsque :math:`m\ll 1`, :math:`\omega_p\approx \omega_0` et :math:`R\approx e^{2\pi m}`.