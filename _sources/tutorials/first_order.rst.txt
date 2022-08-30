Analyse d'un Circuit de Premier Ordre
=====================================

Dans ce tutorial, nous allons réaliser une analyse complète d'un circuit. 
Le circuit considéré est le suivant :

.. figure:: img/RC_LP.svg
  :width: 300
  :align: center
  :alt: RC LP

  RC LP Filter


Fonction de Transfert
---------------------

La fonction de transfert du circuit s'obtient en utilisant le pont diviseur de tension. 
En notant :math:`s(t)` la sortie :math:`V_{out}(t)` et :math:`e(t)` l'entrée :math:`V_{in}(t)`, nous obtenons dans le domaine de Laplace:

.. math ::

    S(p) &= \frac{Z_c}{Z_c+Z_r} E(p)
        &= \frac{\frac{1}{Cp}}{\frac{1}{Cp}+R} S(p)\\
        &= \frac{1}{RCp+1} E(p)

Nous en déduisons que la fonction de transfert du système est égal à 

.. math ::

    H(p) = \frac{S(p)}{E(p)} = \frac{1}{RCp+1}

Pour specifier cette fonction de transfert en Python, nous allons utiliser la module `scipy`.


Réponse Temporelle 
------------------

Le système peut être décrit dans le domaine temporelle par l'équation suivante :

.. math ::

    RC \frac{d s(t)}{dt} + s(t) = e(t)

Réponse Indicielle
++++++++++++++++++

Nous allons nous intéresser à la sortie lorsque l'entrée est un échelon d'amplitude E 

.. math ::

    e(t) = \left\{\begin{array}{cc}E&\text{ si } t\ge 0\\
    0 &\text{ ailleurs}
    \end{array}\right.

La sortie du système est supposée initialement nulle c-a-d  :math:`s(0^-)=0`.

Expression
``````````

* Equation caractéristique :

.. math ::

    RC p + 1 = 0 \Rightarrow p=-\frac{1}{RC}

* Régime Libre :

.. math ::

    s_l(t) = \lambda e^{-\frac{1}{RC} t}

* Régime Forcé : Lorsque l'entrée est un échelon d'amplitude E, le regime permanent s'exprime sous la forme :math:`s_p(t) = S u(t)`. La valeur de :math:`S` s'obtient en injectant l'expression du regime permanent dans l'équation différentielle. Pour :math:`t\ge 0`, nous obtenons :

.. math ::

    s_p(t) = E

* Solution Complète: Pour :math:`t\ge 0`, nous obtenons finalement

.. math ::

    s(t) = s_l(t) + s_p(t) = \lambda e^{-\frac{1}{RC} t} + E


La détermination de la constante d'intégration peut s'obtenir en déterminant la valeur de :math:`s(t)` en :math:`t=0^+`. 
Cette valeur peut s'obtenir en intégrant l'équation différentielle entre :math:`t=0^-` et :math:`t=0^+`.

.. math ::

    RC \int_{0^-}^{0^+}\frac{d s(t)}{dt} dt + \int_{0^-}^{0^+}s(t)dt= E \int_{0^-}^{0^+} 1 dt = 0

Sous l'hypothèse où la seconde intégrale du terme de gauche est nulle et en utilisant le fait que la sortie est initialement nulle, 
nous obtenons :

.. math ::

    RC \left[s(t)\right]_{0^-}^{0^+} = 0 \Rightarrow s(0^+) = 0


En exploitant cette equation, il en vient que :

.. math ::

    s(0^+) =\lambda \times 1 + E = 0 \Rightarrow \lambda = -E

Pour :math:`t\ge 0`, nous obtenons finalement l'expression suivante :

.. math ::

    s(t) = E\left(1-e^{-\frac{1}{RC} t}\right)

Valeurs Remarquables 
````````````````````

* Valeur initiale: :math:`s(0^+)=0`,
* Valeur finale: :math:`s(\infty)=E`,
* Valeur maximale: :math:`max(s(t))=E`,
* Valeur en :math:`t=\tau=RC`, :math:`s(\tau)=0.63E`,
* Valeur en :math:`t=3\tau=3RC`, :math:`s(3\tau)=0.95E`.

Simulation Python
+++++++++++++++++

.. plot ::
    :context: close-figs
    :include-source: true

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import lti, step

    R = 10*(10**3)
    C = 10**(-9)
    num = [1]   
    den = [R*C, 1] 
    H = lti(num, den)


    E = 1
    t, s = step(H)
    plt.plot(t, s, label="s(t)")
    plt.plot(t, E*(t>=0), label="e(t)")
    plt.axhline([0.63*E],c="r", linestyle="--")
    plt.axhline([0.95*E],c="r", linestyle="--")
    plt.axvline([R*C],c="r", linestyle="--")
    plt.axvline([3*R*C],c="r", linestyle="--")
    plt.xlim([0, t[-1]])
    plt.xlabel("temps [s]")
    plt.ylabel("sortie")
    plt.legend()
    plt.grid()

Réponse Fréquentielle
---------------------

Expression
++++++++++

La réponse fréquentielle s'obtient en évaluant la fonction de transfert en :math:`p=j\omega`. Mathématiquement, nous obtenons : 

.. math ::

    H(j\omega) = \frac{1}{jRC\omega+1}


* Module :

.. math ::

    |H(j\omega)| = \frac{1}{\sqrt{(RC\omega)^2+1}}

* Argument :

.. math ::

    \arg[H(j\omega)] = -\arctan\left(RC\omega\right)


Valeurs Remarquables 
````````````````````

* Basse-Fréquence : Lorsque :math:`\omega\to 0`, 

.. math ::
    |H(j\omega)|&\approx 1,\\
    \arg[H(j\omega)]&\approx 0.

* Pulsation de coupure : Lorsque :math:`\omega=\omega_c=\frac{1}{RC}`, 

.. math ::
    
    |H(j\omega_c)|&=\frac{1}{\sqrt{2}},\\
    \arg[H(j\omega_c)]&=-45^o.

* Asymptotes Haute-Fréquences :  

.. math :: 

    \lim_{\omega \to \infty} |H(j\omega)| &= \left(\frac{\omega}{\omega_c}\right)^{-1},\\
    \lim_{\omega \to \infty} \arg[H(j\omega)] &= -90^o.

Simulation Python
+++++++++++++++++

.. plot ::
    :context:
    :include-source: true

    w = np.logspace(3, 7, 200)
    wc = 1/(R*C)
    w, Hjw = H.freqresp(w=w)
    H_mod = np.abs(Hjw)
    H_phase = 180*np.angle(Hjw)/np.pi     #convert radian to degree

    # plot figure
    plt.subplot(2,1,1)
    plt.loglog(w,H_mod)
    plt.plot([w[0], w[-1]], [wc/w[0], wc/w[-1]],"r--")
    plt.axhline([1/np.sqrt(2)],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Magnitude")
    plt.xlim([w[0], w[-1]])
    plt.ylim([0.001, 2])
    plt.grid()
    plt.subplot(2,1,2)
    plt.semilogx(w,H_phase)
    plt.axhline([-45],c="r", linestyle="--")
    plt.axvline([wc],c="r", linestyle="--")
    plt.ylabel("Phase [deg]")
    plt.xlabel("w [rad/s]")
    plt.xlim([w[0], w[-1]])
    plt.grid()