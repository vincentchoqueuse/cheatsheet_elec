Cours 
=====

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   rappels/index
   transfer_function
   first_order
   second_order
   filter_synthesis
   signal_list
   circuit_list
   

Acquis d'Apprentissage Visés
----------------------------

* AAv1 (Étude de circuits électronique d’ordre 2) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de déterminer sous forme analytique ou numérique les paramètres caractéristiques d’un circuit du 2nd ordre en fonction de la valeur de ses composants en déterminant au préalable sa fonction de transfert. Les paramètres caractéristiques comprennent:
   * le type de filtre;
   * le coefficient d’amplification;
   * la fréquence propre;
   * le coefficient d’amortissement.
* AAv2 (Modélisation et représentations des systèmes LTI ordre 1 et 2) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de déterminer, pour un système LTI décrit dans un formalisme donné, la réponse indicielle et fréquentielle en utilisant la résolution de l’équation différentielle ou la transformée de Laplace, et de représenter ces réponses sous forme adéquates. Les formalismes considérés incluent:
   * la forme factorisée: z,p,k;
   * la forme polynomiale: b,a. L’étudiant sera en mesure de vérifier la validité de ses développements avec un logiciel de simulation (Python/Numpy/Scipy).
* AAv3 (Caractérisation et identification) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de caractériser le comportement d’un système LTI représenté par sa réponse indicielle, sa réponse fréquentielle ou son diagramme des pôles et des zéros. La caractérisation portera sur les critères suivants:
   * Caractéristiques temporelles: stabilité, présence de dépassement, temps de réponse à 5 %, 
   * Caractéristiques fréquentielles: type, amplification, fréquence propre, amortissement, comportement asymptotique.
* AAv4 (Design) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de proposer un circuit respectant un cahier des charges. Le cahier des charges sera spécifié sous la forme soit par de plusieurs paramètres caractéristiques d’une cellule d’ordre 2 (type, coefficient d’amplification, fréquence propre, coefficient d’amortissement) ou soit par un gabarit fréquentiel. L'étudiant sera en mesure de vérifier la conformité de sa proposition avec le cahier des charges en utilisant un logiciel de simulation (Python/Numpy/Scipy et LTspice).
* AAv5 (Restitution) : A l’issue du 4e semestre d’électronique, l’étudiant sera capable de rédiger un rapport de synthèse technique dans un support adapté comprenant du texte, des illustrations, du code, des résultats d'expérimentation en laboratoire.

Outils Numériques
-----------------

Cet enseignement utilise différents outils permettant d'illustrer un certain nombre de notions.

* LTspice (Simulation de Circuits): LTspice est un simulateur SPICE de haute performance qui permet de modéliser et d'analyser le comportement de circuits électroniques. C'est un outil essentiel pour vérifier les conceptions avant de procéder à la réalisation physique.
   * Visualisation: l'outil permet la visualisation des signaux, des caractéristiques de transfert et d'autres comportements des circuits, ce qui facilite la compréhension.
   * Composants Intégrés: LTspice contient une grande bibliothèque de composants, ce qui permet d'expérimenter avec différentes configurations et composants.
* Python avec numpy, scipy et matplotlib:
   * Traitement des Données: numpy est idéal pour les opérations mathématiques sur des tableaux, et scipy fournit des outils pour des opérations plus complexes telles que la transformation de Fourier ou la résolution d'équations différentielles, qui sont couramment utilisées en électronique.
   * Visualisation: matplotlib est une bibliothèque de visualisation qui peut être utilisée pour tracer des courbes, des histogrammes, des diagrammes de puissance, etc. Elle est essentielle pour analyser et comprendre les données issues des simulations ou des expérimentations.
   * Flexibilité: Python est un langage de programmation polyvalent, permettant de développer des outils ou des scripts personnalisés pour automatiser des tâches, traiter des données ou même interfacer avec du matériel électronique réel.
* Jupyter:
   * Interactivité: Les notebooks Jupyter offrent un environnement interactif où il est possible de combiner du code, des formules mathématiques, des visualisations et du texte de manière cohérente. Cela permet de créer des documents de travail clairs et illustrés.
   * Documenter et Partager: Jupyter permet de documenter son travail et de partager ses analyses et ses découvertes avec d'autres, facilitant ainsi la collaboration et la discussion.
   * Intégration avec Python: Jupyter supporte nativement Python, ce qui signifie qu'il peut utiliser numpy, scipy, matplotlib et d'autres bibliothèques directement à l'intérieur de leurs notebooks.

.. note ::
   
   Installation: Pour installer Python avec les librairies Numpy, Scipy et Maptplotlib, il est recommandé d'utiliser `conda` (:doc:`documentation <../cheatsheets/conda>`)