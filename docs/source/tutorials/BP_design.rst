Synthèse d'un filtre passe-bande 
================================

Ce tutorial montre le process complet pour synthétiser un filtre d'ordre N à partir d'un cahier des charges. La méthodologie décrite ici est 
applicable à n'importe quel filtre. 


Cahier des charges
------------------

* Type de filtre: passe-bande, 
* Technique de synthèse: Butterworth, 
* Bande passante : :math:`\omega \in [900, 1111]` rad/s,
* Bande rejetée : :math:`\omega \in [0, 500[ \cup [2000, +\infty[` rad/s,
* Atténuation maximale dans la bande passante: :math:`3` dB,
* Atténuation minimale dans la bande rejetée: :math:`40` dB.


Détermination du Gabarit Normalisé
----------------------------------

Dans un premier temps, nous allons revenir à la conception d'un filtre passe-bas normalisé (:math:`\omega_c=1` rad/s). Pour réaliser cette
étape de normalisation, nous allons utiliser la formule liant la pulsation normalisée :math:`\omega` et la pulsation dénormalisée :math:`\widehat{\omega}` (voir :ref:`mapping-BP`)

.. math ::

    \omega = \frac{\widehat{\omega}^2-\omega_0^2}{\widehat{\omega}\Delta \omega}


Application Numérique
+++++++++++++++++++++

* Bande passante: :math:`\Delta \omega=1111-900=211` rad/s.
* Pulsation centrale : :math:`\omega_0=\sqrt{900\times 1111}=1000` rad/s.
* Valeur du module en :math:`\widehat{\omega}=1111` rad/s: :math:`T_c=10^{-3/20}=0.707`,
* Valeur du module en :math:`\widehat{\omega}=2000` rad/s: :math:`T_s=10^{-40/20}=0.01`.

En utilisant la formule, nous obtenons :

.. math ::

    \omega_c &= \frac{1111^2-1000^2}{1111\times 211}\approx 1~rad/s\\
    \omega_s &= \frac{2000^2-1000^2}{2000\times 211}\approx 7.11~rad/s\\


Représentation du Gabarit
+++++++++++++++++++++++++

.. plot ::

    import matplotlib.pyplot as plt

    options = {"fill": False,"closed": True,"color": 'b',"hatch": "/"}
    fig, axs = plt.subplots(1, 2, figsize=(10, 4)) 

    ax0 = axs[0]
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.set_xlim([100, 10000])
    ax0.set_ylim([0.001, 2])
    xmin, xmax = ax0.get_xlim()
    ymin, ymax = ax0.get_ylim()

    wc = [900, 1111]
    ws = [500, 2000]
    Tc = 0.707
    Ts = 0.01

    polygon_data1 = [[wc[0], ymin], [wc[0],Tc], [wc[1],Tc], [wc[1],ymin], [wc[0], ymin]]
    polygon_data2 = [[xmin,Ts], [ws[0],Ts], [ws[0],1], [ws[1],1], [ws[1],Ts], [xmax,Ts], [xmax,ymax], [xmin,ymax], [xmin,Ts]]
    patch1 = plt.Polygon(polygon_data1,**options)
    patch2 = plt.Polygon(polygon_data2,**options)
    ax0.add_patch(patch1)
    ax0.add_patch(patch2)
    ax0.set_title("filtre BP")
    ax0.set_xlabel("pulsation (rad/s)")
    ax0.set_ylabel("module")

    ax1 = axs[1]
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim([0.1, 100])
    ax1.set_ylim([0.001, 2])
    xmin, xmax = ax1.get_xlim()
    ymin, ymax = ax1.get_ylim()
    ax1.set_title("filtre LP normalisé")
    ax1.set_xlabel("pulsation (rad/s)")
    ax1.set_ylabel("module")

    wc = 1
    ws = 7.11
    Tc = 0.707
    Ts = 0.01

    polygon_data1 = [[xmin,Tc], [wc,Tc], [wc,ymin], [xmin,ymin]]
    polygon_data2 = [[xmin,ymax], [xmin,1], [ws,1], [ws,Ts], [xmax,Ts], [xmax,ymax], [xmin,ymax]]
    patch1 = plt.Polygon(polygon_data1,**options)
    patch2 = plt.Polygon(polygon_data2,**options)
    ax1.add_patch(patch1)
    ax1.add_patch(patch2)
    fig.tight_layout()


Détermination de l'ordre
------------------------

Il est possible de déterminer l'ordre du filtre passe-bas normalisé en utilisant le comportement asymptotique :

.. math ::

    N = \left\lceil-\frac{\ln\left(\frac{0.707}{0.01}\right)}{\ln\left(\frac{1}{7.11}\right)}\right\rceil = 3


Synthèse du Filtre Normalisé
----------------------------

Pour synthétiser le filtre, nous allons utiliser la technique de synthèse de Butterworth. La fonction de transfert du filtre normalisé peut s'exprimer sous la forme factorisée suivante (zpk):


.. math ::

    H_n(p)=k\frac{\prod_{l=1}^3 (p-z_l)}{\prod_{l=1}^3 (p-p_l)}


Il est possible d'obtenir les pôles :math:`p_l` et les zéros :math:`z_l` ainsi que le gain k du filtre normalisé en utilisant `scipy`:


.. code ::

    from scipy.signal import butter

    z,p,k = butter(3, 1, "low", analog=True, output="zpk")

Nous obtenons les paramètres suivants:

* zéros: :math:`z_l=\{\}`, 
* pôles: :math:`p_l=\{-0.5+0.8660254, -1, -0.5-0.8660254j\}`,
* gain: :math:`k=1`

Dénormalisation du Filtre 
-------------------------

Pour dénormaliser le filtre, nous allons opérer un mapping des pôles et zéros. Dans le cas d'un passe-bande, le mapping des pôles est donné par (voir :ref:`mapping-BP-zpk`). 

.. math ::     

    \widehat{p}_l&=\alpha p_l \pm \sqrt{\alpha^2p_l^2-\omega_0^2}\\

* :math:`\alpha=\Delta \omega/2=211/2=105.5` rad/s désigne la moitié de la bande passante,
* :math:`p_l` correspond aux pôles du filtre normalisé, 
* :math:`\widehat{p}_l` correspond aux pôles du filtre dénormalisé.

Après dénormalisation, nous obtenons un filtre d'ordre :math:`2N=6`.
Pour conserver un gain maximum unitaire dans la bande passante, il est également nécessaire de changer le coefficient :math:`k` de la manière suivante:

.. math ::

    \widehat{k} = k (\Delta \omega)^N


Application Numérique
+++++++++++++++++++++

Après dénormalisation, nous obtenons un filtre d'ordre 6 avec les paramètres suivants :

* zéros: 3 zéros en 0 (filtre passe-bande d'ordre 6)
    * :math:`\widehat{z}_l=\{0, 0, 0\}`, 
* pôles: 3 paires de pôles complexes-conjugués
    * :math:`\widehat{p}_1=-47.943-911.424j` et :math:`\widehat{p}_1^*=-47.943+911.424j`,
    * :math:`\widehat{p}_2=-57.556-1094.155j` et :math:`\widehat{p}_2^*=-57.556+1094.155j`
    * :math:`\widehat{p}_3=-105.5-994.419j` et :math:`\widehat{p}_3^*=-105.5+994.419j`,
    
* gain `k`:
    * :math:`\widehat{k} = 1 \times (211)^3 =9393931`


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import butter
    import matplotlib.pyplot as plt

    z,p,k  =  butter(3, 1, "low", analog=True, output="zpk")
    z2,p2,k2 =  butter(3, [900, 1100], "bandpass", analog=True, output="zpk")

    fig, axs = plt.subplots(1, 2,figsize=(10,4))
    axs[0].plot(np.real(p),np.imag(p),'x')
    axs[0].plot(np.real(z),np.imag(z),'o')
    axs[0].set_xlabel("Re (.)")
    axs[0].set_ylabel("Im (.)")
    axs[0].axis("equal")
    axs[0].grid()
    axs[0].set_title("Filtre LP Normalisé")
    axs[1].plot(np.real(p2),np.imag(p2),'x')
    axs[1].plot(np.real(z2),np.imag(z2),'o')
    axs[1].set_xlabel("Re (.)")
    axs[1].set_ylabel("Im (.)")
    axs[1].axis("equal")
    axs[1].grid()
    axs[1].set_title("Filtre BP")
    fig.tight_layout()

Vérification
------------

Pour vérifier que le filtre dénormalisé respecte bien les contraintes du cahier des charges, une solution naturelle consiste à afficher la réponse fréquentielle du filtre dénormalisé. 

.. math ::

    H(p)=\widehat{k}\frac{\prod_{l=1}^3 (p-\widehat{z}_l)}{\prod_{l=1}^6 (p-\widehat{p}_l)}

.. code ::

    from scipy.signal import lti
    import matplotlib.pyplot as plt

    k2 = 9393931
    z2 = [0.+0.j, 0.+0.j, 0.+0.j]
    p2 = [ -47.943-911.374j, -105.5-994.369j, -47.943 +911.374j, -57.556+1094.106j, -105.5 +994.369j, -57.556-1094.106j]
    H = lti(z2, p2, k2)
    w, Hjw = H.freqresp()
    plt.loglog(w, np.abs(Hjw))
    plt.xlabel("pulsation (rad/s)")
    plt.ylabel("module")


.. plot :: 

    import matplotlib.pyplot as plt
    from scipy.signal import lti, butter 

    z, p, k = butter(3, [900, 1111], "bandpass", analog=True, output="zpk")
    H = lti(z, p, k)

    fig = plt.figure()
    w, Hjw = H.freqresp()
    plt.loglog(w, np.abs(Hjw))
    plt.xlabel("pulsation (rad/s)")
    plt.ylabel("module")
    ax = plt.gca()

    options = {"fill": False,"closed": True,"color": 'b',"hatch": "/"}
    wc = [900, 1111]
    ws = [500, 2000]
    Tc = 0.707
    Ts = 0.01
    ax.set_xlim([100, 10000])
    ax.set_ylim([0.001, 2])
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()

    polygon_data1 = [[wc[0], ymin], [wc[0],Tc], [wc[1],Tc], [wc[1],ymin], [wc[0], ymin]]
    polygon_data2 = [[xmin,Ts], [ws[0],Ts], [ws[0],1], [ws[1],1], [ws[1],Ts], [xmax,Ts], [xmax,ymax], [xmin,ymax], [xmin,Ts]]
    patch1 = plt.Polygon(polygon_data1,**options)
    patch2 = plt.Polygon(polygon_data2,**options)
    ax.add_patch(patch1)
    ax.add_patch(patch2)
    fig.tight_layout()