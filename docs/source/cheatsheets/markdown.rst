Markdown
========

L'outil jupyter permet de créer des cellules de texte. Ces cellules peuvent être mise en forme en utilisant le langage Markdown.


Le Markdown est un langage de balisage léger créé en 2004 par John Gruber avec une contribution importante d'Aaron Swartz. Conçu pour être facile à lire et à écrire, son design repose sur le principe selon lequel un texte formaté avec Markdown devrait être parfaitement lisible en tant que texte brut. Le nom "Markdown" est un jeu de mots sur "markup" (balisage en anglais), indiquant une réduction (ou simplification) des conventions traditionnelles de balisage.

Markdown est souvent utilisé pour la rédaction de documentation, pour écrire des messages dans des forums, ou pour créer des contenus pour le web. Sa syntaxe est délibérément simple, privilégiant une lisibilité immédiate. Avec une poignée de caractères spéciaux, les utilisateurs peuvent formater le texte, créer des listes, ajouter des liens et bien plus encore.

Aujourd'hui, grâce à sa simplicité et sa popularité croissante, Markdown est supporté par de nombreux éditeurs de texte et plateformes en ligne, dont GitHub, Reddit et Jekyll. Il existe également de nombreux convertisseurs qui transforment le Markdown en HTML, permettant ainsi une intégration facile sur le web.


Titres
------
.. code-block:: markdown

   # Titre de niveau 1
   ## Titre de niveau 2
   ### Titre de niveau 3
   #### Titre de niveau 4
   ##### Titre de niveau 5
   ###### Titre de niveau 6

Mise en forme du texte
----------------------
.. code-block:: markdown

   **texte en gras**
   __texte en gras__

   *texte en italique*
   _texte en italique_

   ~~texte barré~~

   `code`

Liens
-----
.. code-block:: markdown

   [Texte du lien](URL)
   [Texte du lien avec titre](URL "titre du lien")

Images
------
.. code-block:: markdown

   ![Texte alternatif](URL_de_l'image)
   ![Texte alternatif avec titre](URL_de_l'image "titre de l'image")

Listes
------
.. code-block:: markdown

   - Élément de liste non ordonnée
   * Autre élément de liste non ordonnée
   + Encore un autre élément de liste non ordonnée

   1. Élément de liste ordonnée
   2. Deuxième élément de liste ordonnée

Citations
---------

.. code-block:: markdown

   > Citation

Séparateurs
-----------

.. code-block:: markdown

   ---
   ou
   ***

Code
----

.. code-block:: markdown

   ```python
   print("Hello, World!")
   ```

Equations
---------

Sur une ligne séparée 
+++++++++++++++++++++

.. code-block:: markdown

    $$X(f) = \int_{-\infty}^{\infty} x(t)e^{-2j\pi ft}dt$$


Dans le texte  
+++++++++++++

.. code-block:: markdown

    en prenant $x(t)=\alpha$, nous obtenons ...



