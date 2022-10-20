Identification à partir de la réponse Indicielle
================================================

Dans ce tutorial, nous montrons comment identifier les paramètres d'un filtre d'ordre 2 à partir de sa réponse indicielle.

**Hypothèses**

* L'amplitude de l'échelon est égale à :math:`E` c-a-d :math:`e(t)=Eu(t)`.
* La réponse indicielle présente un dépassement (:math:`m<1`),
* La réponse indicielle présente au minimum deux dépassements de même signe (:math:`m\ll 1`),
* Le filtre est initialement au repos (:math:`s(0^-)=\dot{s}(0^-)=0`),
* Le filtre est soit un LP, un BP, un HP ou un BR,
* Les abaques de dépassement et de temps de réponse ne sont pas disponibles.


Réponse Indicielle 
------------------

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    m = 0.2
    w0 = 10
    T = 2

    den = [(1/(w0**2)),2*m/w0,1]
    sys = lti([T],den)
    
    
    t = np.arange(0, 10, 0.01)
    t,s = sys.step(T=t)
    t_2 = np.insert(t, 0, [-1,0], axis=0)
    s_2 = np.insert(s, 0, [0,0], axis=0)
    plt.plot([-0.1, 3], [2, 2], 'r--')
    plt.plot([-0.1, 3], [0, 0], 'r--')
    plt.plot([-0.1, 3], [3.05, 3.05], 'r--')
    plt.plot([-0.1, 3], [2.3, 2.3], 'r--')
    plt.plot([0.32, 0.32], [-0.2, 3.05], 'r--')
    plt.plot([0.96, 0.96], [-0.2, 2.3], 'r--')
    plt.xlim([-0.1, 3])
    plt.ylim([-0.2, 3.3])
    plt.plot(t_2,s_2,label="s(t)")
    t = np.array([-1, -0.0001, 0, 10])
    plt.plot(t,t>=0,label="u(t)")
    plt.yticks([0, 2], ["$s(0^+)$", "$s(\infty)$"])
    plt.annotate("", xy=(0.1, 1.95), xytext=(0.1, 3.1),arrowprops=dict(arrowstyle="<->"))
    plt.annotate("", xy=(0.7, 1.95), xytext=(0.7, 2.35),arrowprops=dict(arrowstyle="<->"))
    plt.annotate("", xy=(0.3, 0.2), xytext=(0.99, 0.2),arrowprops=dict(arrowstyle="<->"))
    plt.text(0, 2.5, "$D_1$", rotation="90")
    plt.text(0.6, 2.15, "$D_2$", rotation="90")
    plt.text(0.6, 0.3, "$T_p$")
    plt.xlabel("temps [s]")
    plt.ylabel("sortie")
    plt.grid()
    plt.legend()



* :math:`T_p`: période des pseudo-oscillations,
* :math:`R=D_1/D_2>1`: ratio de deux dépassements consécutifs de même signe.
* :math:`s(0^+)`: valeur initiale (et sa dérivée :math:`\dot{s}(0^+)` dans le cas d'un BP),
* :math:`s(\infty)`: valeur finale.

Identification du Type
----------------------

L'identification du type de filtre s'obtient à partir de l'analyse des conditions aux limites.

* Si le filtre ne laisse pas passer la discontinuité et présente un régime permanent non nul ( :math:`s(0^+)=0 \cap s(\infty)\ne 0`), alors :code:`type="LP"`,
* Si le filtre ne laisse pas passer la discontinuité et présente un régime permanent nul (:math:`s(0^+)=0 \cap s(\infty)= 0`), alors :code:`type="BP"`,
* Si le filtre laisse passer la discontinuité et présente un régime permanent nul (:math:`s(0^+)\ne 0 \cap s(\infty)= 0`), alors :code:`type="HP"`,
* Si le filtre laisse passer la discontinuité et présente un régime permanent non nul ( :math:`s(0^+)\ne 0 \cap s(\infty)\ne 0`), alors :code:`type="BR"`,

Identification des paramètres 
-----------------------------




Coefficient d'amortissement et Pulsation propre
+++++++++++++++++++++++++++++++++++++++++++++++

* Coefficient d'amortissement : :math:`m=\frac{\ln(R)}{2\pi}`,
* Pulsation propre: :math:`\omega_0 = \frac{2\pi}{T_p \sqrt{1-m^2}}`
 
Coefficient d'amplification
+++++++++++++++++++++++++++

* Pour le filtre LP, :math:`T_0= \frac{s(\infty)}{E}`,
* Pour le filtre HP, :math:`T_\infty= \frac{s(0^+)}{E}`,
* Pour le filtre BP, :math:`T_m = \frac{\dot{s}(0^+)}{2m\omega_0 E}`,
* Pour le filtre BR, :math:`T_0= \frac{s(\infty)}{E}` ou :math:`T_0= \frac{s(0^+)}{E}`.


