Liste des Signaux
=================

Impulsion
---------

Modèle Mathématique 
+++++++++++++++++++

.. math ::

    \delta(t)=\left\{
    \begin{array}{ll}
    \infty &\text{si }t=0,\\
    0 &\text{si }t\ne0.
    \end{array}\right.

sous la contrainte :

.. math ::

    \int_{-\infty}^{\infty}\delta(t)dt=1

Représentation
++++++++++++++

.. plot::
    :context: close-figs

    import numpy 
    import matplotlib.pyplot as plt 

    # plot figure
    t = np.array([-0.5, 1])
    u = (t==0)
    

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t,u)
    ax.set_ylim([-0.5, 1.5])
    ax.set_xlim([-0.5, 1])
    ax.set_xlabel("$t$")
    ax.set_ylabel("$u(t)$")
    ax.annotate("", xy=(0, 1), xytext=(0, 0), arrowprops=dict(arrowstyle="->",linewidth=2,color="C0"))
    plt.grid()


Echelon Unitaire
----------------

Modèle Mathématique 
+++++++++++++++++++

.. math ::

    u(t)=\left\{
    \begin{array}{ll}
    1 &\text{si }t\ge 0,\\
    0 &\text{si }t<0.
    \end{array}\right.

Représentation
++++++++++++++

.. plot::
    :context: close-figs

    import numpy 
    import matplotlib.pyplot as plt 

    # plot figure
    t = np.array([-0.5, -0.0001, 0, 1])
    u = (t>=0)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t,u)
    ax.set_ylim([-0.5, 1.5])
    ax.set_xlim([-0.5, 1])
    ax.set_xlabel("$t$")
    ax.set_ylabel("$u(t)$")
    plt.grid()


Sinusoïde 
---------

Modèle Mathématique 
+++++++++++++++++++

.. math ::

    e(t)=E \cos(\omega t + \varphi_e)

* :math:`\omega=2\pi f` correspond à la pulsation [rad/s], :math:`f=1/T` correspond à la fréquence [Hz] et :math:`T` correspond à la période [s].
* :math:`E` correspond à l'amplitude crête,
* :math:`\varphi_e` correspond à la phase initiale.

Représentation
++++++++++++++

.. plot::
    :context: close-figs

    import numpy 
    import matplotlib.pyplot as plt 

    # plot figure
    E = 1.2
    phi = 0.1
    f = 2
    T = 1/f
    t = np.arange(-1, 1, 0.01)
    e = E*np.cos(2*np.pi*f*t+phi)
    t0 = -phi/(2*np.pi*f)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t,e)
    ax.plot([-0.5, 1],[E, E],"r--", linewidth=1)
    ax.plot([t0, t0],[-1.5, 1.5],"r--", linewidth=1)
    ax.plot([t0+T, t0+T],[-1.5, 1.5],"r--", linewidth=1)
    ax.annotate("", xy=(t0+T, 0.1), xytext=(t0, 0.1), arrowprops=dict(arrowstyle="<->",linewidth=1,color="r"))
    ax.annotate("", xy=(-0.2, E), xytext=(-0.2, 0), arrowprops=dict(arrowstyle="<->",linewidth=1,color="r"))
    ax.text(-0.3, E/2, "$E$", fontsize=12,color="r")
    ax.text(t0+T/2-0.1, 0.2, "$T=1/f$", fontsize=12,color="r")
    ax.set_ylim([-1.5, 1.5])
    ax.set_xlim([-0.5, 1])
    ax.set_xlabel("$t$")
    ax.set_ylabel("$e(t)$")
    plt.grid()
