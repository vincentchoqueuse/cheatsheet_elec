Synthèse des Filtres d'ordre N
==============================

Un filtre est souvent représenté par une fonction de transfert qui détermine comment les différentes fréquences d'un signal d'entrée sont affectées. L'ordre d'un :math:`N` d'un filtre est lié à la puissance la plus élevée dans son équation différentielle, ce qui, en retour, est souvent directement lié au nombre de composants nécessaires pour réaliser le filtre.

Plus :math:`N` est élevé, plus le filtre est capable d'offrir une transition abrupte entre les fréquences qu'il laisse passer et celles qu'il rejette. Cependant, cela vient aussi avec une complexité accrue et des exigences plus strictes en termes de composants et de conception.

Concevoir un filtre n'est pas simplement une question de choix de l'ordre approprié. La synthèse des filtres concerne la définition des caractéristiques désirées du filtre (comme la bande passante, l'atténuation, la phase) et la conversion de ces spécifications en une conception de circuit ou un algorithme. L'ingénieur doit trouver un compromis entre plusieurs paramètres : rapidité de transition entre les bandes passantes et de coupure, ondulation acceptable dans la bande passante, atténuation minimale dans la bande de coupure, et bien sûr, la complexité et la faisabilité du filtre.

Méthodologie
------------

* Étape 1 : Synthèse du filtre normalisé

    - Définir les spécifications du filtre : Avant toute chose, il est nécessaire de définir les spécifications souhaitées pour le filtre, comme la bande passante, l'atténuation, l'ondulation dans la bande passante, etc.
    - Choisir la technique de synthèse : Cela peut être Butterworth, Chebyshev, elliptique, etc. Chaque type a ses propres caractéristiques.
    - Déterminer l'ordre :math:`N` du filtre : En utilisant les spécifications et le type de réponse choisie, déterminez l'ordre minimal :math:`N` du filtre nécessaire pour satisfaire ces spécifications.
    - Synthèse de la fonction de transfert : Avec l'ordre déterminé et le type de réponse, utilisez les formules appropriées pour déduire la fonction de transfert :math:`H_n(p)` du filtre normalisé.

* Étape 2 : Dénormalisation. La dénormalisation consiste à adapter le filtre conçu dans l'étape précédente à vos besoins réels, comme la fréquence de coupure ou la bande passante.

    - Réaliser la substitution :math:`p\to f(p)` pour obtenir la fonction de transfert du filtre dénormalisé.

* Étape 3 : Réalisation du filtre

    - Sélection des composants : À partir de la fonction de transfert dénormalisée, choisissez des composants (résistances, condensateurs, inductances, etc.) pour réaliser physiquement le filtre.

    - Assemblage et test : Une fois que vous avez tous les composants nécessaires, assemblez le filtre. Testez ensuite ses performances pour vous assurer qu'il répond aux spécifications.


Denormalisation
---------------

Pour synthétiser un filtre d'ordre N, la procédure classique consiste à d'abord synthétiser son équivalent "passe-bas" normalisé puis à réaliser une dénormalisation. Soit :math:`H_n(p)` la fonction de transfert du filtre normalisé. La fonction du filtre dénormalisé s'obtient en modifiant la variable p de la manière suivante :

.. math ::

    H(p) = \frac{N(p)}{D(p)}= \left.H_n(p)\right|_{p\to f(p)}

* :math:`f(p)`: fonction de transformation,
* :math:`H_n(p)`: fonction de transfert du filtre normalisé.


Mapping fréquentiel 
+++++++++++++++++++

Lors de la dénormalisation, la pulsation :math:`\omega` est mappé en une ou plusieurs pulsations :math:`\widehat{\omega}`. Le lien entre 
:math:`\omega` et :math:`\widehat{\omega}` est donné par l'équation : 

.. math ::

    \omega = \frac{1}{j}f(j\widehat{\omega})


Mapping des pôles et zéros  
++++++++++++++++++++++++++

Lors de la dénormalisation, le pôle :math:`p_l` est mappé en un ou plusieurs pôles :math:`\widehat{p}_l`. Le lien entre 
:math:`p_l` et :math:`\widehat{p}_l` est donné par l'équation : 

.. math ::

    p_l = f(\widehat{p}_l)


Passe-Bas 
---------

Transformation 
++++++++++++++

.. math ::

    f(p) = \frac{p}{\omega_c}


Mapping Fréquentiel 
+++++++++++++++++++

La pulsation :math:`\omega` rad/s du filtre normalisé est mappée à la pulsation :math:`\widehat{\omega}` telle que 

.. math :: 

    j\omega = \frac{j\widehat{\omega}}{\omega_c} \Rightarrow \omega=\frac{\widehat{\omega}}{\omega_c}

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    num, den = cheby1(5,1,1, analog=True)
    num2, den2 = cheby1(5,1,2, analog=True)
    sys = lti(num,den)
    sys2 = lti(num2,den2)
    w = np.arange(-5,5,0.05)
    w,Hjw = sys.freqresp(w=w)
    w2,Hjw2 = sys2.freqresp(w=w)
    

    fig = plt.figure(figsize=(8, 6))
    ax0 = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=2)
    ax0.plot(np.abs(Hjw),w)
    ax0.axhline([1.2],c="r",linestyle="--")
    ax0.set_ylabel("w [rad/s]")
    ax0.set_xlabel("Module")
    ax0.grid()
    ax0.set_xlim([0,1])
    ax0.set_ylim([w[0],w[-1]])
    ax0.set_title("Filtre Normalisé")
    ax0.invert_xaxis()

    ax1 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=2)
    ax1.plot(w, w/2)
    ax1.set_xlabel("$\widehat{w}$ [rad/s]")
    ax1.set_ylabel("$w$ [rad/s]")
    ax1.axhline([1.2],c="r",linestyle="--")
    ax1.axvline([1.2*2],c="r",linestyle="--")
    ax1.set_xlim([w[0],w[-1]])
    ax1.set_ylim([w[0],w[-1]])
    ax1.grid()

    ax2 = plt.subplot2grid((3, 3), (2, 1), colspan=2, rowspan=1)
    ax2.plot(w2, np.abs(Hjw2))
    ax2.set_xlabel("$\widehat{w}$ [rad/s]")
    ax2.set_ylabel("Module")
    ax2.set_title("Filtre Dénormalisé")
    ax2.set_ylim([0,1])
    ax2.set_xlim([w[0],w[-1]])
    ax2.axvline([1.2*2],c="r",linestyle="--")
    ax2.grid()
    fig.tight_layout()

Mapping des pôles et zéros  
++++++++++++++++++++++++++

Les pôles :math:`p_l` et zéros :math:`z_l` du filtre normalisé sont mappés aux pôles et zéros

.. math::     

    \widehat{p}_l&=\omega_c p_l\\
    \widehat{z}_l&=\omega_c z_l

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    z,p,k = cheby1(5,3,1, analog=True,output='zpk')
    z2,p2,k2 = cheby1(5,3,2, analog=True,output='zpk')

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].plot(np.real(p),np.imag(p),'x')
    axs[0].plot(np.real(z),np.imag(z),'o')
    axs[0].set_xlabel("Re (.)")
    axs[0].set_ylabel("Im (.)")
    axs[0].axis("equal")
    axs[0].grid()
    axs[0].set_title("Filtre Normalisé")
    axs[1].plot(np.real(p2),np.imag(p2),'x')
    axs[1].plot(np.real(z2),np.imag(z2),'o')
    axs[1].set_xlabel("Re (.)")
    axs[1].set_ylabel("Im (.)")
    axs[1].axis("equal")
    axs[1].grid()
    axs[1].set_title("Filtre Dénormalisé")
    fig.tight_layout()



Passe-Haut 
----------

Transformation 
++++++++++++++

.. math ::

    f(p) = \frac{\omega_c}{p}

Mapping Fréquentiel 
+++++++++++++++++++

La pulsation :math:`\omega` du filtre normalisé est mappée à la pulsation :math:`\widehat{\omega}` telle que 

.. math :: 

    j\omega = \frac{\omega_c}{j\widehat{\omega}} \Rightarrow \omega =-\frac{\omega_c}{\widehat{\omega}}


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    num, den = cheby1(5,1,1, analog=True)
    num2, den2 = cheby1(5,1,2, btype="highpass", analog=True)
    sys = lti(num,den)
    sys2 = lti(num2,den2)
    w = np.arange(-5,5,0.05)
    wp = np.arange(-5,-0.05,0.05)
    wm = np.arange(0.05,5,0.05)
    w,Hjw = sys.freqresp(w=w)
    w2,Hjw2 = sys2.freqresp(w=w)
    

    fig = plt.figure(figsize=(8, 6))
    ax0 = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=2)
    ax0.plot(np.abs(Hjw),w)
    ax0.axhline([1.2],c="r",linestyle="--")
    ax0.set_ylabel("w [rad/s]")
    ax0.set_xlabel("Module")
    ax0.grid()
    ax0.set_xlim([0,1])
    ax0.set_ylim([w[0],w[-1]])
    ax0.set_title("Filtre Normalisé")
    ax0.invert_xaxis()

    ax1 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=2)
    ax1.plot(wm, -2/wm, "C0")
    ax1.plot(wp, -2/wp, "C0")
    ax1.set_xlabel("$\widehat{w}$ [rad/s]")
    ax1.set_ylabel("$w$ [rad/s]")
    ax1.axhline([1.2],c="r",linestyle="--")
    ax1.axvline([-2/1.2],c="r",linestyle="--")
    ax1.set_xlim([w[0],w[-1]])
    ax1.set_ylim([w[0],w[-1]])
    ax1.grid()

    ax2 = plt.subplot2grid((3, 3), (2, 1), colspan=2, rowspan=1)
    ax2.plot(w2, np.abs(Hjw2))
    ax2.set_xlabel("$\widehat{w}$ [rad/s]")
    ax2.set_ylabel("Module")
    ax2.set_title("Filtre Dénormalisé")
    ax2.set_ylim([0,1])
    ax2.set_xlim([w[0],w[-1]])
    ax2.axvline([-2/1.2],c="r",linestyle="--")
    ax2.grid()
    fig.tight_layout()

Mapping des pôles et zéros  
++++++++++++++++++++++++++

Les pôles :math:`p_l` et zéros :math:`z_l` du filtre normalisé sont mappés aux pôles et zéros

.. math::     

    \widehat{p}_l&=\omega_c /p_l\\
    \widehat{z}_l&=\omega_c /z_l

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    z,p,k = cheby1(5,3,1, analog=True,output='zpk')
    z2,p2,k2 = cheby1(5,3,2, btype="highpass", analog=True,output='zpk')

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].plot(np.real(p),np.imag(p),'x')
    axs[0].plot(np.real(z),np.imag(z),'o')
    axs[0].set_xlabel("Re (.)")
    axs[0].set_ylabel("Im (.)")
    axs[0].axis("equal")
    axs[0].grid()
    axs[0].set_title("Filtre Normalisé")
    axs[1].plot(np.real(p2),np.imag(p2),'x')
    axs[1].plot(np.real(z2),np.imag(z2),'o')
    axs[1].set_xlabel("Re (.)")
    axs[1].set_ylabel("Im (.)")
    axs[1].axis("equal")
    axs[1].grid()
    axs[1].set_title("Filtre Dénormalisé")
    fig.tight_layout()


Passe-Bande 
-----------

Transformation 
++++++++++++++

.. math ::

    f(p) = \frac{p^2+\omega_0^2}{p\Delta \omega}

* :math:`\omega_0=\sqrt{\omega_{c1}\omega_{c2}}` désigne la pulsation centrale,
* :math:`\Delta \omega=\omega_{c2}-\omega_{c1}` désigne la largeur de la bande passante.


Mapping Fréquentiel 
+++++++++++++++++++

La pulsation :math:`\omega` du filtre normalisé est mappée à la pulsation :math:`\widehat{\omega}` où 

.. math :: 

    j\omega = \frac{(j\widehat{\omega})^2+\omega_0^2}{j\widehat{\omega}\Delta \omega} \Rightarrow \omega = \frac{\widehat{\omega}^2-\omega_0^2}{\widehat{\omega}\Delta \omega}

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    num, den = cheby1(5,1,1, analog=True)
    num2, den2 = cheby1(5,1,[2,4], btype="bandpass", analog=True)
    sys = lti(num,den)
    sys2 = lti(num2,den2)
    w = np.arange(-5,5,0.05)
    wp = np.arange(-5,-0.05,0.05)
    wm = np.arange(0.05,5,0.05)
    w,Hjw = sys.freqresp(w=w)
    w2,Hjw2 = sys2.freqresp(w=w)
    w0 = np.sqrt(2*4)
    B = 4-2
    w_hat = np.roots([1, -1.2*B, -w0**2]) 

    fig = plt.figure(figsize=(8, 6))
    ax0 = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=2)
    ax0.plot(np.abs(Hjw),w)
    ax0.axhline([1.2],c="r",linestyle="--")
    ax0.set_ylabel("w [rad/s]")
    ax0.set_xlabel("Module")
    ax0.grid()
    ax0.set_xlim([0,1])
    ax0.set_ylim([w[0],w[-1]])
    ax0.set_title("Filtre Normalisé")
    ax0.invert_xaxis()

    
    ax1 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=2)
    ax1.plot(wm, (wm**2-w0**2)/(wm*B),"C0")
    ax1.plot(wp, (wp**2-w0**2)/(wp*B),"C0")
    ax1.set_xlabel("$\widehat{w}$ [rad/s]")
    ax1.set_ylabel("$w$ [rad/s]")
    ax1.axhline([1.2],c="r",linestyle="--")
    ax1.axvline([w_hat[0]],c="r",linestyle="--")
    ax1.axvline([w_hat[1]],c="r",linestyle="--")
    ax1.set_xlim([w[0],w[-1]])
    ax1.set_ylim([w[0],w[-1]])
    ax1.grid()

    ax2 = plt.subplot2grid((3, 3), (2, 1), colspan=2, rowspan=1)
    ax2.plot(w2, np.abs(Hjw2))
    ax2.set_xlabel("$\widehat{w}$ [rad/s]")
    ax2.set_ylabel("Module")
    ax2.set_title("Filtre Dénormalisé")
    ax2.set_ylim([0,1])
    ax2.set_xlim([w[0],w[-1]])
    ax2.axvline([w_hat[0]],c="r",linestyle="--")
    ax2.axvline([w_hat[1]],c="r",linestyle="--")
    ax2.grid()
    fig.tight_layout()

Mapping des pôles et zéros  
++++++++++++++++++++++++++

Les pôles :math:`p_l` et zéros :math:`z_l` du filtre normalisé sont mappés aux pôles et zéros

.. math::     

    \widehat{p}_l&=\alpha p_l \pm \sqrt{\alpha^2p_l^2-\omega_0^2}\\
    \widehat{z}_l&=\alpha z_l \pm \sqrt{\alpha^2z_l^2-\omega_0^2}

où :math:`\alpha=\Delta \omega/2`. Pour obtenir un passe-bande, il est également nécessaire d'ajouter plusieurs zéros en 0.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    z,p,k  = cheby1(5,3,1, analog=True,output='zpk')
    z2,p2,k2 = cheby1(5,3,[2,4], btype="bandpass", analog=True,output='zpk')

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].plot(np.real(p),np.imag(p),'x')
    axs[0].plot(np.real(z),np.imag(z),'o')
    axs[0].set_xlabel("Re (.)")
    axs[0].set_ylabel("Im (.)")
    axs[0].axis("equal")
    axs[0].grid()
    axs[0].set_title("Filtre Normalisé")
    axs[1].plot(np.real(p2),np.imag(p2),'x')
    axs[1].plot(np.real(z2),np.imag(z2),'o')
    axs[1].set_xlabel("Re (.)")
    axs[1].set_ylabel("Im (.)")
    axs[1].axis("equal")
    axs[1].grid()
    axs[1].set_title("Filtre Dénormalisé")
    fig.tight_layout()


Rejecteur 
---------

Transformation 
++++++++++++++

.. math ::

    f(p) = \frac{p\Delta \omega}{p^2+\omega_0^2}

où :math:`\omega_0=\sqrt{\omega_{c1}\omega_{c2}}` désigne la pulsation centrale et :math:`\Delta \omega=\omega_{c2}-\omega_{c1}` désigne la largeur de la bande passante.

Mapping Fréquentiel 
+++++++++++++++++++

La pulsation :math:`\omega` du filtre normalisé est mappée à la pulsation :math:`\widehat{\omega}` où 

.. math :: 

    j\omega = \frac{j\widehat{\omega}\Delta \omega}{(j\widehat{\omega}^2)+\omega_0^2}  \Rightarrow \omega = \frac{\widehat{\omega}\Delta \omega}{\omega_0^2-\widehat{\omega}^2}  

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    num, den = cheby1(5,1,1, analog=True)
    num2, den2 = cheby1(5,1,[2,4], btype="bandstop", analog=True)
    sys = lti(num,den)
    sys2 = lti(num2,den2)
    w = np.arange(-5,5,0.05)
    w0 = np.sqrt(2*4)
    w_0 = np.arange(-5,-w0-0.05,0.05)
    w_1 = np.arange(-w0+0.05,w0-0.05,0.05)
    w_2 = np.arange(w0+0.05, 5,0.05)
    w,Hjw = sys.freqresp(w=w)
    w2,Hjw2 = sys2.freqresp(w=w)
    
    B = 4-2
    w_hat = np.roots([1.2, B, -1.2*w0**2]) 

    fig = plt.figure(figsize=(8, 6))
    ax0 = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=2)
    ax0.plot(np.abs(Hjw),w)
    ax0.axhline([1.2],c="r",linestyle="--")
    ax0.set_ylabel("w [rad/s]")
    ax0.set_xlabel("Module")
    ax0.grid()
    ax0.set_xlim([0,1])
    ax0.set_ylim([w[0],w[-1]])
    ax0.set_title("Filtre Normalisé")
    ax0.invert_xaxis()

    ax1 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=2)
    ax1.plot(w_0, (w_0*B)/(-w_0**2+w0**2),"C0")
    ax1.plot(w_1, (w_1*B)/(-w_1**2+w0**2),"C0")
    ax1.plot(w_2, (w_2*B)/(-w_2**2+w0**2),"C0")
    ax1.set_xlabel("$\widehat{w}$ [rad/s]")
    ax1.set_ylabel("$w$ [rad/s]")
    ax1.axhline([1.2],c="r",linestyle="--")
    ax1.axvline([w_hat[0]],c="r",linestyle="--")
    ax1.axvline([w_hat[1]],c="r",linestyle="--")
    ax1.set_xlim([w[0],w[-1]])
    ax1.set_ylim([w[0],w[-1]])
    ax1.grid()

    ax2 = plt.subplot2grid((3, 3), (2, 1), colspan=2, rowspan=1)
    ax2.plot(w2, np.abs(Hjw2))
    ax2.set_xlabel("$\widehat{w}$ [rad/s]")
    ax2.set_ylabel("Module")
    ax2.set_title("Filtre Dénormalisé")
    ax2.set_ylim([0,1])
    ax2.set_xlim([w[0],w[-1]])
    ax2.axvline([w_hat[0]],c="r",linestyle="--")
    ax2.axvline([w_hat[1]],c="r",linestyle="--")
    ax2.grid()
    fig.tight_layout()

Mapping des pôles et zéros  
++++++++++++++++++++++++++

Les pôles :math:`p_l` et zéros :math:`z_l` du filtre normalisé sont mappés aux pôles et zéros

.. math::     

    \widehat{p}_l&=\alpha p_l^{-1} \pm \sqrt{\alpha^2p_l^{-2}-\omega_0^2}\\
    \widehat{z}_l&=\alpha z_l^{-1} \pm \sqrt{\alpha^2z_l^{-2}-\omega_0^2}

où :math:`\alpha=\Delta \omega/2`. Pour obtenir un rejecteur, il est également nécessaire d'ajouter plusieurs zéros en :math:`\pm j\omega_0`.

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti, cheby1
    import matplotlib.pyplot as plt

    z,p,k = cheby1(5,3,1, analog=True,output='zpk')
    z2,p2,k2 = cheby1(5,3,[2,4], btype="bandstop", analog=True,output='zpk')

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].plot(np.real(p), np.imag(p),'x')
    axs[0].plot(np.real(z), np.imag(z),'o')
    axs[0].set_xlabel("Re (.)")
    axs[0].set_ylabel("Im (.)")
    axs[0].axis("equal")
    axs[0].grid()
    axs[0].set_title("Filtre Normalisé")
    axs[1].plot(np.real(p2),np.imag(p2),'x')
    axs[1].plot(np.real(z2),np.imag(z2),'o')
    axs[1].set_xlabel("Re (.)")
    axs[1].set_ylabel("Im (.)")
    axs[1].axis("equal")
    axs[1].grid()
    axs[1].set_title("Filtre Dénormalisé")
    fig.tight_layout()
