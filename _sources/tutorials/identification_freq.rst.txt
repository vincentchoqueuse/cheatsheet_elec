Identification à partir de la réponse Fréquentielle
===================================================

Dans ce tutorial, nous montrons comment identifier les paramètres d'un filtre d'ordre 2 à partir de sa réponse fréquentielle.

**Hypothèses**

* Le filtre est soit un LP, un BP, un HP ou un BR,
* L'abaque de résonance n'est pas disponible.


.. note :: 

    Avant toute identification, vérifiez si l'axe des abscisses est en rad/s ou en Hz.


Filtres LP et HP  
----------------

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    m = 0.25
    w0 = 10
    T = 2
    Hw0 = T/(2*m)

    den = [(1/(w0**2)),2*m/w0,1]
    sys = lti([T],den)
    wr = w0*np.sqrt(1-2*m**2)

    w, Hjw = sys.freqresp()
    H_mod = np.abs(Hjw)
    H_phase = 180*np.angle(Hjw)/np.pi     #convert radian to degree
    # plot figure
    plt.subplot(2,1,1)
    plt.loglog(w,H_mod)
    plt.plot([1, 100], [2, 2], 'r--')
    plt.plot([wr, wr], [0.01, 10], 'r--')
    plt.plot([w0, w0], [0.01, 10], 'r--')
    plt.yticks([2, Hw0], ["$|T|$", "$|H(j\omega_0)|$"])
    plt.xticks([wr, w0], ["$\omega_r$", "$\omega_0$"])
    plt.xlim([4, 40])
    plt.ylim([0.05, 10])
    plt.ylabel("Magnitude")
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot([w0, w0], [-200, 10], 'r--')
    plt.plot([0, w0], [-90, -90], 'r--')
    plt.semilogx(w,H_phase)
    plt.ylabel("Phase [deg]")
    plt.xlabel("w [rad/s]")
    plt.xlim([4, 40])
    plt.ylim([-180, 0])
    plt.xticks([w0], ["$\omega_0$"])
    plt.yticks([-90], ["$-90^o$"])
    plt.grid()
    plt.legend()


Paramètres à mesurer
++++++++++++++++++++

* :math:`\omega_0`: pulsation de symétrie de la phase. Lorsque la phase n'est pas disponible, il est possible d'approximer :math:`\omega_0` par :math:`\omega_r` lorsque :math:`m\ll 1`. 
* :math:`\Omega = [\varphi_{min}, \varphi_{max}]`: intervalle de la phase,
* :math:`|H(j\omega_0)|`: valeur du module en :math:`\omega_0`, 
* :math:`|T| = \lim_{\omega \to 0} |H(j\omega)|` ou :math:`|T| = \lim_{\omega \to \infty} |H(j\omega)|`: valeur de l'asymptote horizontale du module,

Identification des paramètres 
+++++++++++++++++++++++++++++

* Coefficient d'amplification: 

    * Pour le filtre LP: 
        
        * Si :math:`\Omega = [-180, 0]`, alors :math:`T_0 = |T|`
        * sinon :math:`T_0 = -|T|`

    * Pour le filtre HP: 

        * Si :math:`\Omega = [0, -180]`, alors :math:`T_{\infty} = |T|` 
        * sinon :math:`T_{\infty} = -|T|`

* Coefficient d'amortissement: :math:`m = \frac{|T|}{2|H(j\omega_0)|}`
 

Filtres BP et BR
----------------

.. plot ::
    :context: close-figs
    :include-source: false

    import numpy as np 
    from scipy.signal import lti
    import matplotlib.pyplot as plt

    m = 0.25
    w0 = 10
    T = 2
    Hw0 = T/(2*m)

    den = [(1/(w0**2)),2*m/w0,1]
    sys = lti([2*m*T/w0, 0],den)
    wc1 = w0*(-m+np.sqrt(m**2 + 1))
    wc2 = w0*(m+np.sqrt(m**2 + 1))

    w, Hjw = sys.freqresp()
    H_mod = np.abs(Hjw)
    H_phase = 180*np.angle(Hjw)/np.pi     #convert radian to degree
    # plot figure
    plt.subplot(2,1,1)
    plt.loglog(w,H_mod)
    plt.plot([1, 100], [2, 2], 'r--')
    plt.plot([1, 100], [2/np.sqrt(2), 2/np.sqrt(2)], 'r--')
    plt.plot([wc1, wc1], [0.01, 10], 'r--')
    plt.plot([wc2, wc2], [0.01, 10], 'r--')
    plt.plot([w0, w0], [0.01, 10], 'r--')
    plt.yticks([2, 2/np.sqrt(2)], ["$|T|$", "$|T|/\sqrt{2}$"])
    plt.xticks([wc1, w0, wc2], ["$\omega_{c1}$", "$\omega_0$", "$\omega_{c2}$"])
    plt.xlim([1, 100])
    plt.ylim([0.05, 10])
    plt.ylabel("Magnitude")
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot([w0, w0], [-100, 100], 'r--')
    plt.plot([0, w0], [0, 0], 'r--')
    plt.semilogx(w,H_phase)
    plt.ylabel("Phase [deg]")
    plt.xlabel("w [rad/s]")
    plt.xlim([1, 100])
    plt.ylim([-90, 90])
    plt.xticks([w0], ["$\omega_0$"])
    plt.yticks([0], ["$0^o$"])
    plt.grid()
    plt.legend()


Paramètres à mesurer
++++++++++++++++++++

* :math:`\omega_0`: pulsation de symétrie de la phase,
* :math:`\Omega = [\varphi_{min}, \varphi_{max}]`: intervalle de la phase,
* :math:`|T|`: valeur maximale du module, 
* :math:`\omega_{c1}` et :math:`\omega_{c2}` : pulsation de coupure à :math:`-3` dB.

Identification des paramètres 
+++++++++++++++++++++++++++++

* Coefficient d'amplification: 

    * Pour le filtre BP: 
        
        * Si :math:`\Omega = [-90, 90]`, alors :math:`T_{max} = |T|`
        * sinon :math:`T_{max} = -|T|`

    * Pour le filtre BR: 

        * Si :math:`\arg[H(j\omega)]=0` en BF ou HF, alors :math:`T_{0} = |T|` 
        * sinon :math:`T_{0} = -|T|`

* Coefficient d'amortissement: :math:`m =\frac{\Delta \omega}{2\omega_0}` où :math:`\Delta \omega =\omega_{c2}-\omega_{c1}`.
 
