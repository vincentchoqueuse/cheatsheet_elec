Superposition de courbes en Python 
==================================

Dans ce tutorial, nous montrons comment superposer une courbe obtenue avec Scipy et une courbe analytique. Plus spécifiquement, nous allons nous intéresser à la réponse 
fréquentielle d'un système de premier ordre.


.. plot ::
    :context: close-figs
    :include-source: true

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import lti, step

    TO = 1
    wc = 100
    tau = 1/wc
    H = lti([1], [tau, 1])

    # frequency response from scipy
    w, Hjw = H.freqresp()
    H_mod = np.abs(Hjw)

    # analytical frequency response
    H_mod2 = np.abs(TO) / np.sqrt(1+(w/wc)**2)

    # plot figure
    plt.loglog(w, H_mod, label="scipy")
    plt.loglog(w, H_mod2, "--", label="analytical")
    plt.grid()
    plt.legend()
    plt.xlabel("w [rad/s")
    plt.ylabel("Module")