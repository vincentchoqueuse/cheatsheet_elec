Rappels Mathematiques
=====================

Nombres Complexes
-----------------

Notons :math:`j` l'imaginaire pur tel que :math:`j^2=-1` et :math:`\mathbb{C}` le corps des complexes.

Forme algébrique
++++++++++++++++

Tout nombre complexe :math:`z\in \mathbb{C}` s'écrit sous la forme :

.. math::

    z=a+jb


* :math:`a=\Re e(z)` correspond à la partie réelle,
* :math:`b=\Im m(z)`  correspond à la partie imaginaire.

.. plot::
    :context: close-figs

    # compute frequency response
    import numpy 
    import matplotlib.pyplot as plt 

    # plot figure
    z = 0.9 + 0.75j

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(np.real(z),np.imag(z),"*")
    ax.text(np.real(z)+0.05,np.imag(z)+0.05, "z", fontsize=12)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.set_xlabel("$\Re e(.)$", loc='right')
    ax.set_ylabel("$\Im m(.)$", loc='top')
    

    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_position('center')
    ax.set_xticks([np.real(z)],["a"])
    ax.set_yticks([np.imag(z)],["b"])
    plt.grid()

Complexe Conjugué
`````````````````

On appelle conjugué de :math:`z` le nombre complexe 

.. math::

    z^*=a-jb


Exponentielle Complexe
``````````````````````

L'exponentielle complexe est définie par 

.. math ::

    e^{j\theta}=\cos(\theta)+j\sin(\theta)



* Multiplication : La multiplication de deux exponentielles complexes donne : :math:`e^{j\theta_1}e^{j\theta_2}=e^{j(\theta_1+\theta_2)}`,
* Conjugaison :  Le conjugué d'une exponentielle complexe est égal à : :math:`\left(e^{j\theta}\right)^*=e^{-j\theta}`,
* Périodicité: L'exponentielle complexe est :math:`2\pi`-périodique,
* Formules d'Euler : Les formules d'Euler permettent d'exprimer le cosinus ou le sinus à partie de l'exponentielle complexe

.. math ::

    \cos(\theta)=\Re e(e^{j\theta})=\frac{1}{2}\left(e^{j\theta}+e^{-j\theta}\right)\\
    \sin(\theta)=\Im m(e^{j\theta})=\frac{1}{2j}\left(e^{j\theta}-e^{-j\theta}\right)



Forme Polaire
+++++++++++++

Tout nombre complexe :math:`z\in \mathbb{C}` non nul peut s'écrire sous la forme :

.. math ::

    z=\rho e^{j\theta}

* :math:`\rho = |z|` correspond au module,
* :math:`\theta=\arg[z]` correspond à l'argument (modulo :math:`2\pi`). 

.. plot::
    :context: close-figs

    import numpy 
    import matplotlib.pyplot as plt 

    # plot figure
    z = 0.9 + 0.75j
    r = np.abs(z)
    phi = np.angle(z)
    phi_list = phi*np.arange(0,1,0.01)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(np.real(z),np.imag(z),"*")
    ax.plot([0, np.real(z)],[0, np.imag(z)],"k", linewidth=0.5)
    ax.plot(0.5*r*np.cos(phi_list),0.5*r*np.sin(phi_list),"k", linewidth=0.5)
    ax.text(0.5*np.real(z),0.5*np.imag(z)+0.1, "$\\rho = |z|$", fontsize=12, rotation=30)
    ax.text(0.6,0.2, "$\\theta = \\arg[z]$", fontsize=12, rotation=0)
    ax.text(np.real(z)+0.05,np.imag(z)+0.05, "z", fontsize=12)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.set_xlabel("$\Re e(.)$", loc='right')
    ax.set_ylabel("$\Im m(.)$", loc='top')
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_position('center')
    ax.set_xticks([np.real(z)],["a"])
    ax.set_yticks([np.imag(z)],["b"])
    plt.grid()

Propriétés
``````````

Soit deux complexes :math:`z_1` et :math:`z_2`. 

* Le module et l'argument de :math:`z=z_1z_2` sont donnés par :

.. math ::

    |z|&=|z_1| \times |z_2|\\
    \arg[z] &= \arg[z_1]+\arg[z_2]

* Le module et l'argument de :math:`z=z_1/ z_2` sont donnés par :


.. math ::

    |z|&=\frac{|z_1|}{|z_2|}\\
    \arg[z] &= \arg[z_1]-\arg[z_2]


Conversion
``````````

Soit un nombre complexe :math:`z=a+jb`, alors

.. math ::

    |z|&=\sqrt{a^2+b^2}\\
    \theta&= \left\{\begin{array}{lc} \arctan(b/a) & \text{, si }a>0,\\
        \pi +\arctan(b/a) & \text{, si }a<0.\\
        \end{array}\right.


Polynômes
---------


Forme générale 
++++++++++++++

Modèle Mathématique
```````````````````

Un polynôme de degré :math:`n` est décrit par l'équation suivante :

.. math :: 

    p(x)=a_nx^n+\cdots + a_1 x+a_0

* :math:`n` correspond au degré du polynôme,
* :math:`a_l` correspondent aux coefficients du polynôme.

Racines 
``````` 

Les racines d'un polynôme de degré :math:`n` correspondent aux solutions de l'équation polynomiale suivante :

.. math :: 

    p(x)=0

Lorsque les coefficients :math:`a_l` sont réels et non nuls, le polynôme :math:`p(x)` possède au plus :math:`n` racines. Ces racines peuvent être réelles ou complexes.

Cas du degré 2
++++++++++++++

Modèle Mathématique
```````````````````

Un polynôme de degré 2 est décrit par l'équation suivante :

.. math :: 

    p(x)=a x^2+ b x+c


Racines 
```````

L'expression des racines s'obtient en évaluant le discriminant :

.. math ::

    \Delta = b^2 - 4ac

* Si :math:`\Delta>0`, le polynôme possède deux racines réelles distinctes :

.. math ::

    x_1 = \frac{-b+\sqrt{\Delta}}{2a}\\
    x_2 = \frac{-b-\sqrt{\Delta}}{2a}

* Si :math:`\Delta=0`, le polynôme possède une racine double réelle :

.. math ::

    x_1 = x_2 = -\frac{b}{2a}

* Si :math:`\Delta<0`, le polynôme possède deux racines complexes distinctes :

.. math ::

    x_1 = \frac{-b+j\sqrt{-\Delta}}{2a}\\
    x_2 = \frac{-b-j\sqrt{-\Delta}}{2a}