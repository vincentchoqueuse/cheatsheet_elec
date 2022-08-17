Liste des Fonctions de Transfert 
================================

Premier ordre
-------------

Passe-bas (LP)
++++++++++++++

.. math::

    H(p)=\frac{T_0}{\tau p+1}​

* gain statique: :math:`T_0`, 
* constante de temps (en s): :math:`\tau \ge 0` (en s),

**Réponse Indicielle**

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    tau = 1
    sys = lti([T0],[tau,1])

    t = np.arange(0,7,0.1)
    t,s = sys.step(T=t)

    fig, axs = plt.subplots(1, 1)
    axs.plot(t, s)
    axs.set_title("Réponse Indicielle")
    axs.set_xticks([0,3])
    axs.set_xticklabels(["0","$3\\tau$"])
    axs.set_yticks([0,1.9,2])
    axs.set_yticklabels(["0","$0.95T_0E$","$T_0E$"])
    axs.set_xlabel("t [s]")
    axs.set_xlim([0,7])
    axs.set_ylim([0,2.2])
    axs.grid()
    fig.tight_layout()

* Valeur Finale: :math:`s(\infty)=T_0E`,
* Valeur Initiale: :math:`s(0)=0`,
* Temps de réponse à 95%: :math:`t_r=3\tau`,


**Comportement Fréquentiel**

* Basse-Fréquences: :math:`H(j\omega)\approx T_0`,
* pulsation de coupure à -3dB: :math:`\omega_c = \frac{1}{\tau}` (rad/s).


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    tau = 1
    sys = lti([T0],[tau,1])
    w = np.logspace(-2,2,100)
    w,Hjw = sys.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw))
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[0].set_yticks([2/np.sqrt(2),2])
    axs[0].set_yticklabels(["$\\frac{T_0}{\\sqrt{2}}$","$T_0$"])
    axs[0].grid()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[1].set_yticks([-90,-45,0])
    axs[1].set_yticklabels(["-90","-45","0"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()


Passe-haut (HP)
+++++++++++++++

.. math::

    H(p)=\frac{T_m\tau p}{\tau p+1}​

* gain haute-fréquence: :math:`T_m`, 
* constante de temps (en s): :math:`\tau \ge 0` constante de temps (en s).

**Réponse Indicielle**


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    Tm = 2
    tau = 1
    sys = lti([T0*tau,0],[tau,1])

    t = np.arange(0,7,0.1)
    t,s = sys.step(T=t)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw))
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[0].set_yticks([2/np.sqrt(2),2])
    axs[0].set_yticklabels(["$\\frac{T_m}{\\sqrt{2}}$","$T_m$"])
    axs[0].grid()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[1].set_yticks([0,45,90])
    axs[1].set_yticklabels(["0","45","90"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()


**Comportement Fréquentiel**

* pulsation de coupure à -3dB: :math:`\omega_c = \frac{1}{\tau}` (rad/s).


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    Tm = 2
    tau = 1
    sys = lti([T0*tau,0],[tau,1])

    w = np.logspace(-2,2,100)
    w,Hjw = sys.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw))
    axs[1].semilogx(w, 180*np.angle(Hjw)/np.pi)
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[0].set_yticks([2/np.sqrt(2),2])
    axs[0].set_yticklabels(["$\\frac{T_m}{\\sqrt{2}}$","$T_m$"])
    axs[0].grid()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_c=\\frac{1}{\\tau}$"])
    axs[1].set_yticks([0,45,90])
    axs[1].set_yticklabels(["0","45","90"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()


Second Ordre
------------

Passe-bas (LP)
++++++++++++++

.. math::

    H(p)=\frac{T_0}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain statique: :math:`T_0`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`.

**Réponse Indicielle**

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0],[(1/w0**2),2*m3/w0,1])

    t = np.arange(0,50,0.5)
    t,s1 = sys1.step(T=t)
    t,s2 = sys2.step(T=t)
    t,s3 = sys3.step(T=t)

    fig, axs = plt.subplots(1, 1)
    axs.plot(t, s1,label="$m=2$")
    axs.plot(t, s2,label="$m=0.8$")
    axs.plot(t, s3,label="$m=0.1$")
    axs.set_title("Réponse Indicielle")
    axs.set_yticks([0,1.9,2,2.1])
    axs.set_yticklabels(["0","$0.95T_0E$","$T_0E$","$1.05T_0E$"])
    axs.set_xticks([])
    axs.set_xticklabels([])
    axs.set_xlabel("t [s]")
    axs.set_xlim([0,50])
    axs.set_ylim([0,3.6])
    axs.grid()
    axs.legend()
    fig.tight_layout()


**Comportement Fréquentiel**

* Valeur à la pulsation propre: :math:`H(j\omega_0)=\frac{T_0}{2jm}`,
* Si :math:`m<0.7`, présence d'une résonance à la pulsation :math:`\omega_r=\omega_0\sqrt{1-2m^2}` [rad/s]

.. math ::

    |H(j\omega_r)|=\frac{T_0}{2m\sqrt{1-m^2}}


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0],[(1/w0**2),2*m3/w0,1])

    w = np.logspace(-2,2,200)
    w,Hjw1 = sys1.freqresp(w=w)
    w,Hjw2 = sys2.freqresp(w=w)
    w,Hjw3 = sys3.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw1),label="$m=2$")
    axs[0].loglog(w, np.abs(Hjw2),label="$m=0.8$")
    axs[0].loglog(w, np.abs(Hjw3),label="$m=0.1$")
    axs[1].semilogx(w, 180*np.angle(Hjw1)/np.pi,label="$m=2$")
    axs[1].semilogx(w, 180*np.angle(Hjw2)/np.pi,label="$m=0.8$")
    axs[1].semilogx(w, 180*np.angle(Hjw3)/np.pi,label="$m=0.1$")
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_0$"])
    axs[0].set_yticks([2])
    axs[0].set_yticklabels(["$T_0$"])
    axs[0].grid()
    axs[0].legend()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_0$"])
    axs[1].set_yticks([-180,-90,0])
    axs[1].set_yticklabels(["-180","-90","0"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()


Passe-bande (BP)
++++++++++++++++

.. math::

    H(p)=\frac{\frac{2mT_m}{\omega_0}p}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain maximum: :math:`T_m`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 

**Réponse Indicielle**


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([2*m1*T0/w0,0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([2*m2*T0/w0,0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([2*m3*T0/w0,0],[(1/w0**2),2*m3/w0,1])

    t = np.arange(0,20,0.1)
    t,s1 = sys1.step(T=t)
    t,s2 = sys2.step(T=t)
    t,s3 = sys3.step(T=t)

    fig, axs = plt.subplots(1, 1)
    axs.plot(t, s1,label="$m=2$")
    axs.plot(t, s2,label="$m=0.8$")
    axs.plot(t, s3,label="$m=0.1$")
    axs.set_title("Réponse Indicielle")
    axs.set_yticks([0,2])
    axs.set_yticklabels(["0","$T_mE$"])
    axs.set_xticks([])
    axs.set_xticklabels([])
    axs.set_xlabel("t [s]")
    axs.set_xlim([0,20])
    axs.set_ylim([-0.5,2])
    axs.grid()
    axs.legend()
    fig.tight_layout()

**Comportement Fréquentiel**

* Valeur à la pulsation propre: :math:`H(j\omega_0)=T_m`,
* Intersection des asymptotes de module: :math:`T_i=2m T_m`, 
* Largeur de la bande passante à -3dB: :math:`\Delta \omega =2m \omega_0` [rad/s].


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([2*m1*T0/w0,0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([2*m2*T0/w0,0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([2*m3*T0/w0,0],[(1/w0**2),2*m3/w0,1])

    w = np.logspace(-2,2,200)
    w,Hjw1 = sys1.freqresp(w=w)
    w,Hjw2 = sys2.freqresp(w=w)
    w,Hjw3 = sys3.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw1),label="$m=2$")
    axs[0].loglog(w, np.abs(Hjw2),label="$m=0.8$")
    axs[0].loglog(w, np.abs(Hjw3),label="$m=0.1$")
    axs[1].semilogx(w, 180*np.angle(Hjw1)/np.pi,label="$m=2$")
    axs[1].semilogx(w, 180*np.angle(Hjw2)/np.pi,label="$m=0.8$")
    axs[1].semilogx(w, 180*np.angle(Hjw3)/np.pi,label="$m=0.1$")
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_0$"])
    axs[0].set_yticks([2])
    axs[0].set_yticklabels(["$T_m$"])
    axs[0].grid()
    axs[0].legend()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_0$"])
    axs[1].set_yticks([-90,0,90])
    axs[1].set_yticklabels(["-90","0","90"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()



Passe-haut (HP)
+++++++++++++++

.. math::

    H(p)=\frac{\frac{T_{\infty}}{\omega_0^2}p^2}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain haute-fréquence: :math:`T_{\infty}`,
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 

**Réponse Indicielle**

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m3/w0,1])

    t = np.arange(0,20,0.1)
    t,s1 = sys1.step(T=t)
    t,s2 = sys2.step(T=t)
    t,s3 = sys3.step(T=t)

    fig, axs = plt.subplots(1, 1)
    axs.plot(t, s1,label="$m=2$")
    axs.plot(t, s2,label="$m=0.8$")
    axs.plot(t, s3,label="$m=0.1$")
    axs.set_title("Réponse Indicielle")
    axs.set_yticks([0,2])
    axs.set_yticklabels(["0","$T_mE$"])
    axs.set_xticks([])
    axs.set_xticklabels([])
    axs.set_xlabel("t [s]")
    axs.set_xlim([0,20])
    axs.set_ylim([-2.2,2.2])
    axs.grid()
    axs.legend()
    fig.tight_layout()


**Comportement Fréquentiel**

* Valeur à la pulsation propre: :math:`H(j\omega_0)=j\frac{T_{\infty}}{2m}`,
* Si :math:`m<0.7`, présence d'une résonance à la pulsation :math:`\omega_r=\omega_0/\sqrt{1-2m^2}` [rad/s]

.. math ::

    |H(j\omega_r)|=\frac{T_{\infty}}{2m\sqrt{1-m^2}}


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0/(w0**2),0,0],[(1/w0**2),2*m3/w0,1])

    w = np.logspace(-2,2,200)
    w,Hjw1 = sys1.freqresp(w=w)
    w,Hjw2 = sys2.freqresp(w=w)
    w,Hjw3 = sys3.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw1),label="$m=2$")
    axs[0].loglog(w, np.abs(Hjw2),label="$m=0.8$")
    axs[0].loglog(w, np.abs(Hjw3),label="$m=0.1$")
    axs[1].semilogx(w, 180*np.angle(Hjw1)/np.pi,label="$m=2$")
    axs[1].semilogx(w, 180*np.angle(Hjw2)/np.pi,label="$m=0.8$")
    axs[1].semilogx(w, 180*np.angle(Hjw3)/np.pi,label="$m=0.1$")
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_0$"])
    axs[0].set_yticks([2])
    axs[0].set_yticklabels(["$T_m$"])
    axs[0].grid()
    axs[0].legend()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_0$"])
    axs[1].set_yticks([0,90,180])
    axs[1].set_yticklabels(["0","90","180"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()


Rejecteur (Notch)
+++++++++++++++++

.. math::

    H(p)=\frac{T_0\left(\frac{1}{\omega_0^2}p^2+1\right)}{\frac{1}{\omega_0^2}p^2+\frac{2m}{\omega_0}p+1}​

* gain maximum: :math:`T_0`, 
* pulsation propre: :math:`\omega_0` (rad/s),
* coefficient d'amortissement: :math:`m`. 

**Réponse Indicielle**

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m3/w0,1])

    t = np.arange(0,20,0.1)
    t,s1 = sys1.step(T=t)
    t,s2 = sys2.step(T=t)
    t,s3 = sys3.step(T=t)

    fig, axs = plt.subplots(1, 1)
    axs.plot(t, s1,label="$m=2$")
    axs.plot(t, s2,label="$m=0.8$")
    axs.plot(t, s3,label="$m=0.1$")
    axs.set_title("Réponse Indicielle")
    axs.set_yticks([0,2])
    axs.set_yticklabels(["0","$T_{0}E$"])
    axs.set_xticks([])
    axs.set_xticklabels([])
    axs.set_xlabel("t [s]")
    axs.set_xlim([0,20])
    axs.set_ylim([0,2.7])
    axs.grid()
    axs.legend()
    fig.tight_layout()



**Comportement Fréquentiel**

* Valeur à la pulsation propre: :math:`H(j\omega_0)=0`,
* Largeur de la bande rejetée à -3dB: :math:`\Delta \omega =2m \omega_0` [rad/s].


.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    T0 = 2
    w0 = 1
    m3 = 0.1
    m2 = 0.8
    m1 = 2
    tau = 1
    sys1 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m1/w0,1])
    sys2 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m2/w0,1])
    sys3 = lti([T0/(w0**2),0,T0],[(1/w0**2),2*m3/w0,1])

    w = np.logspace(-2,2,200)
    w,Hjw1 = sys1.freqresp(w=w)
    w,Hjw2 = sys2.freqresp(w=w)
    w,Hjw3 = sys3.freqresp(w=w)

    fig, axs = plt.subplots(2, 1)
    axs[0].loglog(w, np.abs(Hjw1),label="$m=2$")
    axs[0].loglog(w, np.abs(Hjw2),label="$m=0.8$")
    axs[0].loglog(w, np.abs(Hjw3),label="$m=0.1$")
    axs[1].semilogx(w, 180*np.angle(Hjw1)/np.pi,label="$m=2$")
    axs[1].semilogx(w, 180*np.angle(Hjw2)/np.pi,label="$m=0.8$")
    axs[1].semilogx(w, 180*np.angle(Hjw3)/np.pi,label="$m=0.1$")
    axs[0].set_xticks([1])
    axs[0].set_xticklabels(["$\omega_0$"])
    axs[0].set_yticks([2])
    axs[0].set_yticklabels(["$T_{0}$"])
    axs[0].grid()
    axs[0].legend()
    axs[0].set_ylabel("$|H(j\omega)|$")
    axs[0].set_title("Réponse Frequentielle")
    axs[1].set_xlabel("w [rad/s]")
    axs[1].set_ylabel("$\\arg[H(j\omega)]$ [deg]")
    axs[1].set_xticks([1])
    axs[1].set_xticklabels(["$\omega_0$"])
    axs[1].set_yticks([-90,0,90])
    axs[1].set_yticklabels(["-90","0","90"])
    axs[1].grid()
    axs[0].set_xlim([0.01,100])
    axs[1].set_xlim([0.01,100])
    fig.tight_layout()