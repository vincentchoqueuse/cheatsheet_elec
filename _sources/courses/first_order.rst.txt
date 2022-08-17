Systèmes de Premier Ordre 
=========================

Modélisation
------------

Equation différentielle 
+++++++++++++++++++++++

.. math ::

    \tau\frac{d s(t)}{dt} + s(t) = b_1\frac{d e(t)}{dt}+e(t)

* :math:`\tau` désigne la constante de temps [s].

Fonction de transfert
+++++++++++++++++++++

La fonction de transfert d'un système de premier ordre peut s'exprimer sous la forme normalisée suivante :

.. math ::

    H(p)=\frac{N(p)}{\frac{1}{\omega_c}p+1}

* :math:`N(p)` désigne le numérateur de la fonction de transfert (polynôme de degré inférieur ou égale à 1). 
* :math:`\omega_c=\frac{1}{\tau}` désigne la pulsation de coupure à -3dB [rad/s].

Expression du pôle 
++++++++++++++++++

Un système de premier ordre possède un unique pôle. Ce pôle s'obtient en cherchant l'unique racine du dénominateur de la fonction de transfert.

.. math::

    \tau p+1 = 0 \Rightarrow p = -\frac{1}{\tau} = -\omega_c

Exemples (LP)
+++++++++++++

.. math::

    H_{LP}(p)&=\frac{T_0}{\frac{1}{\omega_c}p+1}\\
    H_{HP}(p)&=\frac{\frac{T_\infty}{\omega_0}p}{\frac{1}{\omega_c}p+1}
    

Réponse Temporelle
------------------

La solution complète de l'équation différentielle s'exprime sous la forme :

.. math ::

    s(t)=s_l(t)+s_p(t)

* :math:`s_l(t)`: solution libre (régime libre)

.. math ::

    s_l(t)=\lambda e^{-\frac{1}{\tau} t}

* :math:`s_p(t)`: solution particulière (régime forcé). L'expression du régime forcé dépend de l'allure de l'entrée et des coefficients :math:`b_1` et :math:`b_2`

Exemple
+++++++

Considérons la réponse d'un système de premier ordre a un échelon d'amplitude :math:`E`, c-à-d :math:`e(t)=Eu(t)`. Le système est supposé initialement au repos (:math:`s(0^-)=0`).
Comme l'entrée est un échelon, le regime forcé est de la forme :math:`s_p(t)=Su(t)`. En remplaçant cette expression dans 
l'équation différentielle pour :math:`t\ge 0`, nous obtenons :math:`s_p(t)=T_0E`. Il en vient que :

.. math ::

   s(t)=\lambda e^{-\frac{1}{\tau} t}+T_0E

La constante d'intégration s'obtient en déterminant une condition initiale. 
En intégrant l'équation différentielle entre :math:`t=0^-` et :math:`t=0^+`, nous obtenons :math:`s(0^+) = 0`
En exploitant cette equation, il en vient que :

.. math ::

    s(0^+) =\lambda \times 1 + T_0E = 0 \Rightarrow \lambda = -T_0 E,

Pour un filtre passe-bas de premier ordre, la réponse du système a un échelon d'amplitude :math:`E` s'exprime finalement sous la forme :

.. math ::

    s(t) = T_0 E\left(1-e^{-\frac{1}{\tau} t}\right)

.. plot ::
    :context:
    :include-source: false

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import lti, step


    E = 1
    T_0 = 2
    tau = 10**-2

    H = lti([T_0],[tau, 1])
    t, s = step(H)
    plt.plot(t, E*s, label="s(t)")
    plt.plot(t, E*(t>=0), label="e(t)")
    plt.xlim([0, t[-1]])
    plt.xlabel("temps [s]")
    plt.ylabel("sortie")
    plt.legend()
    plt.grid()

Réponse Fréquentielle
---------------------

La réponse fréquentielle s'obtient en posant :math:`p=j\omega` dans l'expression de la fonction de transfert. Nous obtenons : 

.. math ::

    H(j\omega)=\frac{N(j\omega)}{j\frac{\omega}{\omega_c}+1}


Passe-Bas
+++++++++

* Module :

.. math ::

    |H(j\omega)|=\frac{T_0}{\sqrt{\left(\frac{\omega}{\omega_c}\right)^2+1}}

* Argument : 

.. math ::

    \arg[H(j\omega)]=-\arctan\left( \frac{\omega}{\omega_c} \right)

.. plot ::
    :include-source: false

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import lti

    E = 1
    T_0 = 2
    tau = 10**-2
    wc = 1/tau

    H = lti([T_0],[tau, 1])
    w = np.logspace(0, 4, 200)
    w, Hjw = H.freqresp(w=w)
    H_mod = np.abs(Hjw)
    H_phase = 180*np.angle(Hjw)/np.pi     #convert radian to degree

    # plot figure
    plt.subplot(2,1,1)
    plt.loglog(w,H_mod)
    plt.plot([w[0], w[-1]], [T_0*wc/w[0], T_0*wc/w[-1]],"r--")
    plt.axhline([T_0/np.sqrt(2)],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Magnitude")
    plt.xlim([w[0], w[-1]])
    plt.ylim([0.001, 10])
    plt.grid()
    plt.subplot(2,1,2)
    plt.semilogx(w,H_phase)
    plt.axhline([-45],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Phase [deg]")
    plt.xlabel("w [rad/s]")
    plt.xlim([w[0], w[-1]])
    plt.grid()

Passe-Haut
++++++++++

* Module :

.. math ::

    |H(j\omega)|=\frac{T_\infty\frac{\omega}{\omega_c}}{\sqrt{\left(\frac{\omega}{\omega_c}\right)^2+1}}

* Argument : 

.. math ::

    \arg[H(j\omega)]=90^o-\arctan\left( \frac{\omega}{\omega_c} \right)


.. plot ::
    :include-source: false

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import lti

    E = 1
    T_oo = 2
    tau = 10**-2
    wc = 1/tau

    H = lti([T_oo/wc, 0],[tau, 1])
    w = np.logspace(0, 4, 200)
    w, Hjw = H.freqresp(w=w)
    H_mod = np.abs(Hjw)
    H_phase = 180*np.angle(Hjw)/np.pi     #convert radian to degree

    # plot figure
    plt.subplot(2,1,1)
    plt.loglog(w,H_mod)
    plt.plot([w[0], w[-1]], [T_oo*w[0]/wc, T_oo*w[-1]/wc],"r--")
    plt.axhline([T_oo/np.sqrt(2)],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Magnitude")
    plt.xlim([w[0], w[-1]])
    plt.ylim([0.001, 10])
    plt.grid()
    plt.subplot(2,1,2)
    plt.semilogx(w,H_phase)
    plt.axhline([45],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Phase [deg]")
    plt.xlabel("w [rad/s]")
    plt.xlim([w[0], w[-1]])
    plt.grid()