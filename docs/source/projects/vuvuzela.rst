Projet: Débruitage de Vuvuzela 
==============================


Acquis d'Apprentissage Visés
----------------------------

* AAv1 (Étude de circuits électronique d’ordre 2) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de déterminer sous forme analytique ou numérique les paramètres caractéristiques d’un circuit du 2nd ordre en fonction de la valeur de ses composants en déterminant au préalable sa fonction de transfert. Les paramètres caractéristiques comprennent:

   * le type de filtre;
   * le coefficient d’amplification;
   * la fréquence propre;
   * le coefficient d’amortissement.

* AAv4 (Design) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de proposer un circuit respectant un cahier des charges. Le cahier des charges sera spécifié sous la forme soit par de plusieurs paramètres caractéristiques d’une cellule d’ordre 2 (type, coefficient d’amplification, fréquence propre, coefficient d’amortissement) ou soit par un gabarit fréquentiel. L'étudiant sera en mesure de vérifier la conformité de sa proposition avec le cahier des charges en utilisant un logiciel de simulation (Python/Numpy/Scipy et LTspice).

* AAv5 (Restitution) A l’issue du 4e semestre d’électronique, l’étudiant sera capable de rédiger un rapport de synthèse technique dans un support adapté comprenant du texte, des illustrations, du code, des résultats d'expérimentation en laboratoire.


Description du travail
----------------------

Lors de la Coupe du Monde de Football en 2010, un phénomène sonore a marqué les téléspectateurs du monde entier : le bruit omniprésent du Vuvuzela. Originaire d'Afrique du Sud, cet instrument produit une tonalité continue, qui, bien qu'étant partie intégrante de l'ambiance festive, a parfois nui à la clarté des commentaires sportifs pendant la retransmission des matchs. Pour avoir un aperçu, vous pouvez écouter l'extrait suivant : https://www.youtube.com/watch?v=bKCIFXqhLzo.

Le défi de ce projet est de concevoir un filtre "anti-vuvuzela". Votre mission sera d'atténuer spécifiquement les fréquences sonores produites par cet instrument afin de mettre en avant la qualité audio des commentaires. Le fichier audio à analyser et traiter est mis à votre disposition sur la plateforme Moodle.

Méthodologie 
++++++++++++

En première approximation, un son de vuvuzela peut être modélisé mathématiquement comme une somme de sinusoîdes ayant des fréquences fixes dans le temps (signal stationnaire).

Pour supprimer le son de vuvuzela, une solution possible consiste alors à cascader filtres rejecteur d’ordre 2 convenable paramétrés. Chacun de ces filtres aura pour objectif de supprimer une composante fréquentielle particulière du son de vuvuzela. Pour implementer cette cascade de filtres, il est recommandé d’utiliser la stratégie suivante :

* Analyse du fichier sonore vuvuzela.wav

    - Détermination du nombre :math:`l` de composantes sinusoïdales significatives,
    - Détermination des fréquences :math:`f_l` pour :math:`l=1, \cdots, L`,
    - Détermination approximative de  :math:`m`.

* Mise en oeuvre du filtre :

    - choix d’une topologie de filtre rejecteur,
    - détermination des composants du filtre,
    - vérification sur Ltspice
    - implémentation du filtre et **vérification du comportement fréquentiel**.

Liste des filtres
+++++++++++++++++

Filtres Passifs
```````````````

.. figure:: img/RLC.svg
   :alt: RLC

   Filtre RLC Notch

.. figure:: img/twin_T.svg
   :alt: RLC

   Filtre Twin-T

Filtres Actifs
``````````````

* Twin T Notch Filter: https://www.analog.com/media/en/training-seminars/tutorials/MT-225.pdf
* Bainter Notch Filters: https://www.analog.com/media/en/training-seminars/tutorials/MT-203.pdf


Méthodologie
------------

Le travail réalisé dans ce projet doit vous permettre d'acquérir un certain nombre d'apprentissages. 
La notation du projet sera basée sur la validation des acquis d'apprentissage suivants.


AAv1 (Étude de circuits électronique d’ordre 2)
+++++++++++++++++++++++++++++++++++++++++++++++

* A l’issue du 4e semestre d’électronique, l’étudiant sera capable de déterminer sous forme analytique ou numérique les paramètres caractéristiques d’un circuit du 2nd ordre en fonction de la valeur de ses composants en déterminant au préalable sa fonction de transfert. 

Pour atteindre cet objectif, vous devrez être en mesure de :

    * Calculer la fonction de transfert de plusieurs filtres rejecteurs. 
    * Déterminer pour chaque filtre : le coefficient d’amplification, la fréquence propre, le coefficient d’amortissement.


AAv4 (Design)
+++++++++++++

*  A l’issue du 4e semestre d’électronique, l’étudiant sera capable de proposer un circuit respectant un cahier des charges. Le cahier des charges sera spécifié sous la forme soit par de plusieurs paramètres caractéristiques d’une cellule d’ordre 2 (type, coefficient d’amplification, fréquence propre, coefficient d’amortissement) ou soit par un gabarit fréquentiel. L'étudiant sera en mesure de vérifier la conformité de sa proposition avec le cahier des charges en utilisant un logiciel de simulation (Python/Numpy/Scipy et LTspice).

Pour atteindre cet objectif, vous devrez être en mesure de :

   * Traduire le besoin sous la forme d'un cahier des charges contenant plusieurs spécifications, 
   * Choisir la topologie de filtre appropriée,
   * Calculer les valeurs des composants : Vous devrez être en mesure de calculer efficacement les valeurs des composants tels que les résistances, les condensateurs, etc. pour réaliser la topologie de filtre choisie. 
   * Valider le comportement du filtre : Vous devrez être en mesure de vérifier la réponse fréquentielle du filtre en fonction des spécifications du cahier des charges. Cette validation sera réalisée en utilisant des outils de simulations de circuit ET **des mesures en laboratoire et en mesurant certains paramètres clé de la réponse fréquentielle**. 
   * Optimiser le filtre : Si la réponse du filtre ne répond pas aux spécifications du cahier des charges, vous devrez être en mesure d'optimiser le filtre en ajustant les valeurs des composants ou en choisissant une topologie de filtre différente.
   * Présenter les résultats des différents filtres audio de manière claire et synthétique.
   * Comparer les performances des différents filtres et identifier leurs limites. 

AAv5 (Restitution)
++++++++++++++++++

* A l’issue du 4e semestre d’électronique, l’étudiant sera capable de rédiger un rapport de synthèse technique dans un support adapté comprenant du texte, des illustrations, du code, des résultats d'expérimentation en laboratoire.

Pour atteindre cet objectif, vous devrez être en mesure de :

    * Comprendre les besoins du lecteur et d'adapter son rapport en conséquence.
    * Utiliser un support adapté pour votre restitution respectant des contraintes de sobriété numérique (taille raisonnable) et de confidentialité (travail uniquement communiqué aux membres du binôme et à l'enseignant),
    * Maîtriser la structure du rapport de synthèse technique : L'étudiant sera capable de créer une structure de rapport claire et logique, en utilisant des titres et des sous-titres appropriés pour faciliter la lecture et la compréhension du contenu.
    * Maîtriser les compétences de rédaction : L'étudiant sera capable d'écrire un texte clair et concis, en utilisant un langage technique adapté, sans ambiguïté ni erreurs d'orthographe ou grammaticales.
    * Intégrer des illustrations et des images : L'étudiant sera en mesure d'intégrer des illustrations, des images et des graphiques pertinents pour améliorer la compréhension du contenu et rendre le rapport plus attractif.
    * Intégrer du code informatique : L'étudiant sera en mesure d'intégrer du code informatique pertinent dans son rapport et d'expliquer de manière claire le fonctionnement du code et les résultats obtenus.
    * Rédiger des résultats d'expérimentation : L'étudiant sera capable de synthétiser des résultats d'expérimentation en laboratoire de manière précise et critique, en utilisant des graphiques et des images pour faciliter la compréhension des résultats.
    * (Respecter les normes de citation : L'étudiant sera en mesure de respecter les normes de citation et d'utiliser les références appropriées pour citer les sources consultées lors de la rédaction du rapport).


Utilisation du Matériel
-----------------------

Générateur SDG 1032X
++++++++++++++++++++

.. figure:: img/awg.jpg
   :alt: AWG
   :width: 300

* documentation: https://siglentna.com/wp-content/uploads/dlm_uploads/2021/01/SDG1000-Service-Manual_SM02010-E01C.pdf
* programming guide: https://siglentna.com/wp-content/uploads/dlm_uploads/2023/01/SDG_Programming-Guide_PG02-E05A-12.pdf


Oscilloscope SDS 1104X-E
++++++++++++++++++++++++

.. figure:: img/oscillo.jpg
   :alt: AWG
   :width: 300


* documentation: https://siglentna.com/USA_website_2014/Documents/UserManual/SDS1000X&Xplus_UserManual_UM0101X-E02A.pdf
* programming guide: https://int.siglent.com/u_file/document/SDS1000%20Series&SDS2000X&SDS2000X-E_ProgrammingGuide_PG01-E02D.pdf

Obtention des diagrammes de Bode 
++++++++++++++++++++++++++++++++

L'oscilloscopes et le générateur sont connectés en USB. Cette connexion permet de réaliser des diagrammes de Bode:

* raccorder le générateur à l'entrée de votre circuit, 
* raccorder le générateur à l'entrée CH1 de l'oscilloscope, 
* raccorder la sortie de votre circuit à l'entrée CH2 de l'oscilloscope,
* Sur l'oscilloscope, appuyer sur le bouton `utility`, page 2/4, puis `Bode Plot II`.

Il est possible de calibrer le balayage réalisé par le générateur (menu `config`).

* Dans le menu `config` puis `set_channel`, vérifier que DUT Input=CH1 et DUT Output1=CH2.


Utilisation avec PyVisa
+++++++++++++++++++++++

Installation
````````````

Pour communiquer avec le matériel en salle de TP, une solution consiste à utiliser le driver NI-VISA

* Installation de l'outil NI-VISA: https://www.ni.com/fr-fr/support/downloads/drivers/download.ni-visa.html#464578
* Installation de la librairie python `pyvisa` permettant d'utiliser le driver

.. code ::

    conda install -c conda-forge pyvisa


Programme de Test
`````````````````

.. code ::

    import pyvisa
    import numpy as np
    import matplotlib.pyplot as plt
    
    rm = pyvisa.ResourceManager()
    ressources = rm.list_resources()
    print("liste des ressources: {}".format(ressources))
    print("ressource chargée: instrument {}\n".format(ressources[-1])) #chez moi, c'est la dernière ressource

    sds = rm.open_resource(ressources[-1]) 
    sds.timeout = 30000
    sds.chunk_size = 20*1024*1024
    sds.write("chdr off") # control oscilloscope response format (no string header)
    print("ID: {}".format(sds.query("*IDN?")))

Récuperation des courbes
````````````````````````

.. code ::

    def save_image(sds, filename):
        sds.write("SCDP")
        result_str = sds.read_raw()
        f = open(filename,'wb') 
        f.write(result_str)
        f.flush() 
        f.close()

    save_image(sds, "mon_image.bmp")


Récupération des données 
`````````````````````````

.. code ::

    def get_signal(sds, channel="C1"):
    
        vdiv = float(sds.query("c1:vdiv?"))
        offset = float(sds.query("c1:ofst?"))
        tdiv = float(sds.query("tdiv?"))
        f_s = float(sds.query("sara?"))
        sds.write("{}:wf? dat2".format(channel))
        recv = list(sds.read_raw())[15:]
        recv.pop()
        recv.pop()
        
        s = np.array(recv)
        s = s - 256*(s>127)
        s = s/25*vdiv - offset
        t = -(tdiv*7) + np.arange(len(s))/f_s
        return t, s

    t, s = get_signal(sds)
    plt.plot(t, s)
    plt.xlabel("Time [s]")
    plt.ylabel("CH1 [V]")
    plt.grid()