Expression de la valeur initiale 
=================================

Introduction
------------

Lorsqu'un système est excité par une entrée :math:`e(t)` en :math:`t=0^+`, la sortie :math:`s(t)` peut
présenter différents comportements. Ces différents comportements permettent d'identifier le type de filtre (passe-bas, passe-haut, etc) et certains paramètres.

Dans ce tutorial, nous nous intéressons spécifiquement au comportement à l'excitation, c-à-d en :math:`t=0^+`.

Pour analyser le comportement en :math:`t=0^+`, ce tutorial présente deux approches, l'une basée sur l'équation différentielle et l'autre sur la fonction de transfert.
Pour des raisons de simplicité, les approches présentées ci dessous se limitent au cas des systèmes de second ordre. 

Approche Temporelle
-------------------

Considérons un système de second ordre décrit par l'équation différentielle suivante

.. math ::

    a_2 \ddot{s}(t)+a_1 \dot{s}(t)+a_0 s(t)=b_2 \ddot{e}(t)+b_1 \ddot{e}(t)+b_0 e(t)

Valeur Initiale
+++++++++++++++

Il est possible de trouver la valeur initiale en :math:`t=0^+`
en intégrant plusieurs fois l'équation différentielle entre :math:`0^-` et :math:`0^+`. 

En intégrant deux fois l'équation différentielle entre :math:`0^-` et :math:`0^+`, nous obtenons :

.. math ::

    a_2 \int\int_{0^-}^{0^+}\ddot{s}(t)dt^2+a_1 \int\int_{0^-}^{0^+}\dot{s}(t)dt^2 +a_0 \int\int_{0^-}^{0^+}s(t)dt^2\\
    =b_2 \int\int_{0^-}^{0^+}\ddot{e}(t)dt^2+b_1 \int\int_{0^-}^{0^+}\dot{e}(t)dt^2+b_0 \int\int_{0^-}^{0^+}e(t)dt^2

En supposant que l'entrée et la sortie ne contiennent pas d'impulsion, les deux derniers termes des deux membres sont nuls.
Dans ce contexte, l'égalité se simplifie sous la forme :

.. math ::

    a_2 \left[s(t)\right]_{0^-}^{0^+}=b_2 \left[e(t)\right]_{0^-}^{0^+}

et donc :

.. math ::

    a_2(s(0^+)-s(0^-)) = b_2(e(0^+)-e(0^-))\tag{1}


En intégrant une fois l'équation différentielle entre :math:`0^-` et :math:`0^+`, nous obtenons :

.. math ::

    a_2 \int_{0^-}^{0^+}\ddot{s}(t)dt+a_1 \int_{0^-}^{0^+}\dot{s}(t)dt +a_0 \int_{0^-}^{0^+}s(t)dt=b_2 \int_{0^-}^{0^+}\ddot{e}(t)dt+b_1 \int_{0^-}^{0^+}\dot{e}(t)dt+b_0 \int_{0^-}^{0^+}e(t)dt

Sous les mêmes hypothèses, nous trouvons alors :

.. math ::

    a_2  \left[\dot{s}(t)\right]_{0^-}^{0^+}+a_1  \left[s(t)\right]_{0^-}^{0^+} =b_2 \left[\dot{e}(t)\right]_{0^-}^{0^+}+b_1  \left[e(t)\right]_{0^-}^{0^+}
   
et donc :

.. math ::

    a_2  \left(\dot{s}(0^+)-\dot{s}(0^-)\right)+a_1 \left(s(0^+)-s(0^-)\right) =b_2 \left(\dot{e}(0^+)-\dot{e}(0^-)\right)+b_1  \left(e(0^+)-e(0^-)\right)\tag{2}
    

Ces relations permettent de définir un système d'équation. Pour simplfiier la résolution, nous allons utiliser une notation matricielle. 
Définissons tout d'abord les vecteurs suivants :

.. math ::

    \mathbf{s}(t) &= \begin{bmatrix} s(t) \\ \dot{s}(t)\end{bmatrix} \\
    \mathbf{e}(t) &= \begin{bmatrix} e(t) \\ \dot{e}(t)\end{bmatrix}

Nous obtenons alors le système 

.. math ::

    \begin{bmatrix}a_2 & 0 \\ a_1 &a_2\end{bmatrix}\left(\mathbf{s}(0^+)-\mathbf{s}(0^-)\right) = \begin{bmatrix}b_2 & 0 \\ b_1 &b_2 \end{bmatrix}\left(\mathbf{e}(0^+)-\mathbf{e}(0^-)\right)

En utilisant le fait que

.. math ::

    \begin{bmatrix}a_2 & 0 \\ a_1 &a_2\end{bmatrix}^{-1} = \frac{1}{a_2^2}\begin{bmatrix}a_2 & 0 \\ -a_1 &a_2\end{bmatrix},

nous obtenons :

.. math ::

    \mathbf{s}(0^+) = \frac{1}{a_2^2}\begin{bmatrix}a_2 & 0 \\ -a_1 &a_2\end{bmatrix}\begin{bmatrix}b_2 & 0 \\ b_1 &b_2 \end{bmatrix}\left(\mathbf{e}(0^+)-\mathbf{e}(0^-)\right) + \mathbf{s}(0^-)

La sortie et sa dérivée s'expriment alors sous la forme :

.. math ::

    \mathbf{s}(0^+) = \frac{1}{a_2^2}\begin{bmatrix}a_2b_2 & 0 \\ a_2b_1-a_1b_2 &a_2 b_2 \end{bmatrix}\left(\mathbf{e}(0^+)-\mathbf{e}(0^-)\right) + \mathbf{s}(0^-)

En introduisant la notion de variation, il en vient que : 

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    = \frac{1}{a_2^2}\begin{bmatrix}a_2b_2 & 0 \\ a_2b_1-a_1b_2 &a_2 b_2 \end{bmatrix}
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}

Exemples
--------

Dans cette partie, nous nous intéressons aux comportements des filtres de second ordre de type passe-bas, passe-bande, passe-haut et rejecteur.
les

Pour ces filtres, nous obtenons la relation générale :

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    =  \omega_0^2\begin{bmatrix} b_2  & 0 \\ b_1 -2m b_2 \omega_0 & b_2 \end{bmatrix}
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}


Propriétés 
++++++++++


* Passe-bas :

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    = \mathbf{0} 

* Passe-bande :

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    =  T_m\begin{bmatrix} 0 & 0 \\ 2m  \omega_0   & 0 \end{bmatrix}
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}

* Passe-haut :

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    =  T_{\infty}\begin{bmatrix} 1 & 0 \\ - 2m \omega_0   & 1  \end{bmatrix}
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}

* Rejecteur :

.. math ::

    \begin{bmatrix}
    s(0^+)-s(0^-)\\
    \dot{s}(0^+)-\dot{s}(0^-)
    \end{bmatrix}
    =  T_{0}\begin{bmatrix} 1 & 0 \\ - 2m \omega_0   & 1  \end{bmatrix}
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}



Illustrations
+++++++++++++

Considérons le cas où l'entrée est un échelon d'amplitude :math:`E=1`. Dans ce contexte, le vecteur d'entrée est égale à 

.. math ::
    
    \begin{bmatrix}
    e(0^+)-e(0^-)\\
    \dot{e}(0^+)-\dot{e}(0^-)
    \end{bmatrix}=\begin{bmatrix}1 \\ 0\end{bmatrix}

La figure suivante présente la réponse indicielle pour un filtre passe-bas, passe-bande, passe-haut et rejecteur ayant la même pulsation propre :math:`\omega_0=1` rad/s, le même coefficient d'amortissement :math:`m=0.5` et le même 
coefficient d'amplification :math:`T_0=T_\infty=T_m=2`.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    m = 0.5
    w0 = 1
    T = 2

    den = [(1/(w0**2)),2*m/w0,1]
    sys1 = lti([T],den)
    sys2 = lti([2*m*T/w0,0],den)
    sys3 = lti([T/(w0**2),0,0],den)
    sys4 = lti([T/(w0**2),0,T],den)
    
    t = np.arange(0,10,0.05)
    name_list = ["Passe-Bas","Passe-Bande","Passe-Haut","Rejecteur"]
    plt.plot(t,t>=0,label="u(t)")
    for indice, sys in enumerate([sys1,sys2,sys3,sys4]):
        t,s = sys.step(T=t)
        t_2 = np.insert(t, 0, [-1,0], axis=0)
        s_2 = np.insert(s, 0, [0,0], axis=0)
        plt.plot(t_2,s_2,label=name_list[indice])
    plt.xlim([-1,10])
    plt.xlabel("temps [s]")
    plt.ylabel("s(t)")
    plt.legend(loc=4)

Nous observons rapidement que :

    * Seuls les filtres passe-haut et rejecteur laissent passer les discontinuités en entrée.
    * Seuls les filtres passe-bas et rejecteur possèdent un regime permanent non nul.

